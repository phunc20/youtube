#!/usr/bin/env python
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
