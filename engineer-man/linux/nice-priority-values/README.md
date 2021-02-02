

## Relationship btw Priority Value and Nice Value
- Generally speaking, `PR = 20 + NI`.
- Sometimes the kernel may decide otherwise.
- Cf. the command `chrt`


## More about Nice Value
- In userspace, we can modify the nice value.
- possible values of nice value are within the range of **`[-20..19]`**.
- The lower the nice value, the higher the priority (**N.B.** A priority value of, say, `2` is considered higher than one of value, say, `20`)
- **Only** a **root user** can set a **negative nice value**
  - normal user: able to set nice value btw `[0..19]`
  - root user: able to set nice value btw `[-20..19]`
    - This is probably why when we prepared the `docker` command in `container.sh`, we had that line of **`--privileged`** -- so that later on `Engineer Man` can change a process's nice value to negative.
      - Try use docker container w/o `--privileged` yourself
  - by default, processes are started with nice value `0`


## Commands
```bash
# start process w/ the default nice value (10 by default)
nice <command>

# specify a nice value (here 2)
nice -n 2 <command>

# modify a running process's nice value (here, to 2)
renice -n 2 -p <PID>

# modify massively all running process's nice value for a given user
renice -n 2 -u <user>
```

- Note the diff btw a process's nice value when it's started w/ the `nice` command and w/o
  - `10` as opposed to
  - `0`
