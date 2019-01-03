class Host(object):
    def __init__(self, url, priority=0):
        # type: (str, int) -> None

        self.url = url
        self.priority = priority
        self.retry_count = 0
        self.up = True
