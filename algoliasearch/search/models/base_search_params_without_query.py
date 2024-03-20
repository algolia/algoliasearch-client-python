# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""
from __future__ import annotations

from json import loads
from typing import Annotated, Any, Dict, List, Optional, Self, Union

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

from algoliasearch.search.models.around_precision import AroundPrecision
from algoliasearch.search.models.around_radius import AroundRadius
from algoliasearch.search.models.facet_filters import FacetFilters
from algoliasearch.search.models.numeric_filters import NumericFilters
from algoliasearch.search.models.optional_filters import OptionalFilters
from algoliasearch.search.models.tag_filters import TagFilters


class BaseSearchParamsWithoutQuery(BaseModel):
    """
    BaseSearchParamsWithoutQuery
    """

    similar_query: Optional[StrictStr] = Field(
        default="",
        description="Keywords to be used instead of the search query to conduct a more broader search.  Using the `similarQuery` parameter changes other settings:  - `queryType` is set to `prefixNone`. - `removeStopWords` is set to true. - `words` is set as the first ranking criterion. - All remaining words are treated as `optionalWords`.  Since the `similarQuery` is supposed to do a broad search, they usually return many results. Combine it with `filters` to narrow down the list of results. ",
        alias="similarQuery",
    )
    filters: Optional[StrictStr] = Field(
        default="",
        description="Filter the search so that only records with matching values are included in the results.  These filters are supported:  - **Numeric filters.** `<facet> <op> <number>`, where `<op>` is one of `<`, `<=`, `=`, `!=`, `>`, `>=`. - **Ranges.** `<facet>:<lower> TO <upper>` where `<lower>` and `<upper>` are the lower and upper limits of the range (inclusive). - **Facet filters.** `<facet>:<value>` where `<facet>` is a facet attribute (case-sensitive) and `<value>` a facet value. - **Tag filters.** `_tags:<value>` or just `<value>` (case-sensitive). - **Boolean filters.** `<facet>: true | false`.  You can combine filters with `AND`, `OR`, and `NOT` operators with the following restrictions:  - You can only combine filters of the same type with `OR`.   **Not supported:** `facet:value OR num > 3`. - You can't use `NOT` with combinations of filters.   **Not supported:** `NOT(facet:value OR facet:value)` - You can't combine conjunctions (`AND`) with `OR`.   **Not supported:** `facet:value OR (facet:value AND facet:value)`  Use quotes around your filters, if the facet attribute name or facet value has spaces, keywords (`OR`, `AND`, `NOT`), or quotes. If a facet attribute is an array, the filter matches if it matches at least one element of the array.  For more information, see [Filters](https://www.algolia.com/doc/guides/managing-results/refine-results/filtering/). ",
    )
    facet_filters: Optional[FacetFilters] = Field(default=None, alias="facetFilters")
    optional_filters: Optional[OptionalFilters] = Field(
        default=None, alias="optionalFilters"
    )
    numeric_filters: Optional[NumericFilters] = Field(
        default=None, alias="numericFilters"
    )
    tag_filters: Optional[TagFilters] = Field(default=None, alias="tagFilters")
    sum_or_filters_scores: Optional[StrictBool] = Field(
        default=False,
        description="Whether to sum all filter scores.  If true, all filter scores are summed. Otherwise, the maximum filter score is kept. For more information, see [filter scores](https://www.algolia.com/doc/guides/managing-results/refine-results/filtering/in-depth/filter-scoring/#accumulating-scores-with-sumorfiltersscores). ",
        alias="sumOrFiltersScores",
    )
    restrict_searchable_attributes: Optional[List[StrictStr]] = Field(
        default=None,
        description="Restricts a search to a subset of your searchable attributes.",
        alias="restrictSearchableAttributes",
    )
    facets: Optional[List[StrictStr]] = Field(
        default=None,
        description="Facets for which to retrieve facet values that match the search criteria and the number of matching facet values.  To retrieve all facets, use the wildcard character `*`. For more information, see [facets](https://www.algolia.com/doc/guides/managing-results/refine-results/faceting/#contextual-facet-values-and-counts). ",
    )
    faceting_after_distinct: Optional[StrictBool] = Field(
        default=False,
        description="Whether faceting should be applied after deduplication with `distinct`.  This leads to accurate facet counts when using faceting in combination with `distinct`. It's usually better to use `afterDistinct` modifiers in the `attributesForFaceting` setting, as `facetingAfterDistinct` only computes correct facet counts if all records have the same facet values for the `attributeForDistinct`. ",
        alias="facetingAfterDistinct",
    )
    page: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=0, description="Page of search results to retrieve."
    )
    offset: Optional[StrictInt] = Field(
        default=None, description="Position of the first hit to retrieve."
    )
    length: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(
        default=None,
        description="Number of hits to retrieve (used in combination with `offset`).",
    )
    around_lat_lng: Optional[StrictStr] = Field(
        default="",
        description="Coordinates for the center of a circle, expressed as a comma-separated string of latitude and longitude.  Only records included within circle around this central location are included in the results. The radius of the circle is determined by the `aroundRadius` and `minimumAroundRadius` settings. This parameter is ignored if you also specify `insidePolygon` or `insideBoundingBox`. ",
        alias="aroundLatLng",
    )
    around_lat_lng_via_ip: Optional[StrictBool] = Field(
        default=False,
        description="Whether to obtain the coordinates from the request's IP address.",
        alias="aroundLatLngViaIP",
    )
    around_radius: Optional[AroundRadius] = Field(default=None, alias="aroundRadius")
    around_precision: Optional[AroundPrecision] = Field(
        default=None, alias="aroundPrecision"
    )
    minimum_around_radius: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(
        default=None,
        description="Minimum radius (in meters) for a search around a location when `aroundRadius` isn't set.",
        alias="minimumAroundRadius",
    )
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
    natural_languages: Optional[List[StrictStr]] = Field(
        default=None,
        description="ISO language codes that adjust settings that are useful for processing natural language queries (as opposed to keyword searches):  - Sets `removeStopWords` and `ignorePlurals` to the list of provided languages. - Sets `removeWordsIfNoResults` to `allOptional`. - Adds a `natural_language` attribute to `ruleContexts` and `analyticsTags`. ",
        alias="naturalLanguages",
    )
    rule_contexts: Optional[List[StrictStr]] = Field(
        default=None,
        description="Assigns a rule context to the search query.  [Rule contexts](https://www.algolia.com/doc/guides/managing-results/rules/rules-overview/how-to/customize-search-results-by-platform/#whats-a-context) are strings that you can use to trigger matching rules. ",
        alias="ruleContexts",
    )
    personalization_impact: Optional[
        Annotated[int, Field(le=100, strict=True, ge=0)]
    ] = Field(
        default=100,
        description="Impact that Personalization should have on this search.  The higher this value is, the more Personalization determines the ranking compared to other factors. For more information, see [Understanding Personalization impact](https://www.algolia.com/doc/guides/personalization/personalizing-results/in-depth/configuring-personalization/#understanding-personalization-impact). ",
        alias="personalizationImpact",
    )
    user_token: Optional[StrictStr] = Field(
        default=None,
        description="Unique pseudonymous or anonymous user identifier.  This helps with analytics and click and conversion events. For more information, see [user token](https://www.algolia.com/doc/guides/sending-events/concepts/usertoken/). ",
        alias="userToken",
    )
    get_ranking_info: Optional[StrictBool] = Field(
        default=False,
        description="Whether the search response should include detailed ranking information.",
        alias="getRankingInfo",
    )
    synonyms: Optional[StrictBool] = Field(
        default=True,
        description="Whether to take into account an index's synonyms for this search.",
    )
    click_analytics: Optional[StrictBool] = Field(
        default=False,
        description="Whether to include a `queryID` attribute in the response.  The query ID is a unique identifier for a search query and is required for tracking [click and conversion events](https://www.algolia.com/guides/sending-events/getting-started/). ",
        alias="clickAnalytics",
    )
    analytics: Optional[StrictBool] = Field(
        default=True, description="Whether this search will be included in Analytics."
    )
    analytics_tags: Optional[List[StrictStr]] = Field(
        default=None,
        description="Tags to apply to the query for [segmenting analytics data](https://www.algolia.com/doc/guides/search-analytics/guides/segments/).",
        alias="analyticsTags",
    )
    percentile_computation: Optional[StrictBool] = Field(
        default=True,
        description="Whether to include this search when calculating processing-time percentiles.",
        alias="percentileComputation",
    )
    enable_ab_test: Optional[StrictBool] = Field(
        default=True,
        description="Whether to enable A/B testing for this search.",
        alias="enableABTest",
    )

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BaseSearchParamsWithoutQuery from a JSON string"""
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
        if self.optional_filters:
            _dict["optionalFilters"] = self.optional_filters.to_dict()
        if self.numeric_filters:
            _dict["numericFilters"] = self.numeric_filters.to_dict()
        if self.tag_filters:
            _dict["tagFilters"] = self.tag_filters.to_dict()
        if self.around_radius:
            _dict["aroundRadius"] = self.around_radius.to_dict()
        if self.around_precision:
            _dict["aroundPrecision"] = self.around_precision.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BaseSearchParamsWithoutQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "similarQuery": obj.get("similarQuery"),
                "filters": obj.get("filters"),
                "facetFilters": (
                    FacetFilters.from_dict(obj.get("facetFilters"))
                    if obj.get("facetFilters") is not None
                    else None
                ),
                "optionalFilters": (
                    OptionalFilters.from_dict(obj.get("optionalFilters"))
                    if obj.get("optionalFilters") is not None
                    else None
                ),
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
                "sumOrFiltersScores": obj.get("sumOrFiltersScores"),
                "restrictSearchableAttributes": obj.get("restrictSearchableAttributes"),
                "facets": obj.get("facets"),
                "facetingAfterDistinct": obj.get("facetingAfterDistinct"),
                "page": obj.get("page"),
                "offset": obj.get("offset"),
                "length": obj.get("length"),
                "aroundLatLng": obj.get("aroundLatLng"),
                "aroundLatLngViaIP": obj.get("aroundLatLngViaIP"),
                "aroundRadius": (
                    AroundRadius.from_dict(obj.get("aroundRadius"))
                    if obj.get("aroundRadius") is not None
                    else None
                ),
                "aroundPrecision": (
                    AroundPrecision.from_dict(obj.get("aroundPrecision"))
                    if obj.get("aroundPrecision") is not None
                    else None
                ),
                "minimumAroundRadius": obj.get("minimumAroundRadius"),
                "insideBoundingBox": obj.get("insideBoundingBox"),
                "insidePolygon": obj.get("insidePolygon"),
                "naturalLanguages": obj.get("naturalLanguages"),
                "ruleContexts": obj.get("ruleContexts"),
                "personalizationImpact": obj.get("personalizationImpact"),
                "userToken": obj.get("userToken"),
                "getRankingInfo": obj.get("getRankingInfo"),
                "synonyms": obj.get("synonyms"),
                "clickAnalytics": obj.get("clickAnalytics"),
                "analytics": obj.get("analytics"),
                "analyticsTags": obj.get("analyticsTags"),
                "percentileComputation": obj.get("percentileComputation"),
                "enableABTest": obj.get("enableABTest"),
            }
        )
        return _obj
