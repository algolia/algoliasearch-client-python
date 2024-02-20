# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""
from __future__ import annotations

from json import loads
from typing import Any, Dict, List, Optional, Self

from pydantic import BaseModel, Field, StrictStr

from algoliasearch.search.models.synonym_type import SynonymType


class SynonymHit(BaseModel):
    """
    Synonym object.
    """

    object_id: StrictStr = Field(
        description="Unique identifier of a synonym object.", alias="objectID"
    )
    type: SynonymType
    synonyms: Optional[List[StrictStr]] = Field(
        default=None, description="Words or phrases considered equivalent."
    )
    input: Optional[StrictStr] = Field(
        default=None,
        description="Word or phrase to appear in query strings (for [`onewaysynonym`s](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/adding-synonyms/in-depth/one-way-synonyms/)).",
    )
    word: Optional[StrictStr] = Field(
        default=None,
        description="Word or phrase to appear in query strings (for [`altcorrection1` and `altcorrection2`](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/adding-synonyms/in-depth/synonyms-alternative-corrections/)).",
    )
    corrections: Optional[List[StrictStr]] = Field(
        default=None, description="Words to be matched in records."
    )
    placeholder: Optional[StrictStr] = Field(
        default=None,
        description="[Placeholder token](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/adding-synonyms/in-depth/synonyms-placeholders/) to be put inside records. ",
    )
    replacements: Optional[List[StrictStr]] = Field(
        default=None,
        description="Query words that will match the [placeholder token](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/adding-synonyms/in-depth/synonyms-placeholders/).",
    )

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SynonymHit from a JSON string"""
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
        """Create an instance of SynonymHit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "objectID": obj.get("objectID"),
                "type": obj.get("type"),
                "synonyms": obj.get("synonyms"),
                "input": obj.get("input"),
                "word": obj.get("word"),
                "corrections": obj.get("corrections"),
                "placeholder": obj.get("placeholder"),
                "replacements": obj.get("replacements"),
            }
        )
        return _obj