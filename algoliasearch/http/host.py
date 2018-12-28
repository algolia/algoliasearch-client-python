class Host:
    def __init__(self, url: str, priority: int = 0):
        self.url = url
        self.priority = priority
        self.retry_count = 0
        self.up = True
