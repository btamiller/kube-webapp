#!/usr/bin/env python3

import sys
import subprocess

if __name__ == '__main__':
    catproc = subprocess.Popen(['/bin/cat', '/etc/passwd'], \
                               universal_newlines=True, stdout=subprocess.PIPE)
    srtproc = subprocess.Popen(['/bin/sort'], \
                               universal_newlines=True, stdin=catproc.stdout, stdout=subprocess.PIPE)

    while True:
        s = srtproc.stdout.readline()
        if not s:
            break
        sys.stdout.write(s)
