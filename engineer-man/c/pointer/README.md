```bash
~/.../engineer-man/c/pointer ❯❯❯ gcc pointer.c
pointer.c: In function ‘main’:
pointer.c:10:33: warning: format ‘%d’ expects a matching ‘int’ argument [-Wformat=]
   10 |   printf("p_number = %p(%%p) = %d(%%d)\n", p_number);
      |                                ~^
      |                                 |
      |                                 int
pointer.c:11:33: warning: format ‘%d’ expects a matching ‘int’ argument [-Wformat=]
   11 |   printf("&number  = %p(%%p) = %d(%%d)\n", &number);
      |                                ~^
      |                                 |
      |                                 int
~/.../engineer-man/c/pointer ❯❯❯ ./a.out
p_number = 0x7ffea11dd08c(%p) = -1591881304(%d)
&number  = 0x7ffea11dd08c(%p) = 0(%d)
(number) = 10 and (p_number dereferenced) = 10
(number) = 11 and (p_number dereferenced) = 11
(number) = 12 and (p_number dereferenced) = 12
(number) = 13 and (p_number dereferenced) = 13
(number) = 14 and (p_number dereferenced) = 14
~/.../engineer-man/c/pointer ❯❯❯ ./a.out
p_number = 0x7ffee35b3f7c(%p) = -480558952(%d)
&number  = 0x7ffee35b3f7c(%p) = 0(%d)
(number) = 10 and (p_number dereferenced) = 10
(number) = 11 and (p_number dereferenced) = 11
(number) = 12 and (p_number dereferenced) = 12
(number) = 13 and (p_number dereferenced) = 13
(number) = 14 and (p_number dereferenced) = 14
~/.../engineer-man/c/pointer ❯❯❯
```
