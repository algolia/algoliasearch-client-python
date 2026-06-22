from dataclasses import dataclass
from typing import ClassVar


@dataclass
class ChunkedHelperOptions:
    """
    Optional configuration for chunked helpers that batch records and poll for task completion.
    """

    DEFAULT_REPLACE_ALL_OBJECTS_MAX_RETRIES: ClassVar[int] = 800

    max_retries: int = 100
