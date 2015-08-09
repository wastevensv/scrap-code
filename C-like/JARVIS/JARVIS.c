#include <stdio.h>
#include <string.h>
#include "JARVIS.h"

void execstring(char com[])
{
  char response[256];
  bzero(response,sizeof(&response));

  char word[256];
  bzero(word,sizeof(&word));

  char tmp[256];

  int i=0;
  int wc=0;

  char c;
  do {
    c = com[i];
    switch(c) {
      case ' ':
      case '\0':
        sprintf(tmp, "%d: %s\n", wc, word);
        strcat(response, tmp);
        wc++;
        bzero(word,sizeof(&word));
        break;
      default:
        strncat(word, &c, 1);
        break;
    }
  i++;
  } while(c != '\0');

  printf(response);
}
