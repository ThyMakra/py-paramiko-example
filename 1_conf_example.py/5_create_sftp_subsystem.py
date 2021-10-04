import paramiko


transport = '.3....'
MyFancySFTPBridge = ''
sftp_bridge_opts = ''

server = '.4....'

class SubSystem:

    def _start(self):
        try: 
            transport.set_subsystem_handler(
                'sftp', MyFancySFTPBridge, *sftp_bridge_opts
            )
            transport.start_server(server=server)
        except paramiko.SSHException:
            print('SSH negotiation failed...')