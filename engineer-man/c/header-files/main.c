#include <stdio.h>

#include "functions.h"

int main(void) {
  // function from header file
  printf("%d\n", add(2, 6));
  // macro from header file
  printf("%f\n", ADD(3.14159, 2.71828));
  // typedef from header file
  person engineer_man;
  engineer_man.age = 32;
  engineer_man.name = "EngineerMan";
  printf("%s's age is %d years old.\n", engineer_man.name, engineer_man.age);
}
