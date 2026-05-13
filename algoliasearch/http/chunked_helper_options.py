from dataclasses import dataclass


@dataclass
class ChunkedHelperOptions:
    """
    Optional configuration for chunked helpers that batch records and poll for task completion.
    """

    max_retries: int = 100
