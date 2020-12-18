#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct entry_t {
	char *key;
	char *value;
	struct entry_t *next;
} entry_t;

typedef struct ht_t {
  // This is nothing more than an array of pointers to entry_t
	entry_t **entries;
} ht_t;

int main(int argc, char **argv) {
	size_t size_struct = sizeof(entry_t);
  printf("sizeof(entry_t) = %zu\n", sizeof(entry_t));
  printf("sizeof(entry_t) = %zu\n", size_struct);
	size_t size_pointer = sizeof(entry_t*);
  printf("sizeof(entry_t*) = %zu\n", sizeof(entry_t*));
  printf("sizeof(entry_t*) = %zu\n", size_pointer);
	printf("\n");
  printf("sizeof(ht_t) = %zu\n", sizeof(ht_t));
  printf("sizeof(ht_t*) = %zu\n", sizeof(ht_t*));
	printf("\n");

	char *key = "abcdefg...xyz";
  printf("sizeof(key) = %zu\n", sizeof(key));
  printf("sizeof(*key) = %zu\n", sizeof(*key));
  printf("strlen(key) = %zu\n", strlen(key));

	return 0;
}
