# coding: utf-8

from asyncio import sleep
from json import loads
from typing import Any, Callable, Dict, List, Optional, Protocol, Self, TypeVar, Union

from pydantic import BaseModel

from algoliasearch.search.models.search_params_object import SearchParamsObject

T = TypeVar("T")


class Timeout(Protocol):
    def __call__(self) -> int:
        return 0

    def __init__(self) -> None:
        pass


class RetryTimeout(Timeout):
    def __call__(self, retry_count: int) -> int:
        return min(retry_count * 0.2, 5)

    def __init__(self) -> None:
        pass


async def create_iterable(
    func: Callable[[T], T],
    validate: Callable[[T], bool],
    aggregator: Callable[[T], None],
    timeout: Timeout = Timeout(),
    error_validate: Callable[[T], bool] = None,
    error_message: Callable[[T], str] = None,
) -> T:
    """
    Helper: Iterates until the given `func` until `timeout` or `validate`.
    """

    async def retry(prev: T = None) -> T:
        resp = await func(prev)

        if aggregator:
            aggregator(resp)

        if validate(resp):
            return resp

        if error_validate is not None and error_validate(resp):
            if error_message is None:
                raise Exception("An error occurred")
            raise Exception(error_message(resp))

        await sleep(timeout())
        return await retry(resp)

    return await retry()


class SecuredApiKeyRestrictions(BaseModel):
    """
    SecuredApiKeyRestrictions
    """

    search_params: SearchParamsObject = SearchParamsObject()
    valid_until: Optional[int] = 0
    restrict_indices: Optional[Union[List[str], str]] = None
    restrict_sources: Optional[str] = None
    user_token: Optional[str] = None

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SecuredApiKeyRestrictions from a JSON string"""
        return cls.from_dict(loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        return self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SecuredApiKeyRestrictions from a dict"""
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        return cls.model_validate(
            {
                "search_params": SearchParamsObject.from_dict(obj.get("search_params")),
                "valid_until": int(obj.get("valid_until")),
                "restrict_indices": obj.get("restrict_indices"),
                "restrict_sources": obj.get("restrict_sources"),
                "user_token": obj.get("user_token"),
            }
        )
