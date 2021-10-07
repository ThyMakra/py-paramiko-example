```
DEBUG:root:     >>> Starting The Server <<<

DEBUG:paramiko.transport:starting thread (server mode): ...
DEBUG:paramiko.transport:Local version/idstring: SSH-2.0-paramiko_2.7.2
DEBUG:paramiko.transport:Remote version/idstring: SSH-2.0-OpenSSH_8.2p1 ...
INFO:paramiko.transport:Connected (version 2.0, client OpenSSH_8.2p1)
DEBUG:paramiko.transport:kex 
...
DEBUG:paramiko.transport:Kex agreed: curve25519-sha256@libssh.org
DEBUG:paramiko.transport:HostKey agreed: ssh-rsa
DEBUG:paramiko.transport:Cipher agreed: ...
DEBUG:paramiko.transport:MAC agreed: ...
DEBUG:paramiko.transport:Compression agreed: none
DEBUG:paramiko.transport:kex ...
DEBUG:paramiko.transport:Switch to new keys ...
DEBUG:paramiko.transport:Auth request (type=none) service=ssh-connection, username=usr
INFO:paramiko.transport:Auth rejected (none).
DEBUG:paramiko.transport:Auth request (type=password) service=ssh-connection, username=usr
INFO:paramiko.transport:Auth granted (password).
DEBUG:paramiko.transport:[chan 0] Max packet in: 32768 bytes
DEBUG:paramiko.transport:[chan 0] Max packet out: 32768 bytes
DEBUG:paramiko.transport:Secsh channel 0 (session) opened.
env request on channel <paramiko.Channel 0 (open) window=2097152 -> <paramiko.Transport at 0x45b34490 (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>>: b'LANG'=b'C.UTF-8'

====== Channel ===== <paramiko.Channel 0 (open) window=2097152 -> <paramiko.Transport at 0x45b34490 (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>>
```