# A Stub SFTP Server

## Generating a RSA Key

1. Inside the `3_sftp_server` folder: 
    - `mkdir secret`
    - `cd secret`
    - `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
        - Enter file in which to save the key (/home/usr/.ssh/id_rsa): `./example-rsa`

> Note: `3_sftp_server/main.py` The `RSA_KEY` is the location of the RSA Key


## Reset The RSA 

To reset the RSA key of port _:8022_ `known_hosts` on your computer: 
    - `ssh-keygen -R [127.0.0.1]:8022`


## Start The Server

`python3 3_sftp_server/main.py`


## Connect To The Server

- `sftp -P 8022 127.0.0.1`
- `sftp -P 8022 user@127.0.0.1`
