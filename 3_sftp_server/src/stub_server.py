import logging
import paramiko

logging.basicConfig(level=logging.DEBUG)

class StubServer(paramiko.ServerInterface):

    def check_channel_subsystem_request(self, channel, name):
        print(f'\n====== Channel ===== {channel}')
        print(f'++++ subsystem name : {name}\n\n')

        return super().check_channel_subsystem_request(channel, name)
    
    def check_channel_request(self, kind, chanid: int):
        return paramiko.OPEN_SUCCEEDED

    def check_auth_password(self, username, password):
        return paramiko.AUTH_SUCCESSFUL

    def check_auth_publickey(self, username, key: paramiko.PKey):
        # return paramiko.AUTH_FAILED
        return paramiko.AUTH_SUCCESSFUL
    
    def get_allowed_auths(self, username):
        return ""

    def check_channel_shell_request(self, channel):
        logging.debug(f"\ncheck_channel_shell_request | channel {channel}")
        return True

    def check_channel_env_request(self, channel, key, value):
        logging.debug(f"\ncheck_channel_env_request | channel {channel} | env {key}={value}")