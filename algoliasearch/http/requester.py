from requests import Request


class Requester:
    def __init__(self, request: Request = None):
        self.__request = Request() if request is None else request

    def request(self, verb: str, url: str, payload: dict, request_options):
        self.__request.request(verb, url, payload)

