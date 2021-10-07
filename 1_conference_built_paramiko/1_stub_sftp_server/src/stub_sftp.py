import os 
import stat

import paramiko
from paramiko.common import AUTH_SUCCESSFUL, OPEN_SUCCEEDED
from paramiko.sftp_attr import SFTPAttributes


class StubServer(paramiko.ServerInterface):
    def check_auth_password(self, username: str, password: str):
        # return super().check_auth_password(username, password)

        # all policies are allowed
        return AUTH_SUCCESSFUL

    def check_channel_request(self, kind, chanid):
        return OPEN_SUCCEEDED


class StubSFTPServer(paramiko.SFTPServerInterface):
    ROOT = ''
    TOKEN_FILE = 'some-random-token.txt'
    someClientAPI = 'some client api with the acccess token'
    
    def __init__(self, *args, **kwargs):
        super(StubSFTPServer, self).__init__(*args, **kwargs)
        # Token for the SFTP server
        serialzed_token = open(self.TOKEN_FILE).read()
        access_token = serialzed_token[len('oauth2:'):]

        self.api_client = self.someClientAPI(access_token)
        self.current_path = self.ROOT

    def list_folder(self, path):
        """ list files in the current directory """

        try:
            """ some api may gives the response
            with many metadatas
            not only the remote server
            """
            resp = self.api_client.metadata(self.current_path)
            print(f'Got response {resp[:40]}')

            out = []
            for content in range(1, 6):
                
                attr = SFTPAttributes()
                attr.filename = os.path.basename(f'filename-{content}')
                attr.st_mode = (stat.S_IFDIR | stat.S_IRWXU)
                """ There are 2 modes of SFTP attributes
                1. if is_dir    (stat.S_IFDIR | stat.S_IRWXU)
                2. else         (stat.S_IFREG | stat.S_IRWXU)
                """
                # attr.st_size = "100" # bytes
                out.append(attr)
        except:
            pass

        return out
