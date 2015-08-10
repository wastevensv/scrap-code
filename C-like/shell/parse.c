#include <stdio.h>
#include <string.h>

#define BUFF_LEN 4096
#define MAX_CHARS 64
#define MAX_WORDS 64

void parsestring(char com[])
{
  char words[MAX_WORDS][MAX_CHARS]; // 'words' - Array of words in line.
  bzero(words,sizeof(words)); // Ensure words is zeroed.

  int cc=0; // 'cc' - index of character being read.
  int wc=0; // 'wc' - number of words read.

  char c; // 'c' - character being read.
  // --- Begin Parse Loop ---
  do {
    // --- Begin Read Loop ---
    for(int i=0; i < MAX_CHARS; i++) {
      c = com[cc++]; // Read next character from line.
      if(c == ' ' || c == '\0') break; // If space or EOL, break out of read loop.
      strncat(words[wc], &c, 1);
    }
    // --- End Read Loop ---

    printf("%d: %s\n", wc, words[wc]); // Print word and word number
    wc++; // Increment word count.
  } while(c != '\0' && wc < MAX_WORDS); // Loop until EOL or too many words.
  // --- End Parse Loop ---

  // TODO: Add code to do something with 'words' array.
}

