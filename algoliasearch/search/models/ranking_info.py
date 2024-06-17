# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""
from __future__ import annotations

from json import loads
from typing import Annotated, Any, Dict, Optional, Self

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt

from algoliasearch.search.models.matched_geo_location import MatchedGeoLocation
from algoliasearch.search.models.personalization import Personalization


class RankingInfo(BaseModel):
    """
    Object with detailed information about the record's ranking.
    """

    filters: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, description="Whether a filter matched the query."
    )
    first_matched_word: Annotated[int, Field(strict=True, ge=0)] = Field(
        description="Position of the first matched word in the best matching attribute of the record.",
        alias="firstMatchedWord",
    )
    geo_distance: Annotated[int, Field(strict=True, ge=0)] = Field(
        description="Distance between the geo location in the search query and the best matching geo location in the record, divided by the geo precision (in meters).",
        alias="geoDistance",
    )
    geo_precision: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="Precision used when computing the geo distance, in meters.",
        alias="geoPrecision",
    )
    matched_geo_location: Optional[MatchedGeoLocation] = Field(
        default=None, alias="matchedGeoLocation"
    )
    personalization: Optional[Personalization] = None
    nb_exact_words: Annotated[int, Field(strict=True, ge=0)] = Field(
        description="Number of exactly matched words.", alias="nbExactWords"
    )
    nb_typos: Annotated[int, Field(strict=True, ge=0)] = Field(
        description="Number of typos encountered when matching the record.",
        alias="nbTypos",
    )
    promoted: Optional[StrictBool] = Field(
        default=None, description="Whether the record was promoted by a rule."
    )
    proximity_distance: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None,
        description="Number of words between multiple matches in the query plus 1. For single word queries, `proximityDistance` is 0.",
        alias="proximityDistance",
    )
    user_score: StrictInt = Field(
        description="Overall ranking of the record, expressed as a single integer. This attribute is internal.",
        alias="userScore",
    )
    words: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None, description="Number of matched words."
    )
    promoted_by_re_ranking: Optional[StrictBool] = Field(
        default=None,
        description="Whether the record is re-ranked.",
        alias="promotedByReRanking",
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RankingInfo from a JSON string"""
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
        if self.matched_geo_location:
            _dict["matchedGeoLocation"] = self.matched_geo_location.to_dict()
        if self.personalization:
            _dict["personalization"] = self.personalization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RankingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "filters": obj.get("filters"),
                "firstMatchedWord": obj.get("firstMatchedWord"),
                "geoDistance": obj.get("geoDistance"),
                "geoPrecision": obj.get("geoPrecision"),
                "matchedGeoLocation": (
                    MatchedGeoLocation.from_dict(obj.get("matchedGeoLocation"))
                    if obj.get("matchedGeoLocation") is not None
                    else None
                ),
                "personalization": (
                    Personalization.from_dict(obj.get("personalization"))
                    if obj.get("personalization") is not None
                    else None
                ),
                "nbExactWords": obj.get("nbExactWords"),
                "nbTypos": obj.get("nbTypos"),
                "promoted": obj.get("promoted"),
                "proximityDistance": obj.get("proximityDistance"),
                "userScore": obj.get("userScore"),
                "words": obj.get("words"),
                "promotedByReRanking": obj.get("promotedByReRanking"),
            }
        )
        return _obj
