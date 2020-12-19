## Opening words
1. What is a header file for?
  - for declaring functions and macros, specifically those that should be shared btw source files
2. Are header files required?
  - No. But you'd be silly not to use them.
  - However, if you're incined not to, you can copy and paste all of your function declarations and macros into every source file.
  - In fact, this is what C compilers do during preprocessing.


## What happens if we include a header file not already there?
```bash
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/c/header-files $ vim main.c
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/c/header-files $ gcc main.c
main.c:2:10: fatal error: functions.h: No such file or directory
    2 | #include "functions.h"
      |          ^~~~~~~~~~~~~
compilation terminated.
leif@CenterLap-x1carbon ~/git-repos/phunc20/youtube/engineer-man/c/header-files $ ls
README.md  main.c
```

