from media_platform.configuration.configuration import Configuration


class Authenticator(object):
    def __init__(self, configuration):
        # type: (Configuration) -> None
        super(Authenticator, self).__init__()

        self.configuration = configuration

    def get_header(self):
        raise NotImplementedError()
