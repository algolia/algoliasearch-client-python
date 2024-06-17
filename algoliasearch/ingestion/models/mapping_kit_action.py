# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""
from __future__ import annotations

from json import loads
from typing import Any, Dict, List, Optional, Self

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr

from algoliasearch.ingestion.models.mapping_field_directive import MappingFieldDirective


class MappingKitAction(BaseModel):
    """
    Describes how a destination object should be resolved by means of applying a set of directives.
    """

    id: Optional[StrictStr] = Field(
        default=None, description="ID to uniquely identify this action."
    )
    enabled: StrictBool = Field(description="Whether this action has any effect.")
    trigger: StrictStr = Field(
        description="Condition which must be satisfied to apply the action. If this evaluates to false, the action is not applied, and the process attempts to apply the next action, if any."
    )
    field_directives: List[MappingFieldDirective] = Field(alias="fieldDirectives")

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MappingKitAction from a JSON string"""
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
        _items = []
        if self.field_directives:
            for _item in self.field_directives:
                if _item:
                    _items.append(_item.to_dict())
            _dict["fieldDirectives"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MappingKitAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "enabled": obj.get("enabled"),
                "trigger": obj.get("trigger"),
                "fieldDirectives": (
                    [
                        MappingFieldDirective.from_dict(_item)
                        for _item in obj.get("fieldDirectives")
                    ]
                    if obj.get("fieldDirectives") is not None
                    else None
                ),
            }
        )
        return _obj
