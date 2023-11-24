# coding: utf-8

"""
    Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field
from search.models.automatic_facet_filters import AutomaticFacetFilters
from search.models.consequence_query import ConsequenceQuery
from search.models.rendering_content import RenderingContent

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Params(BaseModel):
    """
    Additional search parameters.
    """

    query: Optional[ConsequenceQuery] = None
    automatic_facet_filters: Optional[AutomaticFacetFilters] = Field(
        default=None, alias="automaticFacetFilters"
    )
    automatic_optional_facet_filters: Optional[AutomaticFacetFilters] = Field(
        default=None, alias="automaticOptionalFacetFilters"
    )
    rendering_content: Optional[RenderingContent] = Field(
        default=None, alias="renderingContent"
    )
    __properties: ClassVar[List[str]] = [
        "query",
        "automaticFacetFilters",
        "automaticOptionalFacetFilters",
        "renderingContent",
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
        """Create an instance of Params from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of
        # query
        if self.query:
            _dict["query"] = self.query.to_dict()
        # override the default output from pydantic by calling `to_dict()` of
        # automatic_facet_filters
        if self.automatic_facet_filters:
            _dict["automaticFacetFilters"] = self.automatic_facet_filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of
        # automatic_optional_facet_filters
        if self.automatic_optional_facet_filters:
            _dict[
                "automaticOptionalFacetFilters"
            ] = self.automatic_optional_facet_filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of
        # rendering_content
        if self.rendering_content:
            _dict["renderingContent"] = self.rendering_content.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Params from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "query": ConsequenceQuery.from_dict(obj.get("query"))
                if obj.get("query") is not None
                else None,
                "automaticFacetFilters": AutomaticFacetFilters.from_dict(
                    obj.get("automaticFacetFilters")
                )
                if obj.get("automaticFacetFilters") is not None
                else None,
                "automaticOptionalFacetFilters": AutomaticFacetFilters.from_dict(
                    obj.get("automaticOptionalFacetFilters")
                )
                if obj.get("automaticOptionalFacetFilters") is not None
                else None,
                "renderingContent": RenderingContent.from_dict(
                    obj.get("renderingContent")
                )
                if obj.get("renderingContent") is not None
                else None,
            }
        )
        return _obj
