from algoliasearch.response.response import Response


class IndexingResponse(Response):

    def wait(self):
        # type: () -> None

        self._index.wait_task(self.body['taskID'])
