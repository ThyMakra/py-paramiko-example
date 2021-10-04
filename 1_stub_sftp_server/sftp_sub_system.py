import paramiko


class SFTPSubSystem(paramiko.SFTPServerInterface):

    # def __init__(self, server: ServerInterface, *largs: Any, **kwargs: Any) -> None:
    #     super().__init__(server, *largs, **kwargs)

    def __init__(self, channel, name, server):
        pass
    
    def start_subsystem(self, name, transport, channel):
        pass

    def finish_subsystem(self):
        pass
