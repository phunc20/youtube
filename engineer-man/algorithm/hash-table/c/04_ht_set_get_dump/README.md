## Demo
```bash
$ cat hashfunc.c
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 100000

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
	printf("%d\n", hash("anh"));
	return 0;
}


$ cat Makefile
all: clean compile run

clean: hashfunc
	rm hashfunc
	#test -f hashfunc && rm hashfunc

compile: hashfunc.c
	gcc -o hashfunc hashfunc.c

run:
	./hashfunc
$ make
cc     hashfunc.c   -o hashfunc
rm hashfunc
#test -f hashfunc && rm hashfunc
gcc -o hashfunc hashfunc.c
./hashfunc
36967
$ ls
Makefile  hashfunc  hashfunc.c
$ ./hashfunc
36967
$ ./hashfunc
36967
$ ./hashfunc
36967
```

## Replace the `"anh"` by `"em"`
```bash
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/01_hash_fn $ cp hashfunc.c backup.c; sed 's/"a
nh"/"em"/' hashfunc.c --in-place
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/01_hash_fn $ cat hashfunc.c
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 100000

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
        printf("%d\n", hash("em"));
        return 0;
}


leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/01_hash_fn $ make
cc     hashfunc.c   -o hashfunc
rm hashfunc
#test -f hashfunc && rm hashfunc
gcc -o hashfunc hashfunc.c
./hashfunc
3846
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/01_hash_fn $ ./hashfunc
3846
```

**(?)** Why there is an asterisk at the end of **`sizeof(entry_t*)`** whereas there isn't one for **`sizeof(ht_t)`**?
