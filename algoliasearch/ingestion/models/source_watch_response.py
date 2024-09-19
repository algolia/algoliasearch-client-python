# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

from json import loads
from sys import version_info
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, StrictStr

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


from algoliasearch.ingestion.models.event import Event


class SourceWatchResponse(BaseModel):
    """
    SourceWatchResponse
    """

    run_id: Optional[StrictStr] = Field(
        default=None,
        description="Universally unique identifier (UUID) of a task run.",
        alias="runID",
    )
    data: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="depending on the source type, the validation returns sampling data of your source (JSON, CSV, BigQuery).",
    )
    events: Optional[List[Event]] = Field(
        default=None,
        description="in case of error, observability events will be added to the response, if any.",
    )
    message: StrictStr = Field(
        description="a message describing the outcome of a validate run."
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SourceWatchResponse from a JSON string"""
        return cls.from_dict(loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
            exclude_unset=True,
        )
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict["events"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SourceWatchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "runID": obj.get("runID"),
                "data": obj.get("data"),
                "events": (
                    [Event.from_dict(_item) for _item in obj.get("events")]
                    if obj.get("events") is not None
                    else None
                ),
                "message": obj.get("message"),
            }
        )
        return _obj
