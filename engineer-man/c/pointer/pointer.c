#include <stdio.h>   /* printf */
#include <stdlib.h>  /* EXIT_SUCCESS */

void increment_me(int *num) { *num += 1; }

int main(int argc, char **argv) {
  // create a variable and a pointer pointing to it
  int number = 10;
  int *p_number = &number;
  printf("p_number = %p(%%p) = %d(%%d)\n", p_number);
  printf("&number  = %p(%%p) = %d(%%d)\n", &number);
  printf("(number) = %d and (p_number dereferenced) = %d\n", number, *p_number);

  // modify the value of the variable directly and via dereferencing
  number += 1;
  printf("(number) = %d and (p_number dereferenced) = %d\n", number, *p_number);
  *p_number += 1;
  printf("(number) = %d and (p_number dereferenced) = %d\n", number, *p_number);

  // send the pointer and the reference (i.e. the address of the variable) to the function increment_me()
  increment_me(p_number);
  printf("(number) = %d and (p_number dereferenced) = %d\n", number, *p_number);
  increment_me(&number);
  printf("(number) = %d and (p_number dereferenced) = %d\n", number, *p_number);

  return EXIT_SUCCESS;
}
