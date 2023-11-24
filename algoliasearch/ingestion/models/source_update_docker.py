# coding: utf-8

"""
    Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Union

from ingestion.models.docker_registry import DockerRegistry
from pydantic import BaseModel, Field, StrictStr

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SourceUpdateDocker(BaseModel):
    """
    SourceUpdateDocker
    """

    registry: Optional[DockerRegistry] = None
    image: Optional[StrictStr] = Field(
        default=None, description="The name of the image to pull."
    )
    version: Optional[StrictStr] = Field(
        default=None, description="The version of the image, defaults to `latest`."
    )
    configuration: Union[str, Any] = Field(description="The configuration of the spec.")
    __properties: ClassVar[List[str]] = [
        "registry",
        "image",
        "version",
        "configuration",
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True,
        # exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SourceUpdateDocker from a JSON string"""
        return cls.from_dict(json.loads(json_str))

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
        """Create an instance of SourceUpdateDocker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "registry": obj.get("registry"),
                "image": obj.get("image"),
                "version": obj.get("version"),
                "configuration": obj.get("configuration"),
            }
        )
        return _obj
