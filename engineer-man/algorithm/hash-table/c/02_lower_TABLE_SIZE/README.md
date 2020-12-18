## Demo
```bash
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/02_lower_TABLE_SIZE $ diff hashfunc.c ../01_hash_fn/hashfunc.c
6c6
< #define TABLE_SIZE 10
---
> #define TABLE_SIZE 100000
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/algorithm/hash-table/c/02_lower_TABLE_SIZE $ make
cc     hashfunc.c   -o hashfunc
rm hashfunc
#test -f hashfunc && rm hashfunc
gcc -o hashfunc hashfunc.c
./hashfunc
7
```
