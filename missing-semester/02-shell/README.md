```bash
[phunc20@homography-x220t 02-shell]$ foo=bar
[phunc20@homography-x220t 02-shell]$ echo $foo
bar
[phunc20@homography-x220t 02-shell]$ foo=bear
[phunc20@homography-x220t 02-shell]$ echo $foo
bear
[phunc20@homography-x220t 02-shell]$ foo = bar
-bash: foo: command not found
[phunc20@homography-x220t 02-shell]$ # The previous is understood as "run the foo command with args: = and bar"
[phunc20@homography-x220t 02-shell]$ echo "Hello"
Hello
[phunc20@homography-x220t 02-shell]$ echo 'world'
world
[phunc20@homography-x220t 02-shell]$ echo "$foo"
bear
[phunc20@homography-x220t 02-shell]$ echo '$foo'
$foo
[phunc20@homography-x220t 02-shell]$ echo "${foo}"
bear
[phunc20@homography-x220t 02-shell]$ echo "$(foo)"
-bash: foo: command not found

[phunc20@homography-x220t 02-shell]$ echo "$(pwd)"
/home/phunc20/git-repos/phunc20/youtube/missing-semester/02-shell
[phunc20@homography-x220t 02-shell]$ pwd
/home/phunc20/git-repos/phunc20/youtube/missing-semester/02-shell
[phunc20@homography-x220t 02-shell]$ # A lot of things in bash will be $sth as we wil
l see.
[phunc20@homography-x220t 02-shell]$ cat ~/.useful-scripts/mkcd.sh
#!/bin/bash

#mkcd() {
#    [ "$#" -ne 1 ] && echo "Only one input arg allowed." && exit 1
#    [ -z "$1" ] && echo "Please provide one input arg." && exit 1
#    mkdir -p "$1"
#    cd "$1"
#}

## The above seems to work badly because the `exit 1` makes the shell to close itself.

mkcd() {
    if [ "$#" -ne 1 ]; then
        echo "Exactly one input arg required."
    else
        mkdir -p "$1"
        cd "$1"
    fi
}
[phunc20@homography-x220t 02-shell]$ # $0 is the name of the command/script
[phunc20@homography-x220t 02-shell]$ # $1 thru $9 will be the args
[phunc20@homography-x220t 02-shell]$ # $_ is the last arg of the prev. command
[phunc20@homography-x220t 02-shell]$ echo a b c d e f g
a b c d e f g
[phunc20@homography-x220t 02-shell]$ echo $_
g
[phunc20@homography-x220t 02-shell]$ !!
echo $_
g
[phunc20@homography-x220t 02-shell]$ # !! means repeat the prev. command
[phunc20@homography-x220t 02-shell]$ # We can even sudo !! to  repeat the command with su privilege
[phunc20@homography-x220t 02-shell]$ # exit code: $?
[phunc20@homography-x220t 02-shell]$ # if $? shows 0, it means "fine"
[phunc20@homography-x220t 02-shell]$ # like in C, non-zero exit code means "warning"
[phunc20@homography-x220t 02-shell]$ # e.g.
[phunc20@homography-x220t 02-shell]$ echo "Bonjour"
Bonjour
[phunc20@homography-x220t 02-shell]$ echo $?
0
[phunc20@homography-x220t 02-shell]$ printf "Bonjour'
> ^C
[phunc20@homography-x220t 02-shell]$ echo $?
130
[phunc20@homography-x220t 02-shell]$ printf("")
-bash: syntax error near unexpected token `""'
[phunc20@homography-x220t 02-shell]$ echo $?
2
[phunc20@homography-x220t 02-shell]$ printf("Bonjour")
-bash: syntax error near unexpected token `"Bonjour"'
[phunc20@homography-x220t 02-shell]$ echo $?
2
[phunc20@homography-x220t 02-shell]$ printf"Bonjour"
-bash: printfBonjour: command not found
[phunc20@homography-x220t 02-shell]$ echo $?
127
[phunc20@homography-x220t 02-shell]$ printf "Bonjour"
Bonjour[phunc20@homography-x220t 02-shell]$ echo $?
0
[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh
[phunc20@homography-x220t 02-shell]$ echo $?
1
[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh 2&>1
[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh &>
-bash: syntax error near unexpected token `newline'
[phunc20@homography-x220t 02-shell]$ # (?) How to show the error?
[phunc20@homography-x220t 02-shell]$ true
[phunc20@homography-x220t 02-shell]$ echo $?
0
[phunc20@homography-x220t 02-shell]$ false
[phunc20@homography-x220t 02-shell]$ echo $?
1
[phunc20@homography-x220t 02-shell]$ false || echo "Oops"
Oops
[phunc20@homography-x220t 02-shell]$ true || echo "This will not be printed"
[phunc20@homography-x220t 02-shell]$ true && echo "Fine"
Fine
[phunc20@homography-x220t 02-shell]$ false && echo "This will not be printed, either"
[phunc20@homography-x220t 02-shell]$ false ; echo "This will always be printed"
This will always be printed
[phunc20@homography-x220t 02-shell]$ true; echo "This will always be printed"
This will always be printed
[phunc20@homography-x220t 02-shell]$ false    ;          echo "This will always be pr
inted"
This will always be printed
[phunc20@homography-x220t 02-shell]$
[phunc20@homography-x220t 02-shell]$
[phunc20@homography-x220t 02-shell]$ cat <(free -h) <(echo " ") <(df -h)
total        used        free      shared  buff/cache   available
Mem:           15Gi       2.8Gi        10Gi       809Mi       2.4Gi        11Gi
Swap:          31Gi          0B        31Gi

Filesystem      Size  Used Avail Use% Mounted on
dev             7.8G     0  7.8G   0% /dev
run             7.8G  768K  7.8G   1% /run
/dev/sda3        62G   15G   44G  26% /
shm             7.8G  616M  7.2G   8% /dev/shm
cgroup_root      10M     0   10M   0% /sys/fs/cgroup
/dev/sda4       822G  355G  426G  46% /home
/dev/sda2       976M   53M  857M   6% /boot
tmpfs           1.6G  4.0K  1.6G   1% /run/user/1000
[phunc20@homography-x220t 02-shell]$ # This might come in handy because some functions expect their input not from stdin but from some file, in which case we can use <() in place of pipe.
[phunc20@homography-x220t 02-shell]$
[phunc20@homography-x220t 02-shell]$
[phunc20@homography-x220t 02-shell]$ # $$ gives PID
[phunc20@homography-x220t 02-shell]$ echo $$
3258
[phunc20@homography-x220t 02-shell]$ echo $$
3258
[phunc20@homography-x220t 02-shell]$ echo $$
3258
[phunc20@homography-x220t 02-shell]$ echo $$
3258
[phunc20@homography-x220t 02-shell]$ echo $$
3258
[phunc20@homography-x220t 02-shell]$ cat <(echo $$)
3258
[phunc20@homography-x220t 02-shell]$
[phunc20@homography-x220t 02-shell]$
[phunc20@homography-x220t 02-shell]$
[phunc20@homography-x220t 02-shell]$ ./foobar_check.sh ../*
Start program at Fri Dec  4 06:58:54 PM +07 2020
Run program ./foobar_check.sh with 2 args and with pid 6376
../02-shell contains no word "foobar"
../progress.md contains no word "foobar"
[phunc20@homography-x220t 02-shell]$ tree ../
../
├── 02-shell
│   ├── foobar_check.sh
│   └── README.md
└── progress.md

1 directory, 3 files
[phunc20@homography-x220t 02-shell]$
[phunc20@homography-x220t 02-shell]$ # wild card ? and *
[phunc20@homography-x220t 02-shell]$ touch project{1,2,3,42}
[phunc20@homography-x220t 02-shell]$ ls
foobar_check.sh  project2  project42
project1         project3  README.md
[phunc20@homography-x220t 02-shell]$ ls project?
project1  project2  project3
[phunc20@homography-x220t 02-shell]$ ls project*
project1  project2  project3  project42
[phunc20@homography-x220t 02-shell]$ mv project{1,2}
[phunc20@homography-x220t 02-shell]$ # This is equiv. to mv project1 project2
[phunc20@homography-x220t 02-shell]$ ls project*
project2  project3  project42
[phunc20@homography-x220t 02-shell]$ rm project*
[phunc20@homography-x220t 02-shell]$ ls
foobar_check.sh  README.md
~/.../youtube/missing-semester/02-shell ❯❯❯ touch proj{1,2,3}/src/test{1,2,3}.c
touch: cannot touch 'proj1/src/test1.c': No such file or directory
touch: cannot touch 'proj1/src/test2.c': No such file or directory
touch: cannot touch 'proj1/src/test3.c': No such file or directory
touch: cannot touch 'proj2/src/test1.c': No such file or directory
touch: cannot touch 'proj2/src/test2.c': No such file or directory
touch: cannot touch 'proj2/src/test3.c': No such file or directory
touch: cannot touch 'proj3/src/test1.c': No such file or directory
touch: cannot touch 'proj3/src/test2.c': No such file or directory
touch: cannot touch 'proj3/src/test3.c': No such file or directory
~/.../youtube/missing-semester/02-shell ❯❯❯ mkdir foo bar
~/.../youtube/missing-semester/02-shell ❯❯❯ ll
total 20
-rwxr-xr-x 1 phunc20 wheel  442 Dec  5 16:17 foobar_check.sh
-rw-r--r-- 1 phunc20 wheel 7843 Dec  6 10:29 README.md
drwxr-xr-x 2 phunc20 wheel 4096 Dec  6 10:30 foo
drwxr-xr-x 2 phunc20 wheel 4096 Dec  6 10:30 bar
~/.../youtube/missing-semester/02-shell ❯❯❯ touch {foo,bar}/{a..j}.txt
~/.../youtube/missing-semester/02-shell ❯❯❯ tree {foo,bar}
foo
├── a.txt
├── b.txt
├── c.txt
├── d.txt
├── e.txt
├── f.txt
├── g.txt
├── h.txt
├── i.txt
└── j.txt
bar
├── a.txt
├── b.txt
├── c.txt
├── d.txt
├── e.txt
├── f.txt
├── g.txt
├── h.txt
├── i.txt
└── j.txt

0 directories, 20 files
~/.../youtube/missing-semester/02-shell ❯❯❯ touch foo/x bar/y
~/.../youtube/missing-semester/02-shell ❯❯❯ diff <(ls foo) <(ls bar)
11c11
< x
---
> y
~/.../youtube/missing-semester/02-shell ❯❯❯ # Some Python code
~/.../youtube/missing-semester/02-shell ❯❯❯ python 02_print_args.py 10 15 20
20 15 10 ~/.../youtube/missing-semester/02-shell ❯❯❯ cat 02_print_args.py
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
~/.../youtube/missing-semester/02-shell ❯❯❯
~/.../youtube/missing-semester/02-shell ❯❯❯ chmod +x 03_shebang.py
~/.../youtube/missing-semester/02-shell ❯❯❯ ./03_shebang.py
~/.../youtube/missing-semester/02-shell ❯❯❯ ./03_shebang.py a b c ... x y z
z y x ... c b a ~/.../youtube/missing-semester/02-shell ❯❯❯ cat 03_shebang.py
#!/usr/bin/python
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
~/.../youtube/missing-semester/02-shell ❯❯❯
~/.../youtube/missing-semester/02-shell ❯❯❯ workon dsp-py3.8
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ which python
/home/phunc20/.virtualenvs/dsp-py3.8/bin/python
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ cat <(which python) 04_shebang.py
/home/phunc20/.virtualenvs/dsp-py3.8/bin/python
#!/usr/bin/python
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ cat <(echo "#!") <(which python) 04_shebang.py
#!
/home/phunc20/.virtualenvs/dsp-py3.8/bin/python
#!/usr/bin/python
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ cat <(printf "#!") <(which python) 04_shebang.py
#!/home/phunc20/.virtualenvs/dsp-py3.8/bin/python
#!/usr/bin/python
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ cat <(printf "#!") <(which python) 03_shebang.py
#!/home/phunc20/.virtualenvs/dsp-py3.8/bin/python
#!/usr/bin/python
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ cat <(printf "#!") <(which python) 03_shebang.py > 04_shebang.py
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ cat 04_shebang.py
#!/home/phunc20/.virtualenvs/dsp-py3.8/bin/python
#!/usr/bin/python
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ ll 04_shebang.py
-rwxr-xr-x 1 phunc20 wheel 196 Dec  6 10:43 04_shebang.py
(dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ ./04_shebang.py 10 15 20 25
25 20 15 10 (dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯
25 20 15 10 (dsp-py3.8) ~/.../youtube/missing-semester/02-shell ❯❯❯ deactivate
~/.../youtube/missing-semester/02-shell ❯❯❯ cp 03_shebang.py 05_shebang.py
~/.../youtube/missing-semester/02-shell ❯❯❯ vim 05_shebang.py
~/.../youtube/missing-semester/02-shell ❯❯❯ head -1 05_shebang.py
#!/usr/bin/env python
~/.../youtube/missing-semester/02-shell ❯❯❯ ./05_shebang.py a b c ... x y z
z y x ... c b a ~/.../youtube/missing-semester/02-shell ❯❯❯ cp 05_shebang.py 06_shebang.py
~/.../youtube/missing-semester/02-shell ❯❯❯ vim 06_shebang.py
~/.../youtube/missing-semester/02-shell ❯❯❯ head -1 05_shebang.py
#!/usr/bin/env python2
~/.../youtube/missing-semester/02-shell ❯❯❯ ./06_shebang.py a b c ... x y z
  File "./06_shebang.py", line 5
      print(arg, end=' ')
                        ^
SyntaxError: invalid syntax
~/.../youtube/missing-semester/02-shell ❯❯❯ vim 06_shebang.py
~/.../youtube/missing-semester/02-shell ❯❯❯ ./06_shebang.py a b c ... x y z
z
y
x
...
c
b
a
~/.../youtube/missing-semester/02-shell ❯❯❯ cat 06_shebang.py
#!/usr/bin/env python2
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    #print(arg, end=' ')
    print arg
~/.../youtube/missing-semester/02-shell ❯❯❯
importlib.metadata.PackageNotFoundError: tldr
~/.../youtube/missing-semester/02-shell ❯❯❯ pacman -S tldr
~/.../youtube/missing-semester/02-shell ❯❯❯ tldr tar
Traceback (most recent call last):
  File "/usr/bin/tldr", line 33, in <module>
    sys.exit(load_entry_point('tldr==1.1.0', 'console_scripts', 'tldr')())
  File "/usr/bin/tldr", line 22, in importlib_load_entry_point
    for entry_point in distribution(dist_name).entry_points
  File "/usr/lib/python3.8/importlib/metadata.py", line 504, in distribution
    return Distribution.from_name(distribution_name)
  File "/usr/lib/python3.8/importlib/metadata.py", line 177, in from_name
    raise PackageNotFoundError(name)
importlib.metadata.PackageNotFoundError: tldr
~/.../youtube/missing-semester/02-shell ❯❯❯
~/.../youtube/missing-semester/02-shell ❯❯❯ locate resolution
locate: can not stat () `/var/lib/mlocate/mlocate.db': No such file or directory
~/.../youtube/missing-semester/02-shell ❯❯❯ updatedb
updatedb: can not open a temporary file for `/var/lib/mlocate/mlocate.db'
~/.../youtube/missing-semester/02-shell ❯❯❯
~/.../youtube/missing-semester/02-shell ❯❯❯ grep -R foo .
./README.md:[phunc20@homography-x220t 02-shell]$ foo=bar
./README.md:[phunc20@homography-x220t 02-shell]$ echo $foo
./README.md:[phunc20@homography-x220t 02-shell]$ foo=bear
./README.md:[phunc20@homography-x220t 02-shell]$ echo $foo
./README.md:[phunc20@homography-x220t 02-shell]$ foo = bar
./README.md:-bash: foo: command not found
./README.md:[phunc20@homography-x220t 02-shell]$ # The previous is understood as "run the foo command with args: = and bar"
./README.md:[phunc20@homography-x220t 02-shell]$ echo "$foo"
./README.md:[phunc20@homography-x220t 02-shell]$ echo '$foo'
./README.md:$foo
./README.md:[phunc20@homography-x220t 02-shell]$ echo "${foo}"
./README.md:[phunc20@homography-x220t 02-shell]$ echo "$(foo)"
./README.md:-bash: foo: command not found
./README.md:[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh
./README.md:[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh 2&>1
./README.md:[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh &>
./README.md:[phunc20@homography-x220t 02-shell]$ ./foobar_check.sh ../*
./README.md:Run program ./foobar_check.sh with 2 args and with pid 6376
./README.md:../02-shell contains no word "foobar"
./README.md:../progress.md contains no word "foobar"
./README.md:│   ├── foobar_check.sh
./README.md:foobar_check.sh  project2  project42
./README.md:foobar_check.sh  README.md
./README.md:~/.../youtube/missing-semester/02-shell ❯❯❯ mkdir foo bar
./README.md:-rwxr-xr-x 1 phunc20 wheel  442 Dec  5 16:17 foobar_check.sh
./README.md:drwxr-xr-x 2 phunc20 wheel 4096 Dec  6 10:30 foo
./README.md:~/.../youtube/missing-semester/02-shell ❯❯❯ touch {foo,bar}/{a..j}.txt
./README.md:~/.../youtube/missing-semester/02-shell ❯❯❯ tree {foo,bar}
./README.md:foo
./README.md:~/.../youtube/missing-semester/02-shell ❯❯❯ touch foo/x bar/y
./README.md:~/.../youtube/missing-semester/02-shell ❯❯❯ diff <(ls foo) <(ls bar)
./01_foobar_check.sh:  grep foobar "$file" > /dev/null 2> /dev/null
./01_foobar_check.sh:  # the word "foobar", which can be reflected by the
./01_foobar_check.sh:    echo "$file contains no word \"foobar\""
~/.../youtube/missing-semester/02-shell ❯❯❯ grep -Rn foo .
./README.md:2:[phunc20@homography-x220t 02-shell]$ foo=bar
./README.md:3:[phunc20@homography-x220t 02-shell]$ echo $foo
./README.md:5:[phunc20@homography-x220t 02-shell]$ foo=bear
./README.md:6:[phunc20@homography-x220t 02-shell]$ echo $foo
./README.md:8:[phunc20@homography-x220t 02-shell]$ foo = bar
./README.md:9:-bash: foo: command not found
./README.md:10:[phunc20@homography-x220t 02-shell]$ # The previous is understood as "run the foo command with args: = and bar"
./README.md:15:[phunc20@homography-x220t 02-shell]$ echo "$foo"
./README.md:17:[phunc20@homography-x220t 02-shell]$ echo '$foo'
./README.md:18:$foo
./README.md:19:[phunc20@homography-x220t 02-shell]$ echo "${foo}"
./README.md:21:[phunc20@homography-x220t 02-shell]$ echo "$(foo)"
./README.md:22:-bash: foo: command not found
./README.md:89:[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh
./README.md:92:[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh 2&>1
./README.md:93:[phunc20@homography-x220t 02-shell]$ grep foobar ~/.useful-scripts/mkcd.sh &>
./README.md:150:[phunc20@homography-x220t 02-shell]$ ./foobar_check.sh ../*
./README.md:152:Run program ./foobar_check.sh with 2 args and with pid 6376
./README.md:153:../02-shell contains no word "foobar"
./README.md:154:../progress.md contains no word "foobar"
./README.md:158:│   ├── foobar_check.sh
./README.md:167:foobar_check.sh  project2  project42
./README.md:179:foobar_check.sh  README.md
./README.md:190:~/.../youtube/missing-semester/02-shell ❯❯❯ mkdir foo bar
./README.md:193:-rwxr-xr-x 1 phunc20 wheel  442 Dec  5 16:17 foobar_check.sh
./README.md:195:drwxr-xr-x 2 phunc20 wheel 4096 Dec  6 10:30 foo
./README.md:197:~/.../youtube/missing-semester/02-shell ❯❯❯ touch {foo,bar}/{a..j}.txt
./README.md:198:~/.../youtube/missing-semester/02-shell ❯❯❯ tree {foo,bar}
./README.md:199:foo
./README.md:223:~/.../youtube/missing-semester/02-shell ❯❯❯ touch foo/x bar/y
./README.md:224:~/.../youtube/missing-semester/02-shell ❯❯❯ diff <(ls foo) <(ls bar)
./01_foobar_check.sh:7:  grep foobar "$file" > /dev/null 2> /dev/null
./01_foobar_check.sh:10:  # the word "foobar", which can be reflected by the
./01_foobar_check.sh:13:    echo "$file contains no word \"foobar\""
~/.../youtube/missing-semester/02-shell ❯❯❯
```


## `dollar sth`
- `$@` means **all the args**, e.g.
  ```bash
  for file in "$@"; do
    # ...
  done
  ```
## special
- `Ctrl R`: search command

## Further reading
- `man test`



