#ifndef FUNCTIONS_H
#define FUNCTIONS_H

// The above are called "header guard".
// They prevents a header file from being expanded multiple times.

// function declaration
int add(int, int);
//int add(int m, int n);

// macro declaration
#define ADD(m, n) m + n

// typedef declaration
typedef struct {
  int age;
  char *name;
} person;

#endif
