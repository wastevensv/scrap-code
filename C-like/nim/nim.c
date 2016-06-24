#include <stdio.h>

#define START_COINS   12
#define MAX_PICK 3

int main(int argc, char *argv[]) {
  int coins = START_COINS;
  while(coins != 0) {
    for(int c=0; c < coins; c++) {
      fputs("#", stdout);
      fflush(stdout);
    }
    fputs("\n", stdout);
    char user = getchar() - '0';
    getchar();
    if(user < 1 || user > MAX_PICK) {
      printf("Invalid Choice %d.\n", user);
      return -1;
    } else {
      printf("You took %d coins.\n", user);
      coins -= user;
    }
    for(int c=0; c < coins; c++) {
      fputs("#", stdout);
      fflush(stdout);
    }
    fputs("\n", stdout);
    char nim = 4 - user;
    printf("Nim took %d coins.\n", nim);
    coins -= nim;
  }
  fputs("Nim wins.\n", stdout);
  return 0;
}
