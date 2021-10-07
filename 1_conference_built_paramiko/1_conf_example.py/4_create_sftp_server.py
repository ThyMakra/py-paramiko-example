# from .3_create_sftp_transport import Transport 
import paramiko
from paramiko import Server
from paramiko import transport

class SFTPServer:
    server = Server()

    def _maybe_start(self):
        try: 
            transport.start_server(server=server)
        except paramiko.SSHException:
            print('SSH Negotiation failed')


