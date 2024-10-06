# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

from json import loads
from sys import version_info
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


from algoliasearch.ingestion.models.destination_input import DestinationInput
from algoliasearch.ingestion.models.destination_type import DestinationType

_ALIASES = {
    "type": "type",
    "name": "name",
    "input": "input",
    "authentication_id": "authenticationID",
    "transformation_ids": "transformationIDs",
}


def _alias_generator(name: str) -> str:
    return _ALIASES.get(name, name)


class DestinationCreate(BaseModel):
    """
    API request body for creating a new destination.
    """

    type: DestinationType
    name: str
    """ Descriptive name for the resource. """
    input: DestinationInput
    authentication_id: Optional[str] = None
    """ Universally unique identifier (UUID) of an authentication resource. """
    transformation_ids: Optional[List[str]] = None

    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        alias_generator=_alias_generator,
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DestinationCreate from a JSON string"""
        return cls.from_dict(loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias."""
        return self.model_dump(
            by_alias=True,
            exclude_none=True,
            exclude_unset=True,
        )

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DestinationCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        obj["type"] = obj.get("type")
        obj["input"] = (
            DestinationInput.from_dict(obj["input"])
            if obj.get("input") is not None
            else None
        )

        return cls.model_validate(obj)
