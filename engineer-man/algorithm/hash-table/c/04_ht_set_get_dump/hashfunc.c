#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 100000

typedef struct entry_t {
	char *key;
	char *value;
	struct entry_t *next;
} entry_t;

typedef struct {
	// This is nothing more than an array of pointers to entry_t
	entry_t **entries;
} ht_t;

ht_t *ht_create(void) {
	// allocate table
	ht_t *hashtable = malloc(sizeof(ht_t) * 1);
	// allocate its entries
	hashtable->entries = malloc(sizeof(entry_t*) * TABLE_SIZE);

	// set each entry to NULL
	int i = 0;
	for (; i < TABLE_SIZE; ++i)
	  hashtable->entries[i] = NULL;

	return hashtable;
}

unsigned int hash(const char *key) {
	unsigned long int value = 0;
	unsigned int i = 0;
	unsigned int key_len = strlen(key);

	// do several rounds of computation
	for (; i < key_len; ++i) {
		value = value*37 + key[i];
	}

	value = value % TABLE_SIZE;
	return value;
}


int main(int argc, char **argv) {
	ht_t *ht = ht_create();
	return 0;
}

























