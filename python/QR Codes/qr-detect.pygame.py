#!/usr/bin/python
from sys import argv
import zbar
import Image
import time
##
import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
size = (640, 480)
##
d = pygame.display.set_mode(size, pygame.FULLSCREEN)
s = pygame.surface.Surface(size, 0, d)
c = pygame.camera.list_cameras()
##
cam = pygame.camera.Camera(c[0], size)
cam.start()


#if len(argv) < 2: exit(1)

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')
going = True
while going:
    # obtain image data
    waiting = True
    while waiting:
        if cam.query_image():
            time.sleep(0.5)
            rgb = cam.get_image(s)
            rgb = pygame.image.tostring(rgb, 'RGB', False)
            rgb = Image.fromstring('RGB',size,rgb)
            waiting = False
    ##rgb = Image.open(argv[1]).convert('RGB')
    gray = rgb.convert('L')
    width, height = gray.size
    raw = gray.tostring()

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    # extract results
    for symbol in image:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
        print symbol.location[0], symbol.location[2]
        
        #Open overlay
        overlay = Image.open(symbol.data).convert('RGBA')

        #Determine size of QR code and resize image
        dims = (abs(symbol.location[0][0]-symbol.location[2][0]),abs(symbol.location[0][1]-symbol.location[2][1]))
        overlay = overlay.resize(dims)

        #Messy way to determine orientation of QR code (please suggest better one)
        if symbol.location[0][0] < symbol.location[2][0]:
            if symbol.location[0][1] < symbol.location[2][1]:
                region = (symbol.location[0][0],symbol.location[0][1],symbol.location[2][0],symbol.location[2][1])
            else:
                region = (symbol.location[0][0],symbol.location[2][1],symbol.location[2][0],symbol.location[0][1])
        else:
            if symbol.location[0][1] < symbol.location[2][1]:
                region = (symbol.location[2][0],symbol.location[0][1],symbol.location[0][0],symbol.location[2][1])
            else:
                region = (symbol.location[2][0],symbol.location[2][1],symbol.location[0][0],symbol.location[0][1])

        #Finish it
        print dims, region
        rgb.paste(overlay, region, overlay)
    #rgb.save("final.png")
    rgb = rgb.tostring()
    rgb = pygame.image.fromstring(rgb, size, 'RGB', False)
    d.blit(rgb,(0,0))
    pygame.display.flip() # update the display

    # clean up
    del(image)
