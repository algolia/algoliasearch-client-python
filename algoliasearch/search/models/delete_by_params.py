# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""
from __future__ import annotations

from json import loads
from typing import Annotated, Any, Dict, List, Optional, Self, Union

from pydantic import BaseModel, Field, StrictStr

from algoliasearch.search.models.around_radius import AroundRadius
from algoliasearch.search.models.facet_filters import FacetFilters
from algoliasearch.search.models.numeric_filters import NumericFilters
from algoliasearch.search.models.tag_filters import TagFilters


class DeleteByParams(BaseModel):
    """
    DeleteByParams
    """

    facet_filters: Optional[FacetFilters] = Field(default=None, alias="facetFilters")
    filters: Optional[StrictStr] = Field(
        default="",
        description="Filter the search so that only records with matching values are included in the results.  These filters are supported:  - **Numeric filters.** `<facet> <op> <number>`, where `<op>` is one of `<`, `<=`, `=`, `!=`, `>`, `>=`. - **Ranges.** `<facet>:<lower> TO <upper>` where `<lower>` and `<upper>` are the lower and upper limits of the range (inclusive). - **Facet filters.** `<facet>:<value>` where `<facet>` is a facet attribute (case-sensitive) and `<value>` a facet value. - **Tag filters.** `_tags:<value>` or just `<value>` (case-sensitive). - **Boolean filters.** `<facet>: true | false`.  You can combine filters with `AND`, `OR`, and `NOT` operators with the following restrictions:  - You can only combine filters of the same type with `OR`.   **Not supported:** `facet:value OR num > 3`. - You can't use `NOT` with combinations of filters.   **Not supported:** `NOT(facet:value OR facet:value)` - You can't combine conjunctions (`AND`) with `OR`.   **Not supported:** `facet:value OR (facet:value AND facet:value)`  Use quotes around your filters, if the facet attribute name or facet value has spaces, keywords (`OR`, `AND`, `NOT`), or quotes. If a facet attribute is an array, the filter matches if it matches at least one element of the array.  For more information, see [Filters](https://www.algolia.com/doc/guides/managing-results/refine-results/filtering/). ",
    )
    numeric_filters: Optional[NumericFilters] = Field(
        default=None, alias="numericFilters"
    )
    tag_filters: Optional[TagFilters] = Field(default=None, alias="tagFilters")
    around_lat_lng: Optional[StrictStr] = Field(
        default="",
        description="Coordinates for the center of a circle, expressed as a comma-separated string of latitude and longitude.  Only records included within circle around this central location are included in the results. The radius of the circle is determined by the `aroundRadius` and `minimumAroundRadius` settings. This parameter is ignored if you also specify `insidePolygon` or `insideBoundingBox`. ",
        alias="aroundLatLng",
    )
    around_radius: Optional[AroundRadius] = Field(default=None, alias="aroundRadius")
    inside_bounding_box: Optional[
        List[
            List[
                Union[
                    Annotated[float, Field(strict=True)],
                    Annotated[int, Field(strict=True)],
                ]
            ]
        ]
    ] = Field(
        default=None,
        description="Coordinates for a rectangular area in which to search.  Each bounding box is defined by the two opposite points of its diagonal, and expressed as latitude and longitude pair: `[p1 lat, p1 long, p2 lat, p2 long]`. Provide multiple bounding boxes as nested arrays. For more information, see [rectangular area](https://www.algolia.com/doc/guides/managing-results/refine-results/geolocation/#filtering-inside-rectangular-or-polygonal-areas). ",
        alias="insideBoundingBox",
    )
    inside_polygon: Optional[
        List[
            List[
                Union[
                    Annotated[float, Field(strict=True)],
                    Annotated[int, Field(strict=True)],
                ]
            ]
        ]
    ] = Field(
        default=None,
        description="Coordinates of a polygon in which to search.  Polygons are defined by 3 to 10,000 points. Each point is represented by its latitude and longitude. Provide multiple polygons as nested arrays. For more information, see [filtering inside polygons](https://www.algolia.com/doc/guides/managing-results/refine-results/geolocation/#filtering-inside-rectangular-or-polygonal-areas). This parameter is ignored, if you also specify `insideBoundingBox`. ",
        alias="insidePolygon",
    )

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeleteByParams from a JSON string"""
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
        if self.facet_filters:
            _dict["facetFilters"] = self.facet_filters.to_dict()
        if self.numeric_filters:
            _dict["numericFilters"] = self.numeric_filters.to_dict()
        if self.tag_filters:
            _dict["tagFilters"] = self.tag_filters.to_dict()
        if self.around_radius:
            _dict["aroundRadius"] = self.around_radius.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DeleteByParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "facetFilters": (
                    FacetFilters.from_dict(obj.get("facetFilters"))
                    if obj.get("facetFilters") is not None
                    else None
                ),
                "filters": obj.get("filters"),
                "numericFilters": (
                    NumericFilters.from_dict(obj.get("numericFilters"))
                    if obj.get("numericFilters") is not None
                    else None
                ),
                "tagFilters": (
                    TagFilters.from_dict(obj.get("tagFilters"))
                    if obj.get("tagFilters") is not None
                    else None
                ),
                "aroundLatLng": obj.get("aroundLatLng"),
                "aroundRadius": (
                    AroundRadius.from_dict(obj.get("aroundRadius"))
                    if obj.get("aroundRadius") is not None
                    else None
                ),
                "insideBoundingBox": obj.get("insideBoundingBox"),
                "insidePolygon": obj.get("insidePolygon"),
            }
        )
        return _obj
