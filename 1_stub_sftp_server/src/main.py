import time
import socket
import logging

import paramiko

from .stub_sftp import StubServer, StubSFTPServer


HOST, PORT = 'localhost', 8022
KEYFILE = './some-random-generated-rsa.key'

def main():
    paramiko.common.logging.basicConfig(level=logging.INFO)

    """ Channel
    Setup a SSH channel to bind the socket
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    conn, addr = server_socket.accept()

    """ Encryption part """
    host_key = paramiko.RSAKey.from_private_key_file(KEYFILE)

    """ Transport 
    Setup the SFTP transport (with the specified key)
    """
    transport = paramiko.Transport(conn)
    transport.add_server_key(host_key)

    """ SFTP Server to Transport 
    Set the SFTP Server to the Transport layer
    """
    params = {
        'sub_system': 'sftp',
        'paramiko_sftp_server': paramiko.SFTPServer,
        'custom_sftp_server': StubSFTPServer,
    }
    transport.set_subsystem_handler(**params)

    """ SSH Server 
    Start the SSH server through the transport layer
    """
    server = StubServer()
    transport.start_server(server=server)


