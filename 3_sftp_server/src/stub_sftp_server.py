import os, stat, logging
import paramiko as pmk


paths = [
    ['path1.1', 'path1.2', 'path1.3', 'path1.4', 'path1.5', 'path1.6'],
    ['path2.1', 'path2.2', 'path2.3', 'path2.4', 'path2.5', 'path2.6'],
    ['path3.1', 'path3.2', 'path3.3', 'path3.4', 'path3.5', 'path3.6'],
]


class StubSFTPServer(pmk.SFTPServerInterface):

    def __init__(self, *args, **kwargs):
        self._path = '/'
        self.server = args[0]
        #
        logging.debug(f"{self.server.username} username")

        super(StubSFTPServer, self).__init__(*args, **kwargs)

    def _realpath(self, path):
        return "/tmp"

    def make_folder(self, filename: str):
        attr = pmk.SFTPAttributes()
        attr.filename = filename
        attr.st_mode = (stat.S_IFDIR | stat.S_IRWXU)
        return attr

    def list_folder(self, path):
        folders = []
        things = path.replace('/', ' ').split()
        for num in paths[len(things)]:
            folder = self.make_folder(f"folder-{num}")
            folders.append(folder)
        try:
            return folders
            # return [pmk.SFTPAttributes.from_stat(os.stat("/tmp"), filename="tmp")]
        except OSError as e:
            return pmk.SFTPServer.convert_errno(e.errno)

    def stat(self, path):

        logging.debug(f"\nStubSFTPServer | path : {path}")

        # os.chdir('/tmp')

        try:
            return pmk.SFTPAttributes.from_stat(os.stat("/tmp"))
        except OSError as e:
            return pmk.SFTPServer.convert_errno(e.errno) 

    def lstat(self, path):
        try:
            return pmk.SFTPAttributes.from_stat(os.stat("/tmp"))
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
        return "/tmp"