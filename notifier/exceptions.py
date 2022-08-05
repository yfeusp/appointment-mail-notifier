class InvalidMailCredentialsError(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid mail credentials.")


class InvalidRecipientError(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid recipient.")


class HostOrPortFailedConnectionError(Exception):
    def __init__(self):
        Exception.__init__(
            self, "SMTP host or port could not connect with the server."
        )
