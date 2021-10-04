# README

## Read Code In-order

1. `stub_server.py` : How it looks | what a SSH server should look like
2. `sftp_sub_system.py` : How it looks | how a sftp server should look like
3. `src` : a sample SFTP server over SSH Transport layer
    1. `main.py` : bind the channel, start the SFTP over the SSH Transport
    2. `stub_sftp.py` : customizing the SFTP server with the `list_folder`