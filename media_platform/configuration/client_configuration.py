class ClientConfiguration(object):
    def __init__(self, domain, app_id, shared_secret):
        # type: (str, str, str) -> None
        super(ClientConfiguration, self).__init__()

        self.domain = domain
        self.app_id = app_id
        self.shared_secret = shared_secret

        self.base_url = 'https://' + domain + '/_api'
