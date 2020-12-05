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
[phunc20@homography-x220t 02-shell]$

```


## `dollar sth`
- `$@` means **all the args**, e.g.
  ```bash
  for file in "$@"; do
    # ...
  done
  ```


## Further reading
- `man test`



