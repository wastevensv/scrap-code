#include <stdio.h>
#include <string.h>
#include "parse.h"

#define BUFF_LEN 4096

int main (int argc, char *argv[])
{
  char c='\0'; // 'c' - Character being read
  char command[BUFF_LEN]; // 'command' - Current line
  bzero(command, sizeof(command)); // Ensure command string is zeroed.
        
  fputs("WSH> ",stdout); // Print initial prompt.

  // --- Begin main loop ---
  while(c != EOF) {
    // --- Begin read loop ---
    for(int i=0; i < BUFF_LEN; i++) {
      c = getchar(); // Read character from input.
      if(c == '\n' || c == EOF) break; // If EOL or EOF, break out of read loop.
      if(c < 0x20 || c > 0x7E) continue; // Ignore non printable characters (not between ' ' and '~')
      strncat(command, &c, 1); // Append character to command.
    }
    // ---  End read loop  ---
    if(c == EOF) break; // If EOF, exit.

    command[BUFF_LEN] = '\0'; // Ensure that the string is null terminated.

    parsestring(command); // Pass line parser function.
    bzero(command, sizeof(command)); // Reset command string.
    fputs("WSH> ",stdout); // Reprint prompt.
  }
  // ---  End main loop  ---
  puts(""); // Print ending newline.
  return 0;
}

