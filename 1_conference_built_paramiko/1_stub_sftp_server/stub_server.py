import paramiko
from paramiko.common import AUTH_SUCCESSFUL, OPEN_SUCCEEDED


""" Generally,
The SFTP server implements the ServerInterface
"""
class StubServer(paramiko.ServerInterface):

    """ Most of the functions 
    Returns : Boolean values (e.g. AUTH_SUCCESSFUL)
    """
    
    def check_auth_password(self, username: str, password: str):
        # return super().check_auth_password(username, password)

        """ all are allowed """
        return AUTH_SUCCESSFUL

    def check_auth_publickey(self, username: str, key: paramiko.PKey):
        # return super().check_auth_publickey(username, key)

        """ all are allowed """
        return paramiko.AUTH_SUCCESSFUL

    def check_channel_request(self, kind: str, chanid: int):
        # return super().check_channel_request(kind, chanid)

        return OPEN_SUCCEEDED