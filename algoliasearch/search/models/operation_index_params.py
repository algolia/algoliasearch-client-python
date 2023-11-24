# coding: utf-8

"""
    Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictStr
from search.models.operation_type import OperationType
from search.models.scope_type import ScopeType

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class OperationIndexParams(BaseModel):
    """
    OperationIndexParams
    """

    operation: OperationType
    destination: StrictStr = Field(description="Algolia index name.")
    scope: Optional[List[ScopeType]] = Field(
        default=None,
        description="**This only applies to the _copy_ operation.**  If you omit `scope`, the copy command copies all records, settings, synonyms, and rules.  If you specify `scope`, only the specified scopes are copied.",
    )
    __properties: ClassVar[List[str]] = ["operation", "destination", "scope"]

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
        """Create an instance of OperationIndexParams from a JSON string"""
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
        """Create an instance of OperationIndexParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "operation": obj.get("operation"),
                "destination": obj.get("destination"),
                "scope": obj.get("scope"),
            }
        )
        return _obj
