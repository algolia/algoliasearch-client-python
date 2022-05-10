package com.algolia.model.search;

import com.google.gson.annotations.SerializedName;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/** IndexSettingsAsSearchParams */
public class IndexSettingsAsSearchParams {

  @SerializedName("searchableAttributes")
  private List<String> searchableAttributes = null;

  @SerializedName("attributesForFaceting")
  private List<String> attributesForFaceting = null;

  @SerializedName("unretrievableAttributes")
  private List<String> unretrievableAttributes = null;

  @SerializedName("attributesToRetrieve")
  private List<String> attributesToRetrieve = null;

  @SerializedName("restrictSearchableAttributes")
  private List<String> restrictSearchableAttributes = null;

  @SerializedName("ranking")
  private List<String> ranking = null;

  @SerializedName("customRanking")
  private List<String> customRanking = null;

  @SerializedName("relevancyStrictness")
  private Integer relevancyStrictness = 100;

  @SerializedName("attributesToHighlight")
  private List<String> attributesToHighlight = null;

  @SerializedName("attributesToSnippet")
  private List<String> attributesToSnippet = null;

  @SerializedName("highlightPreTag")
  private String highlightPreTag = "<em>";

  @SerializedName("highlightPostTag")
  private String highlightPostTag = "</em>";

  @SerializedName("snippetEllipsisText")
  private String snippetEllipsisText = "…";

  @SerializedName("restrictHighlightAndSnippetArrays")
  private Boolean restrictHighlightAndSnippetArrays = false;

  @SerializedName("hitsPerPage")
  private Integer hitsPerPage = 20;

  @SerializedName("minWordSizefor1Typo")
  private Integer minWordSizefor1Typo = 4;

  @SerializedName("minWordSizefor2Typos")
  private Integer minWordSizefor2Typos = 8;

  @SerializedName("typoTolerance")
  private TypoTolerance typoTolerance = TypoTolerance.TRUE;

  @SerializedName("allowTyposOnNumericTokens")
  private Boolean allowTyposOnNumericTokens = true;

  @SerializedName("disableTypoToleranceOnAttributes")
  private List<String> disableTypoToleranceOnAttributes = null;

  @SerializedName("separatorsToIndex")
  private String separatorsToIndex = "";

  @SerializedName("ignorePlurals")
  private String ignorePlurals = "false";

  @SerializedName("removeStopWords")
  private String removeStopWords = "false";

  @SerializedName("keepDiacriticsOnCharacters")
  private String keepDiacriticsOnCharacters = "";

  @SerializedName("queryLanguages")
  private List<String> queryLanguages = null;

  @SerializedName("decompoundQuery")
  private Boolean decompoundQuery = true;

  @SerializedName("enableRules")
  private Boolean enableRules = true;

  @SerializedName("enablePersonalization")
  private Boolean enablePersonalization = false;

  @SerializedName("queryType")
  private QueryType queryType = QueryType.PREFIX_LAST;

  @SerializedName("removeWordsIfNoResults")
  private RemoveWordsIfNoResults removeWordsIfNoResults =
    RemoveWordsIfNoResults.NONE;

  @SerializedName("advancedSyntax")
  private Boolean advancedSyntax = false;

  @SerializedName("optionalWords")
  private List<String> optionalWords = null;

  @SerializedName("disableExactOnAttributes")
  private List<String> disableExactOnAttributes = null;

  @SerializedName("exactOnSingleWordQuery")
  private ExactOnSingleWordQuery exactOnSingleWordQuery =
    ExactOnSingleWordQuery.ATTRIBUTE;

  @SerializedName("alternativesAsExact")
  private List<AlternativesAsExact> alternativesAsExact = null;

  @SerializedName("advancedSyntaxFeatures")
  private List<AdvancedSyntaxFeatures> advancedSyntaxFeatures = null;

  @SerializedName("distinct")
  private Integer distinct = 0;

  @SerializedName("synonyms")
  private Boolean synonyms = true;

  @SerializedName("replaceSynonymsInHighlight")
  private Boolean replaceSynonymsInHighlight = false;

  @SerializedName("minProximity")
  private Integer minProximity = 1;

  @SerializedName("responseFields")
  private List<String> responseFields = null;

  @SerializedName("maxFacetHits")
  private Integer maxFacetHits = 10;

  @SerializedName("attributeCriteriaComputedByMinProximity")
  private Boolean attributeCriteriaComputedByMinProximity = false;

  @SerializedName("renderingContent")
  private Object renderingContent = new Object();

  public IndexSettingsAsSearchParams setSearchableAttributes(
    List<String> searchableAttributes
  ) {
    this.searchableAttributes = searchableAttributes;
    return this;
  }

  public IndexSettingsAsSearchParams addSearchableAttributes(
    String searchableAttributesItem
  ) {
    if (this.searchableAttributes == null) {
      this.searchableAttributes = new ArrayList<>();
    }
    this.searchableAttributes.add(searchableAttributesItem);
    return this;
  }

  /**
   * The complete list of attributes used for searching.
   *
   * @return searchableAttributes
   */
  @javax.annotation.Nullable
  public List<String> getSearchableAttributes() {
    return searchableAttributes;
  }

  public IndexSettingsAsSearchParams setAttributesForFaceting(
    List<String> attributesForFaceting
  ) {
    this.attributesForFaceting = attributesForFaceting;
    return this;
  }

  public IndexSettingsAsSearchParams addAttributesForFaceting(
    String attributesForFacetingItem
  ) {
    if (this.attributesForFaceting == null) {
      this.attributesForFaceting = new ArrayList<>();
    }
    this.attributesForFaceting.add(attributesForFacetingItem);
    return this;
  }

  /**
   * The complete list of attributes that will be used for faceting.
   *
   * @return attributesForFaceting
   */
  @javax.annotation.Nullable
  public List<String> getAttributesForFaceting() {
    return attributesForFaceting;
  }

  public IndexSettingsAsSearchParams setUnretrievableAttributes(
    List<String> unretrievableAttributes
  ) {
    this.unretrievableAttributes = unretrievableAttributes;
    return this;
  }

  public IndexSettingsAsSearchParams addUnretrievableAttributes(
    String unretrievableAttributesItem
  ) {
    if (this.unretrievableAttributes == null) {
      this.unretrievableAttributes = new ArrayList<>();
    }
    this.unretrievableAttributes.add(unretrievableAttributesItem);
    return this;
  }

  /**
   * List of attributes that can't be retrieved at query time.
   *
   * @return unretrievableAttributes
   */
  @javax.annotation.Nullable
  public List<String> getUnretrievableAttributes() {
    return unretrievableAttributes;
  }

  public IndexSettingsAsSearchParams setAttributesToRetrieve(
    List<String> attributesToRetrieve
  ) {
    this.attributesToRetrieve = attributesToRetrieve;
    return this;
  }

  public IndexSettingsAsSearchParams addAttributesToRetrieve(
    String attributesToRetrieveItem
  ) {
    if (this.attributesToRetrieve == null) {
      this.attributesToRetrieve = new ArrayList<>();
    }
    this.attributesToRetrieve.add(attributesToRetrieveItem);
    return this;
  }

  /**
   * This parameter controls which attributes to retrieve and which not to retrieve.
   *
   * @return attributesToRetrieve
   */
  @javax.annotation.Nullable
  public List<String> getAttributesToRetrieve() {
    return attributesToRetrieve;
  }

  public IndexSettingsAsSearchParams setRestrictSearchableAttributes(
    List<String> restrictSearchableAttributes
  ) {
    this.restrictSearchableAttributes = restrictSearchableAttributes;
    return this;
  }

  public IndexSettingsAsSearchParams addRestrictSearchableAttributes(
    String restrictSearchableAttributesItem
  ) {
    if (this.restrictSearchableAttributes == null) {
      this.restrictSearchableAttributes = new ArrayList<>();
    }
    this.restrictSearchableAttributes.add(restrictSearchableAttributesItem);
    return this;
  }

  /**
   * Restricts a given query to look in only a subset of your searchable attributes.
   *
   * @return restrictSearchableAttributes
   */
  @javax.annotation.Nullable
  public List<String> getRestrictSearchableAttributes() {
    return restrictSearchableAttributes;
  }

  public IndexSettingsAsSearchParams setRanking(List<String> ranking) {
    this.ranking = ranking;
    return this;
  }

  public IndexSettingsAsSearchParams addRanking(String rankingItem) {
    if (this.ranking == null) {
      this.ranking = new ArrayList<>();
    }
    this.ranking.add(rankingItem);
    return this;
  }

  /**
   * Controls how Algolia should sort your results.
   *
   * @return ranking
   */
  @javax.annotation.Nullable
  public List<String> getRanking() {
    return ranking;
  }

  public IndexSettingsAsSearchParams setCustomRanking(
    List<String> customRanking
  ) {
    this.customRanking = customRanking;
    return this;
  }

  public IndexSettingsAsSearchParams addCustomRanking(
    String customRankingItem
  ) {
    if (this.customRanking == null) {
      this.customRanking = new ArrayList<>();
    }
    this.customRanking.add(customRankingItem);
    return this;
  }

  /**
   * Specifies the custom ranking criterion.
   *
   * @return customRanking
   */
  @javax.annotation.Nullable
  public List<String> getCustomRanking() {
    return customRanking;
  }

  public IndexSettingsAsSearchParams setRelevancyStrictness(
    Integer relevancyStrictness
  ) {
    this.relevancyStrictness = relevancyStrictness;
    return this;
  }

  /**
   * Controls the relevancy threshold below which less relevant results aren't included in the
   * results.
   *
   * @return relevancyStrictness
   */
  @javax.annotation.Nullable
  public Integer getRelevancyStrictness() {
    return relevancyStrictness;
  }

  public IndexSettingsAsSearchParams setAttributesToHighlight(
    List<String> attributesToHighlight
  ) {
    this.attributesToHighlight = attributesToHighlight;
    return this;
  }

  public IndexSettingsAsSearchParams addAttributesToHighlight(
    String attributesToHighlightItem
  ) {
    if (this.attributesToHighlight == null) {
      this.attributesToHighlight = new ArrayList<>();
    }
    this.attributesToHighlight.add(attributesToHighlightItem);
    return this;
  }

  /**
   * List of attributes to highlight.
   *
   * @return attributesToHighlight
   */
  @javax.annotation.Nullable
  public List<String> getAttributesToHighlight() {
    return attributesToHighlight;
  }

  public IndexSettingsAsSearchParams setAttributesToSnippet(
    List<String> attributesToSnippet
  ) {
    this.attributesToSnippet = attributesToSnippet;
    return this;
  }

  public IndexSettingsAsSearchParams addAttributesToSnippet(
    String attributesToSnippetItem
  ) {
    if (this.attributesToSnippet == null) {
      this.attributesToSnippet = new ArrayList<>();
    }
    this.attributesToSnippet.add(attributesToSnippetItem);
    return this;
  }

  /**
   * List of attributes to snippet, with an optional maximum number of words to snippet.
   *
   * @return attributesToSnippet
   */
  @javax.annotation.Nullable
  public List<String> getAttributesToSnippet() {
    return attributesToSnippet;
  }

  public IndexSettingsAsSearchParams setHighlightPreTag(
    String highlightPreTag
  ) {
    this.highlightPreTag = highlightPreTag;
    return this;
  }

  /**
   * The HTML string to insert before the highlighted parts in all highlight and snippet results.
   *
   * @return highlightPreTag
   */
  @javax.annotation.Nullable
  public String getHighlightPreTag() {
    return highlightPreTag;
  }

  public IndexSettingsAsSearchParams setHighlightPostTag(
    String highlightPostTag
  ) {
    this.highlightPostTag = highlightPostTag;
    return this;
  }

  /**
   * The HTML string to insert after the highlighted parts in all highlight and snippet results.
   *
   * @return highlightPostTag
   */
  @javax.annotation.Nullable
  public String getHighlightPostTag() {
    return highlightPostTag;
  }

  public IndexSettingsAsSearchParams setSnippetEllipsisText(
    String snippetEllipsisText
  ) {
    this.snippetEllipsisText = snippetEllipsisText;
    return this;
  }

  /**
   * String used as an ellipsis indicator when a snippet is truncated.
   *
   * @return snippetEllipsisText
   */
  @javax.annotation.Nullable
  public String getSnippetEllipsisText() {
    return snippetEllipsisText;
  }

  public IndexSettingsAsSearchParams setRestrictHighlightAndSnippetArrays(
    Boolean restrictHighlightAndSnippetArrays
  ) {
    this.restrictHighlightAndSnippetArrays = restrictHighlightAndSnippetArrays;
    return this;
  }

  /**
   * Restrict highlighting and snippeting to items that matched the query.
   *
   * @return restrictHighlightAndSnippetArrays
   */
  @javax.annotation.Nullable
  public Boolean getRestrictHighlightAndSnippetArrays() {
    return restrictHighlightAndSnippetArrays;
  }

  public IndexSettingsAsSearchParams setHitsPerPage(Integer hitsPerPage) {
    this.hitsPerPage = hitsPerPage;
    return this;
  }

  /**
   * Set the number of hits per page.
   *
   * @return hitsPerPage
   */
  @javax.annotation.Nullable
  public Integer getHitsPerPage() {
    return hitsPerPage;
  }

  public IndexSettingsAsSearchParams setMinWordSizefor1Typo(
    Integer minWordSizefor1Typo
  ) {
    this.minWordSizefor1Typo = minWordSizefor1Typo;
    return this;
  }

  /**
   * Minimum number of characters a word in the query string must contain to accept matches with 1
   * typo.
   *
   * @return minWordSizefor1Typo
   */
  @javax.annotation.Nullable
  public Integer getMinWordSizefor1Typo() {
    return minWordSizefor1Typo;
  }

  public IndexSettingsAsSearchParams setMinWordSizefor2Typos(
    Integer minWordSizefor2Typos
  ) {
    this.minWordSizefor2Typos = minWordSizefor2Typos;
    return this;
  }

  /**
   * Minimum number of characters a word in the query string must contain to accept matches with 2
   * typos.
   *
   * @return minWordSizefor2Typos
   */
  @javax.annotation.Nullable
  public Integer getMinWordSizefor2Typos() {
    return minWordSizefor2Typos;
  }

  public IndexSettingsAsSearchParams setTypoTolerance(
    TypoTolerance typoTolerance
  ) {
    this.typoTolerance = typoTolerance;
    return this;
  }

  /**
   * Get typoTolerance
   *
   * @return typoTolerance
   */
  @javax.annotation.Nullable
  public TypoTolerance getTypoTolerance() {
    return typoTolerance;
  }

  public IndexSettingsAsSearchParams setAllowTyposOnNumericTokens(
    Boolean allowTyposOnNumericTokens
  ) {
    this.allowTyposOnNumericTokens = allowTyposOnNumericTokens;
    return this;
  }

  /**
   * Whether to allow typos on numbers (\"numeric tokens\") in the query string.
   *
   * @return allowTyposOnNumericTokens
   */
  @javax.annotation.Nullable
  public Boolean getAllowTyposOnNumericTokens() {
    return allowTyposOnNumericTokens;
  }

  public IndexSettingsAsSearchParams setDisableTypoToleranceOnAttributes(
    List<String> disableTypoToleranceOnAttributes
  ) {
    this.disableTypoToleranceOnAttributes = disableTypoToleranceOnAttributes;
    return this;
  }

  public IndexSettingsAsSearchParams addDisableTypoToleranceOnAttributes(
    String disableTypoToleranceOnAttributesItem
  ) {
    if (this.disableTypoToleranceOnAttributes == null) {
      this.disableTypoToleranceOnAttributes = new ArrayList<>();
    }
    this.disableTypoToleranceOnAttributes.add(
        disableTypoToleranceOnAttributesItem
      );
    return this;
  }

  /**
   * List of attributes on which you want to disable typo tolerance.
   *
   * @return disableTypoToleranceOnAttributes
   */
  @javax.annotation.Nullable
  public List<String> getDisableTypoToleranceOnAttributes() {
    return disableTypoToleranceOnAttributes;
  }

  public IndexSettingsAsSearchParams setSeparatorsToIndex(
    String separatorsToIndex
  ) {
    this.separatorsToIndex = separatorsToIndex;
    return this;
  }

  /**
   * Control which separators are indexed.
   *
   * @return separatorsToIndex
   */
  @javax.annotation.Nullable
  public String getSeparatorsToIndex() {
    return separatorsToIndex;
  }

  public IndexSettingsAsSearchParams setIgnorePlurals(String ignorePlurals) {
    this.ignorePlurals = ignorePlurals;
    return this;
  }

  /**
   * Treats singular, plurals, and other forms of declensions as matching terms.
   *
   * @return ignorePlurals
   */
  @javax.annotation.Nullable
  public String getIgnorePlurals() {
    return ignorePlurals;
  }

  public IndexSettingsAsSearchParams setRemoveStopWords(
    String removeStopWords
  ) {
    this.removeStopWords = removeStopWords;
    return this;
  }

  /**
   * Removes stop (common) words from the query before executing it.
   *
   * @return removeStopWords
   */
  @javax.annotation.Nullable
  public String getRemoveStopWords() {
    return removeStopWords;
  }

  public IndexSettingsAsSearchParams setKeepDiacriticsOnCharacters(
    String keepDiacriticsOnCharacters
  ) {
    this.keepDiacriticsOnCharacters = keepDiacriticsOnCharacters;
    return this;
  }

  /**
   * List of characters that the engine shouldn't automatically normalize.
   *
   * @return keepDiacriticsOnCharacters
   */
  @javax.annotation.Nullable
  public String getKeepDiacriticsOnCharacters() {
    return keepDiacriticsOnCharacters;
  }

  public IndexSettingsAsSearchParams setQueryLanguages(
    List<String> queryLanguages
  ) {
    this.queryLanguages = queryLanguages;
    return this;
  }

  public IndexSettingsAsSearchParams addQueryLanguages(
    String queryLanguagesItem
  ) {
    if (this.queryLanguages == null) {
      this.queryLanguages = new ArrayList<>();
    }
    this.queryLanguages.add(queryLanguagesItem);
    return this;
  }

  /**
   * Sets the languages to be used by language-specific settings and functionalities such as
   * ignorePlurals, removeStopWords, and CJK word-detection.
   *
   * @return queryLanguages
   */
  @javax.annotation.Nullable
  public List<String> getQueryLanguages() {
    return queryLanguages;
  }

  public IndexSettingsAsSearchParams setDecompoundQuery(
    Boolean decompoundQuery
  ) {
    this.decompoundQuery = decompoundQuery;
    return this;
  }

  /**
   * Splits compound words into their composing atoms in the query.
   *
   * @return decompoundQuery
   */
  @javax.annotation.Nullable
  public Boolean getDecompoundQuery() {
    return decompoundQuery;
  }

  public IndexSettingsAsSearchParams setEnableRules(Boolean enableRules) {
    this.enableRules = enableRules;
    return this;
  }

  /**
   * Whether Rules should be globally enabled.
   *
   * @return enableRules
   */
  @javax.annotation.Nullable
  public Boolean getEnableRules() {
    return enableRules;
  }

  public IndexSettingsAsSearchParams setEnablePersonalization(
    Boolean enablePersonalization
  ) {
    this.enablePersonalization = enablePersonalization;
    return this;
  }

  /**
   * Enable the Personalization feature.
   *
   * @return enablePersonalization
   */
  @javax.annotation.Nullable
  public Boolean getEnablePersonalization() {
    return enablePersonalization;
  }

  public IndexSettingsAsSearchParams setQueryType(QueryType queryType) {
    this.queryType = queryType;
    return this;
  }

  /**
   * Get queryType
   *
   * @return queryType
   */
  @javax.annotation.Nullable
  public QueryType getQueryType() {
    return queryType;
  }

  public IndexSettingsAsSearchParams setRemoveWordsIfNoResults(
    RemoveWordsIfNoResults removeWordsIfNoResults
  ) {
    this.removeWordsIfNoResults = removeWordsIfNoResults;
    return this;
  }

  /**
   * Get removeWordsIfNoResults
   *
   * @return removeWordsIfNoResults
   */
  @javax.annotation.Nullable
  public RemoveWordsIfNoResults getRemoveWordsIfNoResults() {
    return removeWordsIfNoResults;
  }

  public IndexSettingsAsSearchParams setAdvancedSyntax(Boolean advancedSyntax) {
    this.advancedSyntax = advancedSyntax;
    return this;
  }

  /**
   * Enables the advanced query syntax.
   *
   * @return advancedSyntax
   */
  @javax.annotation.Nullable
  public Boolean getAdvancedSyntax() {
    return advancedSyntax;
  }

  public IndexSettingsAsSearchParams setOptionalWords(
    List<String> optionalWords
  ) {
    this.optionalWords = optionalWords;
    return this;
  }

  public IndexSettingsAsSearchParams addOptionalWords(
    String optionalWordsItem
  ) {
    if (this.optionalWords == null) {
      this.optionalWords = new ArrayList<>();
    }
    this.optionalWords.add(optionalWordsItem);
    return this;
  }

  /**
   * A list of words that should be considered as optional when found in the query.
   *
   * @return optionalWords
   */
  @javax.annotation.Nullable
  public List<String> getOptionalWords() {
    return optionalWords;
  }

  public IndexSettingsAsSearchParams setDisableExactOnAttributes(
    List<String> disableExactOnAttributes
  ) {
    this.disableExactOnAttributes = disableExactOnAttributes;
    return this;
  }

  public IndexSettingsAsSearchParams addDisableExactOnAttributes(
    String disableExactOnAttributesItem
  ) {
    if (this.disableExactOnAttributes == null) {
      this.disableExactOnAttributes = new ArrayList<>();
    }
    this.disableExactOnAttributes.add(disableExactOnAttributesItem);
    return this;
  }

  /**
   * List of attributes on which you want to disable the exact ranking criterion.
   *
   * @return disableExactOnAttributes
   */
  @javax.annotation.Nullable
  public List<String> getDisableExactOnAttributes() {
    return disableExactOnAttributes;
  }

  public IndexSettingsAsSearchParams setExactOnSingleWordQuery(
    ExactOnSingleWordQuery exactOnSingleWordQuery
  ) {
    this.exactOnSingleWordQuery = exactOnSingleWordQuery;
    return this;
  }

  /**
   * Get exactOnSingleWordQuery
   *
   * @return exactOnSingleWordQuery
   */
  @javax.annotation.Nullable
  public ExactOnSingleWordQuery getExactOnSingleWordQuery() {
    return exactOnSingleWordQuery;
  }

  public IndexSettingsAsSearchParams setAlternativesAsExact(
    List<AlternativesAsExact> alternativesAsExact
  ) {
    this.alternativesAsExact = alternativesAsExact;
    return this;
  }

  public IndexSettingsAsSearchParams addAlternativesAsExact(
    AlternativesAsExact alternativesAsExactItem
  ) {
    if (this.alternativesAsExact == null) {
      this.alternativesAsExact = new ArrayList<>();
    }
    this.alternativesAsExact.add(alternativesAsExactItem);
    return this;
  }

  /**
   * List of alternatives that should be considered an exact match by the exact ranking criterion.
   *
   * @return alternativesAsExact
   */
  @javax.annotation.Nullable
  public List<AlternativesAsExact> getAlternativesAsExact() {
    return alternativesAsExact;
  }

  public IndexSettingsAsSearchParams setAdvancedSyntaxFeatures(
    List<AdvancedSyntaxFeatures> advancedSyntaxFeatures
  ) {
    this.advancedSyntaxFeatures = advancedSyntaxFeatures;
    return this;
  }

  public IndexSettingsAsSearchParams addAdvancedSyntaxFeatures(
    AdvancedSyntaxFeatures advancedSyntaxFeaturesItem
  ) {
    if (this.advancedSyntaxFeatures == null) {
      this.advancedSyntaxFeatures = new ArrayList<>();
    }
    this.advancedSyntaxFeatures.add(advancedSyntaxFeaturesItem);
    return this;
  }

  /**
   * Allows you to specify which advanced syntax features are active when ‘advancedSyntax' is
   * enabled.
   *
   * @return advancedSyntaxFeatures
   */
  @javax.annotation.Nullable
  public List<AdvancedSyntaxFeatures> getAdvancedSyntaxFeatures() {
    return advancedSyntaxFeatures;
  }

  public IndexSettingsAsSearchParams setDistinct(Integer distinct) {
    this.distinct = distinct;
    return this;
  }

  /**
   * Enables de-duplication or grouping of results. minimum: 0 maximum: 4
   *
   * @return distinct
   */
  @javax.annotation.Nullable
  public Integer getDistinct() {
    return distinct;
  }

  public IndexSettingsAsSearchParams setSynonyms(Boolean synonyms) {
    this.synonyms = synonyms;
    return this;
  }

  /**
   * Whether to take into account an index's synonyms for a particular search.
   *
   * @return synonyms
   */
  @javax.annotation.Nullable
  public Boolean getSynonyms() {
    return synonyms;
  }

  public IndexSettingsAsSearchParams setReplaceSynonymsInHighlight(
    Boolean replaceSynonymsInHighlight
  ) {
    this.replaceSynonymsInHighlight = replaceSynonymsInHighlight;
    return this;
  }

  /**
   * Whether to highlight and snippet the original word that matches the synonym or the synonym
   * itself.
   *
   * @return replaceSynonymsInHighlight
   */
  @javax.annotation.Nullable
  public Boolean getReplaceSynonymsInHighlight() {
    return replaceSynonymsInHighlight;
  }

  public IndexSettingsAsSearchParams setMinProximity(Integer minProximity) {
    this.minProximity = minProximity;
    return this;
  }

  /**
   * Precision of the proximity ranking criterion. minimum: 1 maximum: 7
   *
   * @return minProximity
   */
  @javax.annotation.Nullable
  public Integer getMinProximity() {
    return minProximity;
  }

  public IndexSettingsAsSearchParams setResponseFields(
    List<String> responseFields
  ) {
    this.responseFields = responseFields;
    return this;
  }

  public IndexSettingsAsSearchParams addResponseFields(
    String responseFieldsItem
  ) {
    if (this.responseFields == null) {
      this.responseFields = new ArrayList<>();
    }
    this.responseFields.add(responseFieldsItem);
    return this;
  }

  /**
   * Choose which fields to return in the API response. This parameters applies to search and browse
   * queries.
   *
   * @return responseFields
   */
  @javax.annotation.Nullable
  public List<String> getResponseFields() {
    return responseFields;
  }

  public IndexSettingsAsSearchParams setMaxFacetHits(Integer maxFacetHits) {
    this.maxFacetHits = maxFacetHits;
    return this;
  }

  /**
   * Maximum number of facet hits to return during a search for facet values. For performance
   * reasons, the maximum allowed number of returned values is 100. maximum: 100
   *
   * @return maxFacetHits
   */
  @javax.annotation.Nullable
  public Integer getMaxFacetHits() {
    return maxFacetHits;
  }

  public IndexSettingsAsSearchParams setAttributeCriteriaComputedByMinProximity(
    Boolean attributeCriteriaComputedByMinProximity
  ) {
    this.attributeCriteriaComputedByMinProximity =
      attributeCriteriaComputedByMinProximity;
    return this;
  }

  /**
   * When attribute is ranked above proximity in your ranking formula, proximity is used to select
   * which searchable attribute is matched in the attribute ranking stage.
   *
   * @return attributeCriteriaComputedByMinProximity
   */
  @javax.annotation.Nullable
  public Boolean getAttributeCriteriaComputedByMinProximity() {
    return attributeCriteriaComputedByMinProximity;
  }

  public IndexSettingsAsSearchParams setRenderingContent(
    Object renderingContent
  ) {
    this.renderingContent = renderingContent;
    return this;
  }

  /**
   * Content defining how the search interface should be rendered. Can be set via the settings for a
   * default value and can be overridden via rules.
   *
   * @return renderingContent
   */
  @javax.annotation.Nullable
  public Object getRenderingContent() {
    return renderingContent;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IndexSettingsAsSearchParams indexSettingsAsSearchParams = (IndexSettingsAsSearchParams) o;
    return (
      Objects.equals(
        this.searchableAttributes,
        indexSettingsAsSearchParams.searchableAttributes
      ) &&
      Objects.equals(
        this.attributesForFaceting,
        indexSettingsAsSearchParams.attributesForFaceting
      ) &&
      Objects.equals(
        this.unretrievableAttributes,
        indexSettingsAsSearchParams.unretrievableAttributes
      ) &&
      Objects.equals(
        this.attributesToRetrieve,
        indexSettingsAsSearchParams.attributesToRetrieve
      ) &&
      Objects.equals(
        this.restrictSearchableAttributes,
        indexSettingsAsSearchParams.restrictSearchableAttributes
      ) &&
      Objects.equals(this.ranking, indexSettingsAsSearchParams.ranking) &&
      Objects.equals(
        this.customRanking,
        indexSettingsAsSearchParams.customRanking
      ) &&
      Objects.equals(
        this.relevancyStrictness,
        indexSettingsAsSearchParams.relevancyStrictness
      ) &&
      Objects.equals(
        this.attributesToHighlight,
        indexSettingsAsSearchParams.attributesToHighlight
      ) &&
      Objects.equals(
        this.attributesToSnippet,
        indexSettingsAsSearchParams.attributesToSnippet
      ) &&
      Objects.equals(
        this.highlightPreTag,
        indexSettingsAsSearchParams.highlightPreTag
      ) &&
      Objects.equals(
        this.highlightPostTag,
        indexSettingsAsSearchParams.highlightPostTag
      ) &&
      Objects.equals(
        this.snippetEllipsisText,
        indexSettingsAsSearchParams.snippetEllipsisText
      ) &&
      Objects.equals(
        this.restrictHighlightAndSnippetArrays,
        indexSettingsAsSearchParams.restrictHighlightAndSnippetArrays
      ) &&
      Objects.equals(
        this.hitsPerPage,
        indexSettingsAsSearchParams.hitsPerPage
      ) &&
      Objects.equals(
        this.minWordSizefor1Typo,
        indexSettingsAsSearchParams.minWordSizefor1Typo
      ) &&
      Objects.equals(
        this.minWordSizefor2Typos,
        indexSettingsAsSearchParams.minWordSizefor2Typos
      ) &&
      Objects.equals(
        this.typoTolerance,
        indexSettingsAsSearchParams.typoTolerance
      ) &&
      Objects.equals(
        this.allowTyposOnNumericTokens,
        indexSettingsAsSearchParams.allowTyposOnNumericTokens
      ) &&
      Objects.equals(
        this.disableTypoToleranceOnAttributes,
        indexSettingsAsSearchParams.disableTypoToleranceOnAttributes
      ) &&
      Objects.equals(
        this.separatorsToIndex,
        indexSettingsAsSearchParams.separatorsToIndex
      ) &&
      Objects.equals(
        this.ignorePlurals,
        indexSettingsAsSearchParams.ignorePlurals
      ) &&
      Objects.equals(
        this.removeStopWords,
        indexSettingsAsSearchParams.removeStopWords
      ) &&
      Objects.equals(
        this.keepDiacriticsOnCharacters,
        indexSettingsAsSearchParams.keepDiacriticsOnCharacters
      ) &&
      Objects.equals(
        this.queryLanguages,
        indexSettingsAsSearchParams.queryLanguages
      ) &&
      Objects.equals(
        this.decompoundQuery,
        indexSettingsAsSearchParams.decompoundQuery
      ) &&
      Objects.equals(
        this.enableRules,
        indexSettingsAsSearchParams.enableRules
      ) &&
      Objects.equals(
        this.enablePersonalization,
        indexSettingsAsSearchParams.enablePersonalization
      ) &&
      Objects.equals(this.queryType, indexSettingsAsSearchParams.queryType) &&
      Objects.equals(
        this.removeWordsIfNoResults,
        indexSettingsAsSearchParams.removeWordsIfNoResults
      ) &&
      Objects.equals(
        this.advancedSyntax,
        indexSettingsAsSearchParams.advancedSyntax
      ) &&
      Objects.equals(
        this.optionalWords,
        indexSettingsAsSearchParams.optionalWords
      ) &&
      Objects.equals(
        this.disableExactOnAttributes,
        indexSettingsAsSearchParams.disableExactOnAttributes
      ) &&
      Objects.equals(
        this.exactOnSingleWordQuery,
        indexSettingsAsSearchParams.exactOnSingleWordQuery
      ) &&
      Objects.equals(
        this.alternativesAsExact,
        indexSettingsAsSearchParams.alternativesAsExact
      ) &&
      Objects.equals(
        this.advancedSyntaxFeatures,
        indexSettingsAsSearchParams.advancedSyntaxFeatures
      ) &&
      Objects.equals(this.distinct, indexSettingsAsSearchParams.distinct) &&
      Objects.equals(this.synonyms, indexSettingsAsSearchParams.synonyms) &&
      Objects.equals(
        this.replaceSynonymsInHighlight,
        indexSettingsAsSearchParams.replaceSynonymsInHighlight
      ) &&
      Objects.equals(
        this.minProximity,
        indexSettingsAsSearchParams.minProximity
      ) &&
      Objects.equals(
        this.responseFields,
        indexSettingsAsSearchParams.responseFields
      ) &&
      Objects.equals(
        this.maxFacetHits,
        indexSettingsAsSearchParams.maxFacetHits
      ) &&
      Objects.equals(
        this.attributeCriteriaComputedByMinProximity,
        indexSettingsAsSearchParams.attributeCriteriaComputedByMinProximity
      ) &&
      Objects.equals(
        this.renderingContent,
        indexSettingsAsSearchParams.renderingContent
      )
    );
  }

  @Override
  public int hashCode() {
    return Objects.hash(
      searchableAttributes,
      attributesForFaceting,
      unretrievableAttributes,
      attributesToRetrieve,
      restrictSearchableAttributes,
      ranking,
      customRanking,
      relevancyStrictness,
      attributesToHighlight,
      attributesToSnippet,
      highlightPreTag,
      highlightPostTag,
      snippetEllipsisText,
      restrictHighlightAndSnippetArrays,
      hitsPerPage,
      minWordSizefor1Typo,
      minWordSizefor2Typos,
      typoTolerance,
      allowTyposOnNumericTokens,
      disableTypoToleranceOnAttributes,
      separatorsToIndex,
      ignorePlurals,
      removeStopWords,
      keepDiacriticsOnCharacters,
      queryLanguages,
      decompoundQuery,
      enableRules,
      enablePersonalization,
      queryType,
      removeWordsIfNoResults,
      advancedSyntax,
      optionalWords,
      disableExactOnAttributes,
      exactOnSingleWordQuery,
      alternativesAsExact,
      advancedSyntaxFeatures,
      distinct,
      synonyms,
      replaceSynonymsInHighlight,
      minProximity,
      responseFields,
      maxFacetHits,
      attributeCriteriaComputedByMinProximity,
      renderingContent
    );
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IndexSettingsAsSearchParams {\n");
    sb
      .append("    searchableAttributes: ")
      .append(toIndentedString(searchableAttributes))
      .append("\n");
    sb
      .append("    attributesForFaceting: ")
      .append(toIndentedString(attributesForFaceting))
      .append("\n");
    sb
      .append("    unretrievableAttributes: ")
      .append(toIndentedString(unretrievableAttributes))
      .append("\n");
    sb
      .append("    attributesToRetrieve: ")
      .append(toIndentedString(attributesToRetrieve))
      .append("\n");
    sb
      .append("    restrictSearchableAttributes: ")
      .append(toIndentedString(restrictSearchableAttributes))
      .append("\n");
    sb.append("    ranking: ").append(toIndentedString(ranking)).append("\n");
    sb
      .append("    customRanking: ")
      .append(toIndentedString(customRanking))
      .append("\n");
    sb
      .append("    relevancyStrictness: ")
      .append(toIndentedString(relevancyStrictness))
      .append("\n");
    sb
      .append("    attributesToHighlight: ")
      .append(toIndentedString(attributesToHighlight))
      .append("\n");
    sb
      .append("    attributesToSnippet: ")
      .append(toIndentedString(attributesToSnippet))
      .append("\n");
    sb
      .append("    highlightPreTag: ")
      .append(toIndentedString(highlightPreTag))
      .append("\n");
    sb
      .append("    highlightPostTag: ")
      .append(toIndentedString(highlightPostTag))
      .append("\n");
    sb
      .append("    snippetEllipsisText: ")
      .append(toIndentedString(snippetEllipsisText))
      .append("\n");
    sb
      .append("    restrictHighlightAndSnippetArrays: ")
      .append(toIndentedString(restrictHighlightAndSnippetArrays))
      .append("\n");
    sb
      .append("    hitsPerPage: ")
      .append(toIndentedString(hitsPerPage))
      .append("\n");
    sb
      .append("    minWordSizefor1Typo: ")
      .append(toIndentedString(minWordSizefor1Typo))
      .append("\n");
    sb
      .append("    minWordSizefor2Typos: ")
      .append(toIndentedString(minWordSizefor2Typos))
      .append("\n");
    sb
      .append("    typoTolerance: ")
      .append(toIndentedString(typoTolerance))
      .append("\n");
    sb
      .append("    allowTyposOnNumericTokens: ")
      .append(toIndentedString(allowTyposOnNumericTokens))
      .append("\n");
    sb
      .append("    disableTypoToleranceOnAttributes: ")
      .append(toIndentedString(disableTypoToleranceOnAttributes))
      .append("\n");
    sb
      .append("    separatorsToIndex: ")
      .append(toIndentedString(separatorsToIndex))
      .append("\n");
    sb
      .append("    ignorePlurals: ")
      .append(toIndentedString(ignorePlurals))
      .append("\n");
    sb
      .append("    removeStopWords: ")
      .append(toIndentedString(removeStopWords))
      .append("\n");
    sb
      .append("    keepDiacriticsOnCharacters: ")
      .append(toIndentedString(keepDiacriticsOnCharacters))
      .append("\n");
    sb
      .append("    queryLanguages: ")
      .append(toIndentedString(queryLanguages))
      .append("\n");
    sb
      .append("    decompoundQuery: ")
      .append(toIndentedString(decompoundQuery))
      .append("\n");
    sb
      .append("    enableRules: ")
      .append(toIndentedString(enableRules))
      .append("\n");
    sb
      .append("    enablePersonalization: ")
      .append(toIndentedString(enablePersonalization))
      .append("\n");
    sb
      .append("    queryType: ")
      .append(toIndentedString(queryType))
      .append("\n");
    sb
      .append("    removeWordsIfNoResults: ")
      .append(toIndentedString(removeWordsIfNoResults))
      .append("\n");
    sb
      .append("    advancedSyntax: ")
      .append(toIndentedString(advancedSyntax))
      .append("\n");
    sb
      .append("    optionalWords: ")
      .append(toIndentedString(optionalWords))
      .append("\n");
    sb
      .append("    disableExactOnAttributes: ")
      .append(toIndentedString(disableExactOnAttributes))
      .append("\n");
    sb
      .append("    exactOnSingleWordQuery: ")
      .append(toIndentedString(exactOnSingleWordQuery))
      .append("\n");
    sb
      .append("    alternativesAsExact: ")
      .append(toIndentedString(alternativesAsExact))
      .append("\n");
    sb
      .append("    advancedSyntaxFeatures: ")
      .append(toIndentedString(advancedSyntaxFeatures))
      .append("\n");
    sb.append("    distinct: ").append(toIndentedString(distinct)).append("\n");
    sb.append("    synonyms: ").append(toIndentedString(synonyms)).append("\n");
    sb
      .append("    replaceSynonymsInHighlight: ")
      .append(toIndentedString(replaceSynonymsInHighlight))
      .append("\n");
    sb
      .append("    minProximity: ")
      .append(toIndentedString(minProximity))
      .append("\n");
    sb
      .append("    responseFields: ")
      .append(toIndentedString(responseFields))
      .append("\n");
    sb
      .append("    maxFacetHits: ")
      .append(toIndentedString(maxFacetHits))
      .append("\n");
    sb
      .append("    attributeCriteriaComputedByMinProximity: ")
      .append(toIndentedString(attributeCriteriaComputedByMinProximity))
      .append("\n");
    sb
      .append("    renderingContent: ")
      .append(toIndentedString(renderingContent))
      .append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}
