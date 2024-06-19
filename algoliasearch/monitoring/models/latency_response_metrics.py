# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

from json import loads
from typing import Any, Dict, List, Optional, Self

from pydantic import BaseModel, ConfigDict

from algoliasearch.monitoring.models.time_inner import TimeInner


class LatencyResponseMetrics(BaseModel):
    """
    LatencyResponseMetrics
    """

    latency: Optional[Dict[str, List[TimeInner]]] = None

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LatencyResponseMetrics from a JSON string"""
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
        )
        _field_dict_of_array = {}
        if self.latency:
            for _key in self.latency:
                if self.latency[_key] is not None:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.latency[_key]
                    ]
            _dict["latency"] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LatencyResponseMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "latency": dict(
                    (
                        _k,
                        [TimeInner.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None,
                    )
                    for _k, _v in obj.get("latency").items()
                )
            }
        )
        return _obj
