// Draws red and blue bars using the Linux Framebuffer.
// Will not work over SSH or with X running.
//  - William A Stevens V (wasv)
// Known to work on a 1st gen Rasberry Pi.

// Based on tutorials from
// https://raspberrycompote.blogspot.ie/search/label/graphics
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <linux/kd.h>
#include <linux/vt.h>
#include <sys/mman.h>
#include <sys/ioctl.h>

typedef struct {
  int fd;
  int kbfd;
  char *fbp;
  struct fb_var_screeninfo vinfo;
  struct fb_var_screeninfo orig_vinfo;
  struct fb_fix_screeninfo finfo;
  int orig_vty;
} FBO;

void put_pixel(FBO *fb, int x, int y, int r, int g, int b)
{
    // calculate the pixel's byte offset inside the buffer
    // note: x * 3 as every pixel is 3 consecutive bytes
    unsigned int pix_offset = x * 3 + y * fb->finfo.line_length;

    // now this is about the same as 'fbp[pix_offset] = value'
    *((char*)(fb->fbp + pix_offset)) = r;
    *((char*)(fb->fbp + pix_offset + 1)) = g;
    *((char*)(fb->fbp + pix_offset + 2)) = b;
}

void FBO_deinit(FBO* fb) {
  if(fb->fbp != NULL) {
    munmap(fb->fbp, (fb->finfo.smem_len));
  }
  if (ioctl(fb->fd, FBIOPUT_VSCREENINFO, &fb->orig_vinfo)) {
    fputs("Error re-setting screen information.\n",stderr);
  }
  close(fb->fd);

  if(ioctl(fb->kbfd, KDSETMODE, KD_TEXT)) {
    fputs("Error re-setting cursor.\n",stderr);
  }
  //if (ioctl(fb->kbfd,VT_ACTIVATE,fb->orig_vty)) {
  //  fputs("chvt: VT_ACTIVATE\n", stderr);
  //}
  close(fb->kbfd);
  free(fb);
  fb = NULL;
}

FBO* FBO_init(const char* fbpath, const char* ttypath) {
  FBO *fb = malloc(sizeof(FBO));
  fb->fbp = NULL;
  // Open the file for reading and writing
  fb->fd = open(fbpath, O_RDWR);
  if (!fb->fd) {
    fputs("Error: cannot open framebuffer device.\n",stderr);
    FBO_deinit(fb);
    return NULL;
  }

  // Get variable screen information
  if (ioctl(fb->fd, FBIOGET_VSCREENINFO, &fb->vinfo)) {
    fputs("Error reading variable information.\n",stderr);
    FBO_deinit(fb);
    return NULL;
  }
  // Store for reset (copy vinfo to vinfo_orig)
  memcpy(&fb->orig_vinfo, &fb->vinfo,
         sizeof(struct fb_var_screeninfo));

  // Change variable info
  fb->vinfo.bits_per_pixel = 24;

  if (ioctl(fb->fd, FBIOPUT_VSCREENINFO, &fb->vinfo)) {
    fputs("Error setting screen information.\n",stderr);
    FBO_deinit(fb);
    return NULL;
  }

  // Get fixed screen information
  if (ioctl(fb->fd, FBIOGET_FSCREENINFO, &fb->finfo)) {
    fputs("Error reading fixed information.\n",stderr);
    FBO_deinit(fb);
    return NULL;
  }

  fprintf(stderr, "%dx%d, %d bpp\n", fb->vinfo.xres, fb->vinfo.yres, 
         fb->vinfo.bits_per_pixel );
  

  // map framebuffer to user memory 
  fb->fbp = (char*)mmap(0, 
                    fb->finfo.smem_len, 
                    PROT_READ | PROT_WRITE, 
                    MAP_SHARED, 
                    fb->fd, 0);

  if ((int)fb->fbp == -1) {
    fputs("Failed to mmap.\n",stderr);
    FBO_deinit(fb);
    return NULL;
  }

  fb->kbfd = open(ttypath, O_RDWR);
  if (fb->kbfd < -1) {
    fputs("Error opening console.\n",stderr);
    FBO_deinit(fb);
    return NULL;
  }

  //struct vt_stat vtstat;
  //if (ioctl(fb->kbfd, VT_GETSTATE, &vtstat)) {
  //  fputs("fgconsole: VT_GETSTATE\n", stderr);
  //  return NULL;
  //}
  //fb->orig_vty = vtstat.v_active;
  //if (ioctl(fb->kbfd,VT_ACTIVATE,8)) {
  //  fputs("chvt: VT_ACTIVATE\n", stderr);
  //  FBO_deinit(fb);
  //  return NULL;
  //}
  if (ioctl(fb->kbfd, KDSETMODE, KD_GRAPHICS)) {
    fputs("Warn: Could not hide cursor.\n",stderr);
  }

  return fb;
}

int main(int argc, char* argv[]) {
  FBO *fbo = FBO_init("/dev/fb0", "/dev/tty");
  if(fbo == NULL)
  {
    fputs("Error making FBO.\n",stderr);
    return -1;
  }
  fputs("Drawing...\n",stderr);
  // draw...
  for (unsigned int x = 0; x < fbo->vinfo.xres; x++) { 
    for (unsigned int y = 0; y < (fbo->vinfo.yres / 2); y++) {
      put_pixel(fbo, x, y , 0xff, 0x00, 0x00);
    }
    for (unsigned int y = (fbo->vinfo.yres / 2); y < fbo->vinfo.yres; y++) {
      put_pixel(fbo, x, y , 0x00, 0x00, 0xff);
    }
  }
  sleep(5);
  FBO_deinit(fbo);

  // cleanup
  return 0;
}
// vim: et:ts=2:sw=2
