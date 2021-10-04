import paramiko


""" SFTP is FTP running on top of SSH tunnel. """

ssh = paramiko.SSHClient()

""" By default, 
the policy of paramiko would not allow any connections
"""
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())

# parameters of the
# connect()
params = {
    'host': '127.0.0.1',
    'username': 'alice',
    'password': 'secret',
}
ssh.connect(**params)

sftp = ssh.open_sftp() 
params = {
    'remote_filename': 'sample.py',
    'local_filename': 'local.py',
}
sftp.get(**params)
sftp.close()

