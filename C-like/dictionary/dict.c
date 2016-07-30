#include <string.h>
#include <stdio.h>

#define LINE_BUFF_LEN 256
#define RSLT_BUFF_LEN 256
#define KEY_BUFF_LEN  64

void trimbegin(char *src) {
  int offset = 0;
  for(int i=0; i < strlen(src)-1; i++) {
    if(src[i] < 127 && src[i] > 32) {
      break;
    } else {
      offset++;
    }
  }
  int i=0;
  for(; i < (strlen(src)-1)-offset; i++) {
    src[i] = src[i+offset];
  }
  src[i] = '\0';
}

void trimend(char *src) {
  for(int i=strlen(src)-1; i >= 0; i--) {
    if(src[i] < 127 && src[i] > 32) {
      return;
    } else {
      src[i] = 0;
    }
  }
}

void lookup(FILE *dict, char *query, char *response) {
  char buffer[LINE_BUFF_LEN];
  while(fgets(buffer, LINE_BUFF_LEN, dict)) {
    char *cln_loc = strchr(buffer, ':');
    int len_key = (cln_loc - buffer)/sizeof(char);
    char key[KEY_BUFF_LEN];
    strncpy(key, buffer, len_key-1);
    key[len_key-1] = '\0';
    trimend(key);
    if(!strcmp(key, query)) {
      strcpy(response, (cln_loc+1));
      trimbegin(response);
      trimend(response);
      return;
    }
  }
  *response = '\0';
}

int main(int argc, char *argv[]) {
  if(argc >= 3) {
    FILE *dict = fopen(argv[1], "r");
    char result[RSLT_BUFF_LEN];
    lookup(dict, argv[2], result);
    puts(result);
  } else {
    printf("Usage: %s [dict file] [key]\n", argv[0]);
    return -1;
  }
  return 0;
}
