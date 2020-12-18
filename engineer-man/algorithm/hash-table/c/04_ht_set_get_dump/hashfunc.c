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

//typedef struct ht_t {
typedef struct ht_t {
	// This is nothing more than an array of pointers to entry_t
	entry_t **entries;
} ht_t;

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

ht_t *ht_create(void) {
	// allocate table
	ht_t *hashtable = malloc(sizeof(ht_t) * 1);
	// allocate its entries
	hashtable->entries = malloc(sizeof(entry_t*) * TABLE_SIZE);
	//hashtable->entries = malloc(sizeof(entry_t) * TABLE_SIZE);

	// set each entry to NULL
	int i = 0;
	for (; i < TABLE_SIZE; ++i)
	  hashtable->entries[i] = NULL;

	return hashtable;
}

entry_t *ht_pair(const char *key, const char *value) {
	// cater to the construction of a entry_t: key, value, next
	entry_t *entry = malloc(sizeof(entry));
	entry->key = malloc(sizeof(key) + 1);
	entry->value = malloc(sizeof(value) + 1);
	strcpy(entry->key, key);
	strcpy(entry->value, value);
	entry->next = NULL;
	return entry;
}

void ht_set(ht_t *hashtable, const char *key, const char *value) {
	unsigned int slot = hash(key);
	entry_t *entry = hashtable->entries[slot];
  if (entry == NULL) {
		entry = ht_pair(key, value);
		// (?) why the above line is incorrect?
		//hashtable->entries[slot] = ht_pair(key, value);
		return;
	}

	entry_t *prev;
	// Walk thru the corresponding linked list
	while (entry != NULL) {
		if (strcmp(entry->key, key) == 0) {
			// match found, replace value
			free(entry->value);
			entry->value = malloc(strlen(value) + 1);  // 1 for '\0'
			strcpy(entry->value, value);
			return;
		}
		prev = entry;
		entry = entry->next;
		//entry = prev->next;
	}
	entry = ht_pair(key, value);
	//prev->next = ht_pair(key, value);
}

char *ht_get(ht_t *hashtable, const char *key) {
	// if key found, return the corresponding value
	unsigned int slot = hash(key);
	entry_t *entry = hashtable->entries[slot];
  if (entry == NULL) {
		return NULL;
	}

	// Walk thru the corresponding linked list
	while (entry != NULL) {
		if (strcmp(entry->key, key) == 0) {
			// match found, return value
			return entry->value;
		}
		entry = entry->next;
	}
	// no match found
	return NULL;
}

void my_ht_dump(ht_t *hashtable) {
	// for each slot we print one line
	for (int i=0; i < TABLE_SIZE; ++i) {
		entry_t *entry = hashtable->entries[i];
		if (entry != NULL)
			printf("slot[%4d]:", i);
		while (entry != NULL) {
			printf(" %s=%s", entry->key, entry->value);
			entry = entry->next;
		}
		printf("\n");
	}
}

void ht_dump(ht_t *hashtable) {
	// for each slot we print one line
	//entry_t *entry;
	for (int i=0; i < TABLE_SIZE; ++i) {
		//printf("i = %d", i);
		entry_t *entry = hashtable->entries[i];
		//entry = hashtable->entries[i];
		if (entry == NULL) {
		  //printf("NULL");
			continue;
		}

		printf("slot[%4d]:", i);
		for (;;) {
			printf(" %s=%s", entry->key, entry->value);
			if (entry->next == NULL)
				break;

			entry = entry->next;
		}
		printf("\n");
	}
}

int main(int argc, char **argv) {
	ht_t *ht = ht_create();

	ht_set(ht, "str1", "If");
	ht_set(ht, "str2", "you");
	ht_set(ht, "str3", "can't");
	ht_set(ht, "str4", "convince");
	ht_set(ht, "str5", "them");
	ht_set(ht, "str6", ",");
	ht_set(ht, "str7", "confuse");
	ht_set(ht, "str8", "them");
	ht_set(ht, "str9", ".");

	ht_dump(ht);

	return 0;
}


