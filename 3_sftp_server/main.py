import logging, socket, time, sys, os
import paramiko

from src.stub_server import StubServer
from src.stub_sftp_server import StubSFTPServer


HOST, PORT = '127.0.0.1', 8022
RSA_KEY = './3_sftp_server/secret/example-rsa'
BACKLOG = 2
"""
it specifies the number of unaccepted connections that the system will allow before 
refusing new connections. If not specified, a default reasonable value is chosen.
"""

def main():

    logging.basicConfig(level=logging.DEBUG)

    logging.debug(f"\t>>> Starting The Server <<<\n")

    
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        server_socket.bind((HOST, PORT))
        server_socket.listen(BACKLOG)
    except:
        sys.exit(1)

    host_key = paramiko.RSAKey.from_private_key_file(RSA_KEY)

    # while True:
    conn, addr = server_socket.accept()

    transport = paramiko.Transport(conn)
    transport.add_server_key(host_key)
    transport.set_subsystem_handler(
        'sftp', paramiko.SFTPServer, StubSFTPServer
    )

    server = StubServer()
    transport.start_server(server=server)

    channel = transport.accept()
    while transport.is_active():
        time.sleep(5)

if __name__ == "__main__":
    main()