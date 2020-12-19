## Recall what our bug is
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

The problem lies in the function **`ht_set`**. The pointer `prev` is inevitable.<br>
Abstractly speaking, when we have two pointers `p1` and `p2` and a function `f` which returns a point, the following C code
```c
p2 = p1;
p2 = f();
```
**does not** make `p1` contain the returned value of `f`. Instead, what we did is just keep switching the pointer `p2` from one (`p1`) to another (`f()`).
