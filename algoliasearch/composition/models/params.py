# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

from json import loads
from sys import version_info
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


from algoliasearch.composition.models.around_precision import AroundPrecision
from algoliasearch.composition.models.around_radius import AroundRadius
from algoliasearch.composition.models.facet_filters import FacetFilters
from algoliasearch.composition.models.inside_bounding_box import InsideBoundingBox
from algoliasearch.composition.models.numeric_filters import NumericFilters
from algoliasearch.composition.models.optional_filters import OptionalFilters
from algoliasearch.composition.models.supported_language import SupportedLanguage

_ALIASES = {
    "query": "query",
    "filters": "filters",
    "page": "page",
    "get_ranking_info": "getRankingInfo",
    "relevancy_strictness": "relevancyStrictness",
    "facet_filters": "facetFilters",
    "optional_filters": "optionalFilters",
    "numeric_filters": "numericFilters",
    "hits_per_page": "hitsPerPage",
    "around_lat_lng": "aroundLatLng",
    "around_lat_lng_via_ip": "aroundLatLngViaIP",
    "around_radius": "aroundRadius",
    "around_precision": "aroundPrecision",
    "minimum_around_radius": "minimumAroundRadius",
    "inside_bounding_box": "insideBoundingBox",
    "inside_polygon": "insidePolygon",
    "query_languages": "queryLanguages",
    "natural_languages": "naturalLanguages",
    "enable_rules": "enableRules",
    "rule_contexts": "ruleContexts",
    "user_token": "userToken",
    "click_analytics": "clickAnalytics",
    "analytics": "analytics",
    "analytics_tags": "analyticsTags",
    "enable_ab_test": "enableABTest",
    "enable_re_ranking": "enableReRanking",
}


def _alias_generator(name: str) -> str:
    return _ALIASES.get(name, name)


class Params(BaseModel):
    """
    Params
    """

    query: Optional[str] = None
    """ Search query. """
    filters: Optional[str] = None
    """ Filter expression to only include items that match the filter criteria in the response.  You can use these filter expressions:  - **Numeric filters.** `<facet> <op> <number>`, where `<op>` is one of `<`, `<=`, `=`, `!=`, `>`, `>=`. - **Ranges.** `<facet>:<lower> TO <upper>` where `<lower>` and `<upper>` are the lower and upper limits of the range (inclusive). - **Facet filters.** `<facet>:<value>` where `<facet>` is a facet attribute (case-sensitive) and `<value>` a facet value. - **Tag filters.** `_tags:<value>` or just `<value>` (case-sensitive). - **Boolean filters.** `<facet>: true | false`.  You can combine filters with `AND`, `OR`, and `NOT` operators with the following restrictions:  - You can only combine filters of the same type with `OR`.   **Not supported:** `facet:value OR num > 3`. - You can't use `NOT` with combinations of filters.   **Not supported:** `NOT(facet:value OR facet:value)` - You can't combine conjunctions (`AND`) with `OR`.   **Not supported:** `facet:value OR (facet:value AND facet:value)`  Use quotes around your filters, if the facet attribute name or facet value has spaces, keywords (`OR`, `AND`, `NOT`), or quotes. If a facet attribute is an array, the filter matches if it matches at least one element of the array.  For more information, see [Filters](https://www.algolia.com/doc/guides/managing-results/refine-results/filtering/).  """
    page: Optional[int] = None
    """ Page of search results to retrieve. """
    get_ranking_info: Optional[bool] = None
    """ Whether the search response should include detailed ranking information. """
    relevancy_strictness: Optional[int] = None
    facet_filters: Optional[FacetFilters] = None
    optional_filters: Optional[OptionalFilters] = None
    numeric_filters: Optional[NumericFilters] = None
    hits_per_page: Optional[int] = None
    """ Number of hits per page. """
    around_lat_lng: Optional[str] = None
    """ Coordinates for the center of a circle, expressed as a comma-separated string of latitude and longitude.  Only records included within a circle around this central location are included in the results. The radius of the circle is determined by the `aroundRadius` and `minimumAroundRadius` settings. This parameter is ignored if you also specify `insidePolygon` or `insideBoundingBox`.  """
    around_lat_lng_via_ip: Optional[bool] = None
    """ Whether to obtain the coordinates from the request's IP address. """
    around_radius: Optional[AroundRadius] = None
    around_precision: Optional[AroundPrecision] = None
    minimum_around_radius: Optional[int] = None
    """ Minimum radius (in meters) for a search around a location when `aroundRadius` isn't set. """
    inside_bounding_box: Optional[InsideBoundingBox] = None
    inside_polygon: Optional[List[List[float]]] = None
    """ Coordinates of a polygon in which to search.  Polygons are defined by 3 to 10,000 points. Each point is represented by its latitude and longitude. Provide multiple polygons as nested arrays. For more information, see [filtering inside polygons](https://www.algolia.com/doc/guides/managing-results/refine-results/geolocation/#filtering-inside-rectangular-or-polygonal-areas). This parameter is ignored if you also specify `insideBoundingBox`.  """
    query_languages: Optional[List[SupportedLanguage]] = None
    """ Languages for language-specific query processing steps such as plurals, stop-word removal, and word-detection dictionaries.  This setting sets a default list of languages used by the `removeStopWords` and `ignorePlurals` settings. This setting also sets a dictionary for word detection in the logogram-based [CJK](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/normalization/#normalization-for-logogram-based-languages-cjk) languages. To support this, you must place the CJK language **first**.  **You should always specify a query language.** If you don't specify an indexing language, the search engine uses all [supported languages](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/supported-languages/), or the languages you specified with the `ignorePlurals` or `removeStopWords` parameters. This can lead to unexpected search results. For more information, see [Language-specific configuration](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/language-specific-configurations/).  """
    natural_languages: Optional[List[SupportedLanguage]] = None
    """ ISO language codes that adjust settings that are useful for processing natural language queries (as opposed to keyword searches):  - Sets `removeStopWords` and `ignorePlurals` to the list of provided languages. - Sets `removeWordsIfNoResults` to `allOptional`. - Adds a `natural_language` attribute to `ruleContexts` and `analyticsTags`.  """
    enable_rules: Optional[bool] = None
    """ Whether to enable rules. """
    rule_contexts: Optional[List[str]] = None
    """ Assigns a rule context to the search query.  [Rule contexts](https://www.algolia.com/doc/guides/managing-results/rules/rules-overview/how-to/customize-search-results-by-platform/#whats-a-context) are strings that you can use to trigger matching rules.  """
    user_token: Optional[str] = None
    """ Unique pseudonymous or anonymous user identifier.  This helps with analytics and click and conversion events. For more information, see [user token](https://www.algolia.com/doc/guides/sending-events/concepts/usertoken/).  """
    click_analytics: Optional[bool] = None
    """ Whether to include a `queryID` attribute in the response.  The query ID is a unique identifier for a search query and is required for tracking [click and conversion events](https://www.algolia.com/guides/sending-events/getting-started/).  """
    analytics: Optional[bool] = None
    """ Whether this search will be included in Analytics. """
    analytics_tags: Optional[List[str]] = None
    """ Tags to apply to the query for [segmenting analytics data](https://www.algolia.com/doc/guides/search-analytics/guides/segments/). """
    enable_ab_test: Optional[bool] = None
    """ Whether to enable A/B testing for this search. """
    enable_re_ranking: Optional[bool] = None
    """ Whether this search will use [Dynamic Re-Ranking](https://www.algolia.com/doc/guides/algolia-ai/re-ranking/).  This setting only has an effect if you activated Dynamic Re-Ranking for this index in the Algolia dashboard.  """

    model_config = ConfigDict(
        strict=False,
        use_enum_values=True,
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        alias_generator=_alias_generator,
        extra="allow",
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Params from a JSON string"""
        return cls.from_dict(loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias."""
        return self.model_dump(
            by_alias=True,
            exclude_none=True,
            exclude_unset=True,
        )

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Params from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        obj["facetFilters"] = (
            FacetFilters.from_dict(obj["facetFilters"])
            if obj.get("facetFilters") is not None
            else None
        )
        obj["optionalFilters"] = (
            OptionalFilters.from_dict(obj["optionalFilters"])
            if obj.get("optionalFilters") is not None
            else None
        )
        obj["numericFilters"] = (
            NumericFilters.from_dict(obj["numericFilters"])
            if obj.get("numericFilters") is not None
            else None
        )
        obj["aroundRadius"] = (
            AroundRadius.from_dict(obj["aroundRadius"])
            if obj.get("aroundRadius") is not None
            else None
        )
        obj["aroundPrecision"] = (
            AroundPrecision.from_dict(obj["aroundPrecision"])
            if obj.get("aroundPrecision") is not None
            else None
        )
        obj["insideBoundingBox"] = (
            InsideBoundingBox.from_dict(obj["insideBoundingBox"])
            if obj.get("insideBoundingBox") is not None
            else None
        )
        obj["queryLanguages"] = obj.get("queryLanguages")
        obj["naturalLanguages"] = obj.get("naturalLanguages")

        return cls.model_validate(obj)