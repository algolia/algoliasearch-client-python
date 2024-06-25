# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""

from __future__ import annotations

from json import loads
from typing import Annotated, Any, Dict, List, Optional, Self

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr

from algoliasearch.search.models.advanced_syntax_features import AdvancedSyntaxFeatures
from algoliasearch.search.models.alternatives_as_exact import AlternativesAsExact
from algoliasearch.search.models.distinct import Distinct
from algoliasearch.search.models.exact_on_single_word_query import (
    ExactOnSingleWordQuery,
)
from algoliasearch.search.models.ignore_plurals import IgnorePlurals
from algoliasearch.search.models.mode import Mode
from algoliasearch.search.models.query_type import QueryType
from algoliasearch.search.models.re_ranking_apply_filter import ReRankingApplyFilter
from algoliasearch.search.models.remove_stop_words import RemoveStopWords
from algoliasearch.search.models.remove_words_if_no_results import (
    RemoveWordsIfNoResults,
)
from algoliasearch.search.models.rendering_content import RenderingContent
from algoliasearch.search.models.semantic_search import SemanticSearch
from algoliasearch.search.models.supported_language import SupportedLanguage
from algoliasearch.search.models.typo_tolerance import TypoTolerance


class IndexSettings(BaseModel):
    """
    Index settings.
    """

    attributes_for_faceting: Optional[List[StrictStr]] = Field(
        default=None,
        description='Attributes used for [faceting](https://www.algolia.com/doc/guides/managing-results/refine-results/faceting/).  Facets are attributes that let you categorize search results. They can be used for filtering search results. By default, no attribute is used for faceting. Attribute names are case-sensitive.  **Modifiers**  - `filterOnly("ATTRIBUTE")`.   Allows using this attribute as a filter, but doesn\'t evalue the facet values.  - `searchable("ATTRIBUTE")`.   Allows searching for facet values.  - `afterDistinct("ATTRIBUTE")`.   Evaluates the facet count _after_ deduplication with `distinct`.   This ensures accurate facet counts.   You can apply this modifier to searchable facets: `afterDistinct(searchable(ATTRIBUTE))`. ',
        alias="attributesForFaceting",
    )
    replicas: Optional[List[StrictStr]] = Field(
        default=None,
        description="Creates [replica indices](https://www.algolia.com/doc/guides/managing-results/refine-results/sorting/in-depth/replicas/).  Replicas are copies of a primary index with the same records but different settings, synonyms, or rules. If you want to offer a different ranking or sorting of your search results, you'll use replica indices. All index operations on a primary index are automatically forwarded to its replicas. To add a replica index, you must provide the complete set of replicas to this parameter. If you omit a replica from this list, the replica turns into a regular, standalone index that will no longer by synced with the primary index.  **Modifier**  - `virtual(\"REPLICA\")`.   Create a virtual replica,   Virtual replicas don't increase the number of records and are optimized for [Relevant sorting](https://www.algolia.com/doc/guides/managing-results/refine-results/sorting/in-depth/relevant-sort/). ",
    )
    virtual: Optional[StrictBool] = Field(
        default=None,
        description="Only present if the index is a [virtual replica](https://www.algolia.com/doc/guides/managing-results/refine-results/sorting/how-to/sort-an-index-alphabetically/#virtual-replicas).",
    )
    pagination_limited_to: Optional[Annotated[int, Field(le=20000, strict=True)]] = (
        Field(
            default=1000,
            description="Maximum number of search results that can be obtained through pagination.  Higher pagination limits might slow down your search. For pagination limits above 1,000, the sorting of results beyond the 1,000th hit can't be guaranteed. ",
            alias="paginationLimitedTo",
        )
    )
    unretrievable_attributes: Optional[List[StrictStr]] = Field(
        default=None,
        description="Attributes that can't be retrieved at query time.  This can be useful if you want to use an attribute for ranking or to [restrict access](https://www.algolia.com/doc/guides/security/api-keys/how-to/user-restricted-access-to-data/), but don't want to include it in the search results. Attribute names are case-sensitive. ",
        alias="unretrievableAttributes",
    )
    disable_typo_tolerance_on_words: Optional[List[StrictStr]] = Field(
        default=None,
        description="Words for which you want to turn off [typo tolerance](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/typo-tolerance/). This also turns off [word splitting and concatenation](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/splitting-and-concatenation/) for the specified words. ",
        alias="disableTypoToleranceOnWords",
    )
    attributes_to_transliterate: Optional[List[StrictStr]] = Field(
        default=None,
        description="Attributes, for which you want to support [Japanese transliteration](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/language-specific-configurations/#japanese-transliteration-and-type-ahead).  Transliteration supports searching in any of the Japanese writing systems. To support transliteration, you must set the indexing language to Japanese. Attribute names are case-sensitive. ",
        alias="attributesToTransliterate",
    )
    camel_case_attributes: Optional[List[StrictStr]] = Field(
        default=None,
        description="Attributes for which to split [camel case](https://wikipedia.org/wiki/Camel_case) words. Attribute names are case-sensitive. ",
        alias="camelCaseAttributes",
    )
    decompounded_attributes: Optional[Dict[str, Any]] = Field(
        default=None,
        description='Searchable attributes to which Algolia should apply [word segmentation](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/how-to/customize-segmentation/) (decompounding). Attribute names are case-sensitive.  Compound words are formed by combining two or more individual words, and are particularly prevalent in Germanic languages—for example, "firefighter". With decompounding, the individual components are indexed separately.  You can specify different lists for different languages. Decompounding is supported for these languages: Dutch (`nl`), German (`de`), Finnish (`fi`), Danish (`da`), Swedish (`sv`), and Norwegian (`no`). ',
        alias="decompoundedAttributes",
    )
    index_languages: Optional[List[SupportedLanguage]] = Field(
        default=None,
        description="Languages for language-specific processing steps, such as word detection and dictionary settings.  **You should always specify an indexing language.** If you don't specify an indexing language, the search engine uses all [supported languages](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/supported-languages/), or the languages you specified with the `ignorePlurals` or `removeStopWords` parameters. This can lead to unexpected search results. For more information, see [Language-specific configuration](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/language-specific-configurations/). ",
        alias="indexLanguages",
    )
    disable_prefix_on_attributes: Optional[List[StrictStr]] = Field(
        default=None,
        description="Searchable attributes for which you want to turn off [prefix matching](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/override-search-engine-defaults/#adjusting-prefix-search). Attribute names are case-sensitive. ",
        alias="disablePrefixOnAttributes",
    )
    allow_compression_of_integer_array: Optional[StrictBool] = Field(
        default=False,
        description="Whether arrays with exclusively non-negative integers should be compressed for better performance. If true, the compressed arrays may be reordered. ",
        alias="allowCompressionOfIntegerArray",
    )
    numeric_attributes_for_filtering: Optional[List[StrictStr]] = Field(
        default=None,
        description='Numeric attributes that can be used as [numerical filters](https://www.algolia.com/doc/guides/managing-results/rules/detecting-intent/how-to/applying-a-custom-filter-for-a-specific-query/#numerical-filters). Attribute names are case-sensitive.  By default, all numeric attributes are available as numerical filters. For faster indexing, reduce the number of numeric attributes.  If you want to turn off filtering for all numeric attributes, specifiy an attribute that doesn\'t exist in your index, such as `NO_NUMERIC_FILTERING`.  **Modifier**  - `equalOnly("ATTRIBUTE")`.   Support only filtering based on equality comparisons `=` and `!=`. ',
        alias="numericAttributesForFiltering",
    )
    separators_to_index: Optional[StrictStr] = Field(
        default="",
        description="Controls which separators are indexed.  Separators are all non-letter characters except spaces and currency characters, such as $€£¥. By default, separator characters aren't indexed. With `separatorsToIndex`, Algolia treats separator characters as separate words. For example, a search for `C#` would report two matches. ",
        alias="separatorsToIndex",
    )
    searchable_attributes: Optional[List[StrictStr]] = Field(
        default=None,
        description='Attributes used for searching. Attribute names are case-sensitive.  By default, all attributes are searchable and the [Attribute](https://www.algolia.com/doc/guides/managing-results/relevance-overview/in-depth/ranking-criteria/#attribute) ranking criterion is turned off. With a non-empty list, Algolia only returns results with matches in the selected attributes. In addition, the Attribute ranking criterion is turned on: matches in attributes that are higher in the list of `searchableAttributes` rank first. To make matches in two attributes rank equally, include them in a comma-separated string, such as `"title,alternate_title"`. Attributes with the same priority are always unordered.  For more information, see [Searchable attributes](https://www.algolia.com/doc/guides/sending-and-managing-data/prepare-your-data/how-to/setting-searchable-attributes/).  **Modifier**  - `unordered("ATTRIBUTE")`.   Ignore the position of a match within the attribute.  Without modifier, matches at the beginning of an attribute rank higer than matches at the end. ',
        alias="searchableAttributes",
    )
    user_data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="An object with custom data.  You can store up to 32kB as custom data. ",
        alias="userData",
    )
    custom_normalization: Optional[Dict[str, Dict[str, StrictStr]]] = Field(
        default=None,
        description="Characters and their normalized replacements. This overrides Algolia's default [normalization](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/normalization/). ",
        alias="customNormalization",
    )
    attribute_for_distinct: Optional[StrictStr] = Field(
        default=None,
        description="Attribute that should be used to establish groups of results. Attribute names are case-sensitive.  All records with the same value for this attribute are considered a group. You can combine `attributeForDistinct` with the `distinct` search parameter to control how many items per group are included in the search results.  If you want to use the same attribute also for faceting, use the `afterDistinct` modifier of the `attributesForFaceting` setting. This applies faceting _after_ deduplication, which will result in accurate facet counts. ",
        alias="attributeForDistinct",
    )
    attributes_to_retrieve: Optional[List[StrictStr]] = Field(
        default=None,
        description='Attributes to include in the API response.  To reduce the size of your response, you can retrieve only some of the attributes. Attribute names are case-sensitive.  - `*` retrieves all attributes, except attributes included in the `customRanking` and `unretrievableAttributes` settings. - To retrieve all attributes except a specific one, prefix the attribute with a dash and combine it with the `*`: `["*", "-ATTRIBUTE"]`. - The `objectID` attribute is always included. ',
        alias="attributesToRetrieve",
    )
    ranking: Optional[List[StrictStr]] = Field(
        default=None,
        description='Determines the order in which Algolia returns your results.  By default, each entry corresponds to a [ranking criteria](https://www.algolia.com/doc/guides/managing-results/relevance-overview/in-depth/ranking-criteria/). The tie-breaking algorithm sequentially applies each criterion in the order they\'re specified. If you configure a replica index for [sorting by an attribute](https://www.algolia.com/doc/guides/managing-results/refine-results/sorting/how-to/sort-by-attribute/), you put the sorting attribute at the top of the list.  **Modifiers**  - `asc("ATTRIBUTE")`.   Sort the index by the values of an attribute, in ascending order. - `desc("ATTRIBUTE")`.   Sort the index by the values of an attribute, in descending order.  Before you modify the default setting, you should test your changes in the dashboard, and by [A/B testing](https://www.algolia.com/doc/guides/ab-testing/what-is-ab-testing/). ',
    )
    custom_ranking: Optional[List[StrictStr]] = Field(
        default=None,
        description='Attributes to use as [custom ranking](https://www.algolia.com/doc/guides/managing-results/must-do/custom-ranking/). Attribute names are case-sensitive.  The custom ranking attributes decide which items are shown first if the other ranking criteria are equal.  Records with missing values for your selected custom ranking attributes are always sorted last. Boolean attributes are sorted based on their alphabetical order.  **Modifiers**  - `asc("ATTRIBUTE")`.   Sort the index by the values of an attribute, in ascending order.  - `desc("ATTRIBUTE")`.   Sort the index by the values of an attribute, in descending order.  If you use two or more custom ranking attributes, [reduce the precision](https://www.algolia.com/doc/guides/managing-results/must-do/custom-ranking/how-to/controlling-custom-ranking-metrics-precision/) of your first attributes, or the other attributes will never be applied. ',
        alias="customRanking",
    )
    relevancy_strictness: Optional[StrictInt] = Field(
        default=100,
        description="Relevancy threshold below which less relevant results aren't included in the results.  You can only set `relevancyStrictness` on [virtual replica indices](https://www.algolia.com/doc/guides/managing-results/refine-results/sorting/in-depth/replicas/#what-are-virtual-replicas). Use this setting to strike a balance between the relevance and number of returned results. ",
        alias="relevancyStrictness",
    )
    attributes_to_highlight: Optional[List[StrictStr]] = Field(
        default=None,
        description="Attributes to highlight.  By default, all searchable attributes are highlighted. Use `*` to highlight all attributes or use an empty array `[]` to turn off highlighting. Attribute names are case-sensitive.  With highlighting, strings that match the search query are surrounded by HTML tags defined by `highlightPreTag` and `highlightPostTag`. You can use this to visually highlight matching parts of a search query in your UI.  For more information, see [Highlighting and snippeting](https://www.algolia.com/doc/guides/building-search-ui/ui-and-ux-patterns/highlighting-snippeting/js/). ",
        alias="attributesToHighlight",
    )
    attributes_to_snippet: Optional[List[StrictStr]] = Field(
        default=None,
        description="Attributes for which to enable snippets. Attribute names are case-sensitive.  Snippets provide additional context to matched words. If you enable snippets, they include 10 words, including the matched word. The matched word will also be wrapped by HTML tags for highlighting. You can adjust the number of words with the following notation: `ATTRIBUTE:NUMBER`, where `NUMBER` is the number of words to be extracted. ",
        alias="attributesToSnippet",
    )
    highlight_pre_tag: Optional[StrictStr] = Field(
        default="<em>",
        description="HTML tag to insert before the highlighted parts in all highlighted results and snippets.",
        alias="highlightPreTag",
    )
    highlight_post_tag: Optional[StrictStr] = Field(
        default="</em>",
        description="HTML tag to insert after the highlighted parts in all highlighted results and snippets.",
        alias="highlightPostTag",
    )
    snippet_ellipsis_text: Optional[StrictStr] = Field(
        default="…",
        description="String used as an ellipsis indicator when a snippet is truncated.",
        alias="snippetEllipsisText",
    )
    restrict_highlight_and_snippet_arrays: Optional[StrictBool] = Field(
        default=False,
        description="Whether to restrict highlighting and snippeting to items that at least partially matched the search query. By default, all items are highlighted and snippeted. ",
        alias="restrictHighlightAndSnippetArrays",
    )
    hits_per_page: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(
        default=20, description="Number of hits per page.", alias="hitsPerPage"
    )
    min_word_sizefor1_typo: Optional[StrictInt] = Field(
        default=4,
        description="Minimum number of characters a word in the search query must contain to accept matches with [one typo](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/typo-tolerance/in-depth/configuring-typo-tolerance/#configuring-word-length-for-typos).",
        alias="minWordSizefor1Typo",
    )
    min_word_sizefor2_typos: Optional[StrictInt] = Field(
        default=8,
        description="Minimum number of characters a word in the search query must contain to accept matches with [two typos](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/typo-tolerance/in-depth/configuring-typo-tolerance/#configuring-word-length-for-typos).",
        alias="minWordSizefor2Typos",
    )
    typo_tolerance: Optional[TypoTolerance] = Field(default=None, alias="typoTolerance")
    allow_typos_on_numeric_tokens: Optional[StrictBool] = Field(
        default=True,
        description="Whether to allow typos on numbers in the search query.  Turn off this setting to reduce the number of irrelevant matches when searching in large sets of similar numbers. ",
        alias="allowTyposOnNumericTokens",
    )
    disable_typo_tolerance_on_attributes: Optional[List[StrictStr]] = Field(
        default=None,
        description="Attributes for which you want to turn off [typo tolerance](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/typo-tolerance/). Attribute names are case-sensitive.  Returning only exact matches can help when:  - [Searching in hyphenated attributes](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/typo-tolerance/how-to/how-to-search-in-hyphenated-attributes/). - Reducing the number of matches when you have too many.   This can happen with attributes that are long blocks of text, such as product descriptions.  Consider alternatives such as `disableTypoToleranceOnWords` or adding synonyms if your attributes have intentional unusual spellings that might look like typos. ",
        alias="disableTypoToleranceOnAttributes",
    )
    ignore_plurals: Optional[IgnorePlurals] = Field(default=None, alias="ignorePlurals")
    remove_stop_words: Optional[RemoveStopWords] = Field(
        default=None, alias="removeStopWords"
    )
    keep_diacritics_on_characters: Optional[StrictStr] = Field(
        default="",
        description="Characters for which diacritics should be preserved.  By default, Algolia removes diacritics from letters. For example, `é` becomes `e`. If this causes issues in your search, you can specify characters that should keep their diacritics. ",
        alias="keepDiacriticsOnCharacters",
    )
    query_languages: Optional[List[SupportedLanguage]] = Field(
        default=None,
        description="Languages for language-specific query processing steps such as plurals, stop-word removal, and word-detection dictionaries.  This setting sets a default list of languages used by the `removeStopWords` and `ignorePlurals` settings. This setting also sets a dictionary for word detection in the logogram-based [CJK](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/normalization/#normalization-for-logogram-based-languages-cjk) languages. To support this, you must place the CJK language **first**.  **You should always specify a query language.** If you don't specify an indexing language, the search engine uses all [supported languages](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/supported-languages/), or the languages you specified with the `ignorePlurals` or `removeStopWords` parameters. This can lead to unexpected search results. For more information, see [Language-specific configuration](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/language-specific-configurations/). ",
        alias="queryLanguages",
    )
    decompound_query: Optional[StrictBool] = Field(
        default=True,
        description="Whether to split compound words into their building blocks.  For more information, see [Word segmentation](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/handling-natural-languages-nlp/in-depth/language-specific-configurations/#splitting-compound-words). Word segmentation is supported for these languages: German, Dutch, Finnish, Swedish, and Norwegian. ",
        alias="decompoundQuery",
    )
    enable_rules: Optional[StrictBool] = Field(
        default=True, description="Whether to enable rules.", alias="enableRules"
    )
    enable_personalization: Optional[StrictBool] = Field(
        default=False,
        description="Whether to enable Personalization.",
        alias="enablePersonalization",
    )
    query_type: Optional[QueryType] = Field(default=None, alias="queryType")
    remove_words_if_no_results: Optional[RemoveWordsIfNoResults] = Field(
        default=None, alias="removeWordsIfNoResults"
    )
    mode: Optional[Mode] = None
    semantic_search: Optional[SemanticSearch] = Field(
        default=None, alias="semanticSearch"
    )
    advanced_syntax: Optional[StrictBool] = Field(
        default=False,
        description="Whether to support phrase matching and excluding words from search queries.  Use the `advancedSyntaxFeatures` parameter to control which feature is supported. ",
        alias="advancedSyntax",
    )
    optional_words: Optional[List[StrictStr]] = Field(
        default=None,
        description='Words that should be considered optional when found in the query.  By default, records must match all words in the search query to be included in the search results. Adding optional words can help to increase the number of search results by running an additional search query that doesn\'t include the optional words. For example, if the search query is "action video" and "video" is an optional word, the search engine runs two queries. One for "action video" and one for "action". Records that match all words are ranked higher.  For a search query with 4 or more words **and** all its words are optional, the number of matched words required for a record to be included in the search results increases for every 1,000 records:  - If `optionalWords` has less than 10 words, the required number of matched words increases by 1:   results 1 to 1,000 require 1 matched word, results 1,001 to 2000 need 2 matched words. - If `optionalWords` has 10 or more words, the number of required matched words increases by the number of optional words dividied by 5 (rounded down).   For example, with 18 optional words: results 1 to 1,000 require 1 matched word, results 1,001 to 2000 need 4 matched words.  For more information, see [Optional words](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/empty-or-insufficient-results/#creating-a-list-of-optional-words). ',
        alias="optionalWords",
    )
    disable_exact_on_attributes: Optional[List[StrictStr]] = Field(
        default=None,
        description="Searchable attributes for which you want to [turn off the Exact ranking criterion](https://www.algolia.com/doc/guides/managing-results/optimize-search-results/override-search-engine-defaults/in-depth/adjust-exact-settings/#turn-off-exact-for-some-attributes). Attribute names are case-sensitive.  This can be useful for attributes with long values, where the likelyhood of an exact match is high, such as product descriptions. Turning off the Exact ranking criterion for these attributes favors exact matching on other attributes. This reduces the impact of individual attributes with a lot of content on ranking. ",
        alias="disableExactOnAttributes",
    )
    exact_on_single_word_query: Optional[ExactOnSingleWordQuery] = Field(
        default=None, alias="exactOnSingleWordQuery"
    )
    alternatives_as_exact: Optional[List[AlternativesAsExact]] = Field(
        default=None,
        description='Alternatives of query words that should be considered as exact matches by the Exact ranking criterion.  - `ignorePlurals`.   Plurals and similar declensions added by the `ignorePlurals` setting are considered exact matches.  - `singleWordSynonym`.   Single-word synonyms, such as "NY/NYC" are considered exact matches.  - `multiWordsSynonym`.   Multi-word synonyms, such as "NY/New York" are considered exact matches. ',
        alias="alternativesAsExact",
    )
    advanced_syntax_features: Optional[List[AdvancedSyntaxFeatures]] = Field(
        default=None,
        description='Advanced search syntax features you want to support.  - `exactPhrase`.   Phrases in quotes must match exactly.   For example, `sparkly blue "iPhone case"` only returns records with the exact string "iPhone case".  - `excludeWords`.   Query words prefixed with a `-` must not occur in a record.   For example, `search -engine` matches records that contain "search" but not "engine".  This setting only has an effect if `advancedSyntax` is true. ',
        alias="advancedSyntaxFeatures",
    )
    distinct: Optional[Distinct] = None
    replace_synonyms_in_highlight: Optional[StrictBool] = Field(
        default=False,
        description='Whether to replace a highlighted word with the matched synonym.  By default, the original words are highlighted even if a synonym matches. For example, with `home` as a synonym for `house` and a search for `home`, records matching either "home" or "house" are included in the search results, and either "home" or "house" are highlighted.  With `replaceSynonymsInHighlight` set to `true`, a search for `home` still matches the same records, but all occurences of "house" are replaced by "home" in the highlighted response. ',
        alias="replaceSynonymsInHighlight",
    )
    min_proximity: Optional[Annotated[int, Field(le=7, strict=True, ge=1)]] = Field(
        default=1,
        description="Minimum proximity score for two matching words.  This adjusts the [Proximity ranking criterion](https://www.algolia.com/doc/guides/managing-results/relevance-overview/in-depth/ranking-criteria/#proximity) by equally scoring matches that are farther apart.  For example, if `minProximity` is 2, neighboring matches and matches with one word between them would have the same score. ",
        alias="minProximity",
    )
    response_fields: Optional[List[StrictStr]] = Field(
        default=None,
        description="Properties to include in the API response of `search` and `browse` requests.  By default, all response properties are included. To reduce the response size, you can select, which attributes should be included.  You can't exclude these properties: `message`, `warning`, `cursor`, `serverUsed`, `indexUsed`, `abTestVariantID`, `parsedQuery`, or any property triggered by the `getRankingInfo` parameter.  Don't exclude properties that you might need in your search UI. ",
        alias="responseFields",
    )
    max_facet_hits: Optional[Annotated[int, Field(le=100, strict=True)]] = Field(
        default=10,
        description="Maximum number of facet values to return when [searching for facet values](https://www.algolia.com/doc/guides/managing-results/refine-results/faceting/#search-for-facet-values).",
        alias="maxFacetHits",
    )
    max_values_per_facet: Optional[Annotated[int, Field(le=1000, strict=True)]] = Field(
        default=100,
        description="Maximum number of facet values to return for each facet.",
        alias="maxValuesPerFacet",
    )
    sort_facet_values_by: Optional[StrictStr] = Field(
        default="count",
        description="Order in which to retrieve facet values.  - `count`.   Facet values are retrieved by decreasing count.   The count is the number of matching records containing this facet value.  - `alpha`.   Retrieve facet values alphabetically.  This setting doesn't influence how facet values are displayed in your UI (see `renderingContent`). For more information, see [facet value display](https://www.algolia.com/doc/guides/building-search-ui/ui-and-ux-patterns/facet-display/js/). ",
        alias="sortFacetValuesBy",
    )
    attribute_criteria_computed_by_min_proximity: Optional[StrictBool] = Field(
        default=False,
        description="Whether the best matching attribute should be determined by minimum proximity.  This setting only affects ranking if the Attribute ranking criterion comes before Proximity in the `ranking` setting. If true, the best matching attribute is selected based on the minimum proximity of multiple matches. Otherwise, the best matching attribute is determined by the order in the `searchableAttributes` setting. ",
        alias="attributeCriteriaComputedByMinProximity",
    )
    rendering_content: Optional[RenderingContent] = Field(
        default=None, alias="renderingContent"
    )
    enable_re_ranking: Optional[StrictBool] = Field(
        default=True,
        description="Whether this search will use [Dynamic Re-Ranking](https://www.algolia.com/doc/guides/algolia-ai/re-ranking/).  This setting only has an effect if you activated Dynamic Re-Ranking for this index in the Algolia dashboard. ",
        alias="enableReRanking",
    )
    re_ranking_apply_filter: Optional[ReRankingApplyFilter] = Field(
        default=None, alias="reRankingApplyFilter"
    )

    model_config = ConfigDict(
        use_enum_values=True, populate_by_name=True, validate_assignment=True
    )

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IndexSettings from a JSON string"""
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
        if self.typo_tolerance:
            _dict["typoTolerance"] = self.typo_tolerance.to_dict()
        if self.ignore_plurals:
            _dict["ignorePlurals"] = self.ignore_plurals.to_dict()
        if self.remove_stop_words:
            _dict["removeStopWords"] = self.remove_stop_words.to_dict()
        if self.semantic_search:
            _dict["semanticSearch"] = self.semantic_search.to_dict()
        if self.distinct:
            _dict["distinct"] = self.distinct.to_dict()
        if self.rendering_content:
            _dict["renderingContent"] = self.rendering_content.to_dict()
        if self.re_ranking_apply_filter:
            _dict["reRankingApplyFilter"] = self.re_ranking_apply_filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IndexSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "attributesForFaceting": obj.get("attributesForFaceting"),
                "replicas": obj.get("replicas"),
                "virtual": obj.get("virtual"),
                "paginationLimitedTo": obj.get("paginationLimitedTo"),
                "unretrievableAttributes": obj.get("unretrievableAttributes"),
                "disableTypoToleranceOnWords": obj.get("disableTypoToleranceOnWords"),
                "attributesToTransliterate": obj.get("attributesToTransliterate"),
                "camelCaseAttributes": obj.get("camelCaseAttributes"),
                "decompoundedAttributes": obj.get("decompoundedAttributes"),
                "indexLanguages": obj.get("indexLanguages"),
                "disablePrefixOnAttributes": obj.get("disablePrefixOnAttributes"),
                "allowCompressionOfIntegerArray": obj.get(
                    "allowCompressionOfIntegerArray"
                ),
                "numericAttributesForFiltering": obj.get(
                    "numericAttributesForFiltering"
                ),
                "separatorsToIndex": obj.get("separatorsToIndex"),
                "searchableAttributes": obj.get("searchableAttributes"),
                "userData": obj.get("userData"),
                "customNormalization": obj.get("customNormalization"),
                "attributeForDistinct": obj.get("attributeForDistinct"),
                "attributesToRetrieve": obj.get("attributesToRetrieve"),
                "ranking": obj.get("ranking"),
                "customRanking": obj.get("customRanking"),
                "relevancyStrictness": obj.get("relevancyStrictness"),
                "attributesToHighlight": obj.get("attributesToHighlight"),
                "attributesToSnippet": obj.get("attributesToSnippet"),
                "highlightPreTag": obj.get("highlightPreTag"),
                "highlightPostTag": obj.get("highlightPostTag"),
                "snippetEllipsisText": obj.get("snippetEllipsisText"),
                "restrictHighlightAndSnippetArrays": obj.get(
                    "restrictHighlightAndSnippetArrays"
                ),
                "hitsPerPage": obj.get("hitsPerPage"),
                "minWordSizefor1Typo": obj.get("minWordSizefor1Typo"),
                "minWordSizefor2Typos": obj.get("minWordSizefor2Typos"),
                "typoTolerance": (
                    TypoTolerance.from_dict(obj.get("typoTolerance"))
                    if obj.get("typoTolerance") is not None
                    else None
                ),
                "allowTyposOnNumericTokens": obj.get("allowTyposOnNumericTokens"),
                "disableTypoToleranceOnAttributes": obj.get(
                    "disableTypoToleranceOnAttributes"
                ),
                "ignorePlurals": (
                    IgnorePlurals.from_dict(obj.get("ignorePlurals"))
                    if obj.get("ignorePlurals") is not None
                    else None
                ),
                "removeStopWords": (
                    RemoveStopWords.from_dict(obj.get("removeStopWords"))
                    if obj.get("removeStopWords") is not None
                    else None
                ),
                "keepDiacriticsOnCharacters": obj.get("keepDiacriticsOnCharacters"),
                "queryLanguages": obj.get("queryLanguages"),
                "decompoundQuery": obj.get("decompoundQuery"),
                "enableRules": obj.get("enableRules"),
                "enablePersonalization": obj.get("enablePersonalization"),
                "queryType": obj.get("queryType"),
                "removeWordsIfNoResults": obj.get("removeWordsIfNoResults"),
                "mode": obj.get("mode"),
                "semanticSearch": (
                    SemanticSearch.from_dict(obj.get("semanticSearch"))
                    if obj.get("semanticSearch") is not None
                    else None
                ),
                "advancedSyntax": obj.get("advancedSyntax"),
                "optionalWords": obj.get("optionalWords"),
                "disableExactOnAttributes": obj.get("disableExactOnAttributes"),
                "exactOnSingleWordQuery": obj.get("exactOnSingleWordQuery"),
                "alternativesAsExact": obj.get("alternativesAsExact"),
                "advancedSyntaxFeatures": obj.get("advancedSyntaxFeatures"),
                "distinct": (
                    Distinct.from_dict(obj.get("distinct"))
                    if obj.get("distinct") is not None
                    else None
                ),
                "replaceSynonymsInHighlight": obj.get("replaceSynonymsInHighlight"),
                "minProximity": obj.get("minProximity"),
                "responseFields": obj.get("responseFields"),
                "maxFacetHits": obj.get("maxFacetHits"),
                "maxValuesPerFacet": obj.get("maxValuesPerFacet"),
                "sortFacetValuesBy": obj.get("sortFacetValuesBy"),
                "attributeCriteriaComputedByMinProximity": obj.get(
                    "attributeCriteriaComputedByMinProximity"
                ),
                "renderingContent": (
                    RenderingContent.from_dict(obj.get("renderingContent"))
                    if obj.get("renderingContent") is not None
                    else None
                ),
                "enableReRanking": obj.get("enableReRanking"),
                "reRankingApplyFilter": (
                    ReRankingApplyFilter.from_dict(obj.get("reRankingApplyFilter"))
                    if obj.get("reRankingApplyFilter") is not None
                    else None
                ),
            }
        )
        return _obj
