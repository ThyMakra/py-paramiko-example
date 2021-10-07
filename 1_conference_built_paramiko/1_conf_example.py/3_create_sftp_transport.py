import paramiko
from paramiko import channel
from paramiko import hostkeys


"""  """
class Transport:
    transport = paramiko.Transport(channel)
    transport.add_server_key(hostkeys)