#!/usr/bin/env python3

import sys
import subprocess
import socket

def cowfortune():
    forproc = subprocess.Popen(['/usr/games/fortune'], \
                               universal_newlines=True, stdout=subprocess.PIPE)
    cowproc = subprocess.Popen(['/usr/games/cowsay'], \
                               universal_newlines=True, stdin=forproc.stdout, stdout=subprocess.PIPE)

    outstr = ''
    while True:
        s = cowproc.stdout.readline()
        if not s:
            break
        outstr += s
    return outstr

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    html =  "<h1 style='color:blue'>Hello From %s!</h1>\n" % socket.gethostname()
    html += "<tt><pre>\n"
    html += cowfortune()
    html += "</pre></tt>\n"

    return [html.encode('utf8')]

if __name__ == '__main__':
    print(cowfortune())
