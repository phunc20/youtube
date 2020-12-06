#!/home/phunc20/.virtualenvs/dsp-py3.8/bin/python
#!/usr/bin/python
# I found the above path using the command `which python`
import sys
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')
