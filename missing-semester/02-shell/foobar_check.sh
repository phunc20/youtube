#!/bin/bash

echo "Start program at $(date)"
echo "Run program $0 with $# args and with pid $$"

for file in "$@"; do
  grep foobar "$file" > /dev/null 2> /dev/null
  # We redirect the STDOUT and STDERR to a null register
  # because we only care whether or not the file contains
  # the word "foobar", which can be reflected by the
  # exit code alone.
  if [[ "$?" -ne 0 ]]; then
    echo "$file contains no word \"foobar\""
  fi
done





