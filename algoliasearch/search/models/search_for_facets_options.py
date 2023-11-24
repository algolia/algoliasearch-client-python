# coding: utf-8

"""
    Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Annotated, BaseModel, Field, StrictStr
from search.models.search_type_facet import SearchTypeFacet

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SearchForFacetsOptions(BaseModel):
    """
    SearchForFacetsOptions
    """

    facet: StrictStr = Field(description="Facet name.")
    index_name: StrictStr = Field(description="Algolia index name.", alias="indexName")
    facet_query: Optional[StrictStr] = Field(
        default="",
        description="Text to search inside the facet's values.",
        alias="facetQuery",
    )
    max_facet_hits: Optional[Annotated[int, Field(le=100, strict=True)]] = Field(
        default=10,
        description="Maximum number of facet hits to return when [searching for facet values](https://www.algolia.com/doc/guides/managing-results/refine-results/faceting/#search-for-facet-values).",
        alias="maxFacetHits",
    )
    type: SearchTypeFacet
    __properties: ClassVar[List[str]] = [
        "facet",
        "indexName",
        "facetQuery",
        "maxFacetHits",
        "type",
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
        """Create an instance of SearchForFacetsOptions from a JSON string"""
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
        """Create an instance of SearchForFacetsOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "facet": obj.get("facet"),
                "indexName": obj.get("indexName"),
                "facetQuery": obj.get("facetQuery")
                if obj.get("facetQuery") is not None
                else "",
                "maxFacetHits": obj.get("maxFacetHits")
                if obj.get("maxFacetHits") is not None
                else 10,
                "type": obj.get("type"),
            }
        )
        return _obj
