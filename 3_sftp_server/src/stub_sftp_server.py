import os, stat
import paramiko as pmk


class StubSFTPServer(pmk.SFTPServerInterface):

    def __init__(self, *args, **kwargs):

        super(StubSFTPServer, self).__init__(*args, **kwargs)

    def _realpath(self, path):
        return ("/mnt")

    def make_folder(self, filename: str):
        attr = pmk.SFTPAttributes()
        attr.filename = filename
        attr.st_mode = (stat.S_IFDIR | stat.S_IRWXU)
        return attr

    def list_folder(self, path):
        folders = []
            
        for num in range(1, 6):
            folder = self.make_folder(f"folder-{num}")
            folders.append(folder)
        try:
            return folders
        except OSError as e:
            return pmk.SFTPServer.convert_errno(e.errno)

    def stat(self, path):
        try:
            return pmk.SFTPAttributes.from_stat(os.stat("/mnt"))
        except OSError as e:
            return pmk.SFTPServer.convert_errno(e.errno) 

    def lstat(self, path):
        try:
            return pmk.SFTPAttributes.from_stat(os.stat("/mnt"))
        except OSError as e:
            return pmk.SFTPServer.convert_errno(e.errno)

    def remove(self, path):
        return pmk.SFTP_OK

    def rename(self, oldpath, newpath):
        return pmk.SFTP_OK

    def mkdir(self, path, attr):
        try:
            os.mkdir(path, mode=0o777)
        except Exception as e:
            print(e)
        return pmk.SFTP_OK

    def rmdir(self, path):
        return pmk.SFTP_OK

    def chattr(self, path, attr):
        return pmk.SFTP_OK

    def symlink(self, target_path, path):
        print("="*6)
        print("Command: symlink")
        print("="*6)
        return pmk.SFTP_OK

    def readlink(self, path):
        print("="*7)
        print("Command: readlink")
        print("="*7)
        return "/mnt"