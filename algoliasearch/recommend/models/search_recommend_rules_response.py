# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

from json import loads
from sys import version_info
from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict, Field, StrictInt

if version_info >= (3, 11):
    from typing import Annotated, Self
else:
    from typing_extensions import Annotated, Self


from algoliasearch.recommend.models.recommend_rule import RecommendRule


class SearchRecommendRulesResponse(BaseModel):
    """
    SearchRecommendRulesResponse
    """

    hits: List[RecommendRule] = Field(
        description="Recommend rules that match the search criteria."
    )
    nb_hits: StrictInt = Field(description="Number of results (hits).", alias="nbHits")
    page: Annotated[int, Field(strict=True, ge=0)] = Field(
        description="Page of search results to retrieve."
    )
    nb_pages: StrictInt = Field(
        description="Number of pages of results.", alias="nbPages"
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SearchRecommendRulesResponse from a JSON string"""
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
        if self.hits:
            for _item in self.hits:
                if _item:
                    _items.append(_item.to_dict())
            _dict["hits"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SearchRecommendRulesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "hits": (
                    [RecommendRule.from_dict(_item) for _item in obj.get("hits")]
                    if obj.get("hits") is not None
                    else None
                ),
                "nbHits": obj.get("nbHits"),
                "page": obj.get("page"),
                "nbPages": obj.get("nbPages"),
            }
        )
        return _obj
