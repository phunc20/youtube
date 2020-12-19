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

## `my_ht_dump` and `ht_dump`
These two functions both run fine.

## Diff `TABLE_SIZE`
- `#define TABLE_SIZE 100000`
  ```bash
  ~/.../hash-table/c/09_continue_experiment ❯❯❯ make
  rm hashfunc
  #test -f hashfunc && rm hashfunc
  gcc -o hashfunc hashfunc.c
  ./hashfunc
  slot[88166]: str1=If
  slot[88167]: str2=you
  slot[88168]: str3=can't
  slot[88169]: str4=convince
  slot[88170]: str5=them
  slot[88171]: str6=,
  slot[88172]: str7=confuse
  slot[88173]: str8=them
  slot[88174]: str9=.
  ```
- `#define TABLE_SIZE 1`: **Last bug!!!** -- To be solved in `../10_last_bug/`
  ```bash
  ~/.../hash-table/c/09_continue_experiment ❯❯❯ make
  cc     hashfunc.c   -o hashfunc
  rm hashfunc
  #test -f hashfunc && rm hashfunc
  gcc -o hashfunc hashfunc.c
  ./hashfunc
  slot[   0]: str1=If
  ```
- `#define TABLE_SIZE 3`
  ```bash
  ~/.../hash-table/c/09_continue_experiment ❯❯❯ make
  cc     hashfunc.c   -o hashfunc
  rm hashfunc
  #test -f hashfunc && rm hashfunc
  gcc -o hashfunc hashfunc.c
  ./hashfunc
  slot[   0]: str3=can't
  slot[   1]: str1=If
  slot[   2]: str2=you
  ```
- `#define TABLE_SIZE 9`
  ```bash
  ~/.../hash-table/c/09_continue_experiment ❯❯❯ make
  cc     hashfunc.c   -o hashfunc
  rm hashfunc
  #test -f hashfunc && rm hashfunc
  gcc -o hashfunc hashfunc.c
  ./hashfunc
  slot[   0]: str3=can't
  slot[   1]: str4=convince
  slot[   2]: str5=them
  slot[   3]: str6=,
  slot[   4]: str7=confuse
  slot[   5]: str8=them
  slot[   6]: str9=.
  slot[   7]: str1=If
  slot[   8]: str2=you
  ```

## Q & A
**(?1)** Line 52 of `hashfunc.c`: `entry_t *entry = malloc(sizeof(entry_t));` could have been replaced by **`entry_t *entry = malloc(sizeof(entry_t*));`**, right?
**(R1)** My own opinion towards this question is that not only can we replace `entry_t` by `entry_t*`, but, by doing so, the memory allocation would be more precise, i.e. less of a waste.
