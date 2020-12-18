## `struct`

The two ways are both ok:
01. 1st way
  ```bash
  typedef struct {
  	entry_t **entries;
  } ht_t;
  ```
02. 2nd way
  ```bash
  typedef struct ht_t {
  	entry_t **entries;
  } ht_t;
  ```

## No need to `* 1` for inside `malloc()`
That is to say, the following two ways are both fine:
01. 1st way
  ```bash
  ht_t *hashtable = malloc(sizeof(ht_t));
  ```
02. 2nd way
  ```bash
  ht_t *hashtable = malloc(sizeof(ht_t) * 1);
  ```

## `sizeof()`
It seems that
- pointers have size `8`
- `entry_t` contains three pointers in its structure, so `24` is reasonable
- `key` is a pointer, so `8` is reasonable
- `*key` is `key[0]`, a `char`, so size `1` seems reasonable

```bash
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/09_continue_experiment $ gcc sizeof.c
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/09_continue_experiment $ ./a.out
sizeof(entry_t) = 24
sizeof(entry_t) = 24
sizeof(entry_t*) = 8
sizeof(entry_t*) = 8

sizeof(ht_t) = 8
sizeof(ht_t*) = 8
sizeof(key) = 8
sizeof(*key) = 1
strlen(key) = 13
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/09_continue_experiment $ cat sizeof.c
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
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/09_continue_experiment $
```

**(?)** Line 52 of `hashfunc.c`: `entry_t *entry = malloc(sizeof(entry_t));` could have been replaced by **`entry_t *entry = malloc(sizeof(entry_t*));`**, right?
