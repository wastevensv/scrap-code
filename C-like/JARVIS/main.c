#include <stdio.h>
#include <string.h>
#include "JARVIS.h"

int main (int argc, char *argv[])
{
  char c='\0';
  char command[256];
  bzero(command, sizeof(&command));
        
  char *response;

  printf("JARVIS> ");

  while(c != EOF) {
    c = getchar();
    switch(c) {
      case '\n':
        printf("In: %s\n",command);
        execstring(command);
        bzero(command, sizeof(&command));
        printf("JARVIS> ");
        break;
      default:
        strncat(command, &c, 1);
        break;
    }
  }

  return 0;
}

