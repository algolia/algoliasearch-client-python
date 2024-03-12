# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""
from __future__ import annotations

from json import loads
from re import match
from typing import Annotated, Any, Dict, Self

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator


class UserId(BaseModel):
    """
    Unique user ID.
    """

    user_id: Annotated[str, Field(strict=True)] = Field(
        description="User ID.", alias="userID"
    )
    cluster_name: StrictStr = Field(
        description="Cluster to which the user is assigned.", alias="clusterName"
    )
    nb_records: StrictInt = Field(
        description="Number of records belonging to the user.", alias="nbRecords"
    )
    data_size: StrictInt = Field(
        description="Data size used by the user.", alias="dataSize"
    )

    @field_validator("user_id")
    def user_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not match(r"^[a-zA-Z0-9 \-*.]+$", value):
            raise ValueError(
                r"must validate the regular expression /^[a-zA-Z0-9 \-*.]+$/"
            )
        return value

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserId from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "userID": obj.get("userID"),
                "clusterName": obj.get("clusterName"),
                "nbRecords": obj.get("nbRecords"),
                "dataSize": obj.get("dataSize"),
            }
        )
        return _obj
