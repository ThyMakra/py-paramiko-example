""" Channel | Regular UNIX Socket """


import socket
import sys


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

    sock.bind(('127.0.0.1', 22))
    socket.listen(100)

    print('listen for connection ...')
    
    channel, addr = sock.accept()

except:
    print('listening / binding / accepting failed')
    sys.exit(1)

