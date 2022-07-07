package com.algolia.model.search;

import com.fasterxml.jackson.annotation.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

/** The Algolia index settings. */
public class IndexSettings {

  @JsonProperty("replicas")
  private List<String> replicas;

  @JsonProperty("paginationLimitedTo")
  private Integer paginationLimitedTo;

  @JsonProperty("disableTypoToleranceOnWords")
  private List<String> disableTypoToleranceOnWords;

  @JsonProperty("attributesToTransliterate")
  private List<String> attributesToTransliterate;

  @JsonProperty("camelCaseAttributes")
  private List<String> camelCaseAttributes;

  @JsonProperty("decompoundedAttributes")
  private Object decompoundedAttributes;

  @JsonProperty("indexLanguages")
  private List<String> indexLanguages;

  @JsonProperty("disablePrefixOnAttributes")
  private List<String> disablePrefixOnAttributes;

  @JsonProperty("allowCompressionOfIntegerArray")
  private Boolean allowCompressionOfIntegerArray;

  @JsonProperty("numericAttributesForFiltering")
  private List<String> numericAttributesForFiltering;

  @JsonProperty("separatorsToIndex")
  private String separatorsToIndex;

  @JsonProperty("searchableAttributes")
  private List<String> searchableAttributes;

  @JsonProperty("userData")
  private Object userData;

  @JsonProperty("customNormalization")
  private Map<String, Map<String, String>> customNormalization;

  @JsonProperty("attributesForFaceting")
  private List<String> attributesForFaceting;

  @JsonProperty("unretrievableAttributes")
  private List<String> unretrievableAttributes;

  @JsonProperty("attributesToRetrieve")
  private List<String> attributesToRetrieve;

  @JsonProperty("restrictSearchableAttributes")
  private List<String> restrictSearchableAttributes;

  @JsonProperty("ranking")
  private List<String> ranking;

  @JsonProperty("customRanking")
  private List<String> customRanking;

  @JsonProperty("relevancyStrictness")
  private Integer relevancyStrictness;

  @JsonProperty("attributesToHighlight")
  private List<String> attributesToHighlight;

  @JsonProperty("attributesToSnippet")
  private List<String> attributesToSnippet;

  @JsonProperty("highlightPreTag")
  private String highlightPreTag;

  @JsonProperty("highlightPostTag")
  private String highlightPostTag;

  @JsonProperty("snippetEllipsisText")
  private String snippetEllipsisText;

  @JsonProperty("restrictHighlightAndSnippetArrays")
  private Boolean restrictHighlightAndSnippetArrays;

  @JsonProperty("hitsPerPage")
  private Integer hitsPerPage;

  @JsonProperty("minWordSizefor1Typo")
  private Integer minWordSizefor1Typo;

  @JsonProperty("minWordSizefor2Typos")
  private Integer minWordSizefor2Typos;

  @JsonProperty("typoTolerance")
  private TypoTolerance typoTolerance;

  @JsonProperty("allowTyposOnNumericTokens")
  private Boolean allowTyposOnNumericTokens;

  @JsonProperty("disableTypoToleranceOnAttributes")
  private List<String> disableTypoToleranceOnAttributes;

  @JsonProperty("ignorePlurals")
  private IgnorePlurals ignorePlurals;

  @JsonProperty("removeStopWords")
  private RemoveStopWords removeStopWords;

  @JsonProperty("keepDiacriticsOnCharacters")
  private String keepDiacriticsOnCharacters;

  @JsonProperty("queryLanguages")
  private List<String> queryLanguages;

  @JsonProperty("decompoundQuery")
  private Boolean decompoundQuery;

  @JsonProperty("enableRules")
  private Boolean enableRules;

  @JsonProperty("enablePersonalization")
  private Boolean enablePersonalization;

  @JsonProperty("queryType")
  private QueryType queryType;

  @JsonProperty("removeWordsIfNoResults")
  private RemoveWordsIfNoResults removeWordsIfNoResults;

  @JsonProperty("advancedSyntax")
  private Boolean advancedSyntax;

  @JsonProperty("optionalWords")
  private List<String> optionalWords;

  @JsonProperty("disableExactOnAttributes")
  private List<String> disableExactOnAttributes;

  @JsonProperty("exactOnSingleWordQuery")
  private ExactOnSingleWordQuery exactOnSingleWordQuery;

  @JsonProperty("alternativesAsExact")
  private List<AlternativesAsExact> alternativesAsExact;

  @JsonProperty("advancedSyntaxFeatures")
  private List<AdvancedSyntaxFeatures> advancedSyntaxFeatures;

  @JsonProperty("distinct")
  private Integer distinct;

  @JsonProperty("synonyms")
  private Boolean synonyms;

  @JsonProperty("replaceSynonymsInHighlight")
  private Boolean replaceSynonymsInHighlight;

  @JsonProperty("minProximity")
  private Integer minProximity;

  @JsonProperty("responseFields")
  private List<String> responseFields;

  @JsonProperty("maxFacetHits")
  private Integer maxFacetHits;

  @JsonProperty("attributeCriteriaComputedByMinProximity")
  private Boolean attributeCriteriaComputedByMinProximity;

  @JsonProperty("renderingContent")
  private RenderingContent renderingContent;

  public IndexSettings setReplicas(List<String> replicas) {
    this.replicas = replicas;
    return this;
  }

  public IndexSettings addReplicas(String replicasItem) {
    if (this.replicas == null) {
      this.replicas = new ArrayList<>();
    }
    this.replicas.add(replicasItem);
    return this;
  }

  /**
   * Creates replicas, exact copies of an index.
   *
   * @return replicas
   */
  @javax.annotation.Nullable
  public List<String> getReplicas() {
    return replicas;
  }

  public IndexSettings setPaginationLimitedTo(Integer paginationLimitedTo) {
    this.paginationLimitedTo = paginationLimitedTo;
    return this;
  }

  /**
   * Set the maximum number of hits accessible via pagination.
   *
   * @return paginationLimitedTo
   */
  @javax.annotation.Nullable
  public Integer getPaginationLimitedTo() {
    return paginationLimitedTo;
  }

  public IndexSettings setDisableTypoToleranceOnWords(List<String> disableTypoToleranceOnWords) {
    this.disableTypoToleranceOnWords = disableTypoToleranceOnWords;
    return this;
  }

  public IndexSettings addDisableTypoToleranceOnWords(String disableTypoToleranceOnWordsItem) {
    if (this.disableTypoToleranceOnWords == null) {
      this.disableTypoToleranceOnWords = new ArrayList<>();
    }
    this.disableTypoToleranceOnWords.add(disableTypoToleranceOnWordsItem);
    return this;
  }

  /**
   * A list of words for which you want to turn off typo tolerance.
   *
   * @return disableTypoToleranceOnWords
   */
  @javax.annotation.Nullable
  public List<String> getDisableTypoToleranceOnWords() {
    return disableTypoToleranceOnWords;
  }

  public IndexSettings setAttributesToTransliterate(List<String> attributesToTransliterate) {
    this.attributesToTransliterate = attributesToTransliterate;
    return this;
  }

  public IndexSettings addAttributesToTransliterate(String attributesToTransliterateItem) {
    if (this.attributesToTransliterate == null) {
      this.attributesToTransliterate = new ArrayList<>();
    }
    this.attributesToTransliterate.add(attributesToTransliterateItem);
    return this;
  }

  /**
   * Specify on which attributes in your index Algolia should apply Japanese transliteration to make
   * words indexed in Katakana or Kanji searchable in Hiragana.
   *
   * @return attributesToTransliterate
   */
  @javax.annotation.Nullable
  public List<String> getAttributesToTransliterate() {
    return attributesToTransliterate;
  }

  public IndexSettings setCamelCaseAttributes(List<String> camelCaseAttributes) {
    this.camelCaseAttributes = camelCaseAttributes;
    return this;
  }

  public IndexSettings addCamelCaseAttributes(String camelCaseAttributesItem) {
    if (this.camelCaseAttributes == null) {
      this.camelCaseAttributes = new ArrayList<>();
    }
    this.camelCaseAttributes.add(camelCaseAttributesItem);
    return this;
  }

  /**
   * List of attributes on which to do a decomposition of camel case words.
   *
   * @return camelCaseAttributes
   */
  @javax.annotation.Nullable
  public List<String> getCamelCaseAttributes() {
    return camelCaseAttributes;
  }

  public IndexSettings setDecompoundedAttributes(Object decompoundedAttributes) {
    this.decompoundedAttributes = decompoundedAttributes;
    return this;
  }

  /**
   * Specify on which attributes in your index Algolia should apply word segmentation, also known as
   * decompounding.
   *
   * @return decompoundedAttributes
   */
  @javax.annotation.Nullable
  public Object getDecompoundedAttributes() {
    return decompoundedAttributes;
  }

  public IndexSettings setIndexLanguages(List<String> indexLanguages) {
    this.indexLanguages = indexLanguages;
    return this;
  }

  public IndexSettings addIndexLanguages(String indexLanguagesItem) {
    if (this.indexLanguages == null) {
      this.indexLanguages = new ArrayList<>();
    }
    this.indexLanguages.add(indexLanguagesItem);
    return this;
  }

  /**
   * Sets the languages at the index level for language-specific processing such as tokenization and
   * normalization.
   *
   * @return indexLanguages
   */
  @javax.annotation.Nullable
  public List<String> getIndexLanguages() {
    return indexLanguages;
  }

  public IndexSettings setDisablePrefixOnAttributes(List<String> disablePrefixOnAttributes) {
    this.disablePrefixOnAttributes = disablePrefixOnAttributes;
    return this;
  }

  public IndexSettings addDisablePrefixOnAttributes(String disablePrefixOnAttributesItem) {
    if (this.disablePrefixOnAttributes == null) {
      this.disablePrefixOnAttributes = new ArrayList<>();
    }
    this.disablePrefixOnAttributes.add(disablePrefixOnAttributesItem);
    return this;
  }

  /**
   * List of attributes on which you want to disable prefix matching.
   *
   * @return disablePrefixOnAttributes
   */
  @javax.annotation.Nullable
  public List<String> getDisablePrefixOnAttributes() {
    return disablePrefixOnAttributes;
  }

  public IndexSettings setAllowCompressionOfIntegerArray(Boolean allowCompressionOfIntegerArray) {
    this.allowCompressionOfIntegerArray = allowCompressionOfIntegerArray;
    return this;
  }

  /**
   * Enables compression of large integer arrays.
   *
   * @return allowCompressionOfIntegerArray
   */
  @javax.annotation.Nullable
  public Boolean getAllowCompressionOfIntegerArray() {
    return allowCompressionOfIntegerArray;
  }

  public IndexSettings setNumericAttributesForFiltering(List<String> numericAttributesForFiltering) {
    this.numericAttributesForFiltering = numericAttributesForFiltering;
    return this;
  }

  public IndexSettings addNumericAttributesForFiltering(String numericAttributesForFilteringItem) {
    if (this.numericAttributesForFiltering == null) {
      this.numericAttributesForFiltering = new ArrayList<>();
    }
    this.numericAttributesForFiltering.add(numericAttributesForFilteringItem);
    return this;
  }

  /**
   * List of numeric attributes that can be used as numerical filters.
   *
   * @return numericAttributesForFiltering
   */
  @javax.annotation.Nullable
  public List<String> getNumericAttributesForFiltering() {
    return numericAttributesForFiltering;
  }

  public IndexSettings setSeparatorsToIndex(String separatorsToIndex) {
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

  public IndexSettings setSearchableAttributes(List<String> searchableAttributes) {
    this.searchableAttributes = searchableAttributes;
    return this;
  }

  public IndexSettings addSearchableAttributes(String searchableAttributesItem) {
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

  public IndexSettings setUserData(Object userData) {
    this.userData = userData;
    return this;
  }

  /**
   * Lets you store custom data in your indices.
   *
   * @return userData
   */
  @javax.annotation.Nullable
  public Object getUserData() {
    return userData;
  }

  public IndexSettings setCustomNormalization(Map<String, Map<String, String>> customNormalization) {
    this.customNormalization = customNormalization;
    return this;
  }

  public IndexSettings putCustomNormalization(String key, Map<String, String> customNormalizationItem) {
    if (this.customNormalization == null) {
      this.customNormalization = new HashMap<>();
    }
    this.customNormalization.put(key, customNormalizationItem);
    return this;
  }

  /**
   * Overrides Algolia's default normalization.
   *
   * @return customNormalization
   */
  @javax.annotation.Nullable
  public Map<String, Map<String, String>> getCustomNormalization() {
    return customNormalization;
  }

  public IndexSettings setAttributesForFaceting(List<String> attributesForFaceting) {
    this.attributesForFaceting = attributesForFaceting;
    return this;
  }

  public IndexSettings addAttributesForFaceting(String attributesForFacetingItem) {
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

  public IndexSettings setUnretrievableAttributes(List<String> unretrievableAttributes) {
    this.unretrievableAttributes = unretrievableAttributes;
    return this;
  }

  public IndexSettings addUnretrievableAttributes(String unretrievableAttributesItem) {
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

  public IndexSettings setAttributesToRetrieve(List<String> attributesToRetrieve) {
    this.attributesToRetrieve = attributesToRetrieve;
    return this;
  }

  public IndexSettings addAttributesToRetrieve(String attributesToRetrieveItem) {
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

  public IndexSettings setRestrictSearchableAttributes(List<String> restrictSearchableAttributes) {
    this.restrictSearchableAttributes = restrictSearchableAttributes;
    return this;
  }

  public IndexSettings addRestrictSearchableAttributes(String restrictSearchableAttributesItem) {
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

  public IndexSettings setRanking(List<String> ranking) {
    this.ranking = ranking;
    return this;
  }

  public IndexSettings addRanking(String rankingItem) {
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

  public IndexSettings setCustomRanking(List<String> customRanking) {
    this.customRanking = customRanking;
    return this;
  }

  public IndexSettings addCustomRanking(String customRankingItem) {
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

  public IndexSettings setRelevancyStrictness(Integer relevancyStrictness) {
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

  public IndexSettings setAttributesToHighlight(List<String> attributesToHighlight) {
    this.attributesToHighlight = attributesToHighlight;
    return this;
  }

  public IndexSettings addAttributesToHighlight(String attributesToHighlightItem) {
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

  public IndexSettings setAttributesToSnippet(List<String> attributesToSnippet) {
    this.attributesToSnippet = attributesToSnippet;
    return this;
  }

  public IndexSettings addAttributesToSnippet(String attributesToSnippetItem) {
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

  public IndexSettings setHighlightPreTag(String highlightPreTag) {
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

  public IndexSettings setHighlightPostTag(String highlightPostTag) {
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

  public IndexSettings setSnippetEllipsisText(String snippetEllipsisText) {
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

  public IndexSettings setRestrictHighlightAndSnippetArrays(Boolean restrictHighlightAndSnippetArrays) {
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

  public IndexSettings setHitsPerPage(Integer hitsPerPage) {
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

  public IndexSettings setMinWordSizefor1Typo(Integer minWordSizefor1Typo) {
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

  public IndexSettings setMinWordSizefor2Typos(Integer minWordSizefor2Typos) {
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

  public IndexSettings setTypoTolerance(TypoTolerance typoTolerance) {
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

  public IndexSettings setAllowTyposOnNumericTokens(Boolean allowTyposOnNumericTokens) {
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

  public IndexSettings setDisableTypoToleranceOnAttributes(List<String> disableTypoToleranceOnAttributes) {
    this.disableTypoToleranceOnAttributes = disableTypoToleranceOnAttributes;
    return this;
  }

  public IndexSettings addDisableTypoToleranceOnAttributes(String disableTypoToleranceOnAttributesItem) {
    if (this.disableTypoToleranceOnAttributes == null) {
      this.disableTypoToleranceOnAttributes = new ArrayList<>();
    }
    this.disableTypoToleranceOnAttributes.add(disableTypoToleranceOnAttributesItem);
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

  public IndexSettings setIgnorePlurals(IgnorePlurals ignorePlurals) {
    this.ignorePlurals = ignorePlurals;
    return this;
  }

  /**
   * Get ignorePlurals
   *
   * @return ignorePlurals
   */
  @javax.annotation.Nullable
  public IgnorePlurals getIgnorePlurals() {
    return ignorePlurals;
  }

  public IndexSettings setRemoveStopWords(RemoveStopWords removeStopWords) {
    this.removeStopWords = removeStopWords;
    return this;
  }

  /**
   * Get removeStopWords
   *
   * @return removeStopWords
   */
  @javax.annotation.Nullable
  public RemoveStopWords getRemoveStopWords() {
    return removeStopWords;
  }

  public IndexSettings setKeepDiacriticsOnCharacters(String keepDiacriticsOnCharacters) {
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

  public IndexSettings setQueryLanguages(List<String> queryLanguages) {
    this.queryLanguages = queryLanguages;
    return this;
  }

  public IndexSettings addQueryLanguages(String queryLanguagesItem) {
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

  public IndexSettings setDecompoundQuery(Boolean decompoundQuery) {
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

  public IndexSettings setEnableRules(Boolean enableRules) {
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

  public IndexSettings setEnablePersonalization(Boolean enablePersonalization) {
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

  public IndexSettings setQueryType(QueryType queryType) {
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

  public IndexSettings setRemoveWordsIfNoResults(RemoveWordsIfNoResults removeWordsIfNoResults) {
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

  public IndexSettings setAdvancedSyntax(Boolean advancedSyntax) {
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

  public IndexSettings setOptionalWords(List<String> optionalWords) {
    this.optionalWords = optionalWords;
    return this;
  }

  public IndexSettings addOptionalWords(String optionalWordsItem) {
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

  public IndexSettings setDisableExactOnAttributes(List<String> disableExactOnAttributes) {
    this.disableExactOnAttributes = disableExactOnAttributes;
    return this;
  }

  public IndexSettings addDisableExactOnAttributes(String disableExactOnAttributesItem) {
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

  public IndexSettings setExactOnSingleWordQuery(ExactOnSingleWordQuery exactOnSingleWordQuery) {
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

  public IndexSettings setAlternativesAsExact(List<AlternativesAsExact> alternativesAsExact) {
    this.alternativesAsExact = alternativesAsExact;
    return this;
  }

  public IndexSettings addAlternativesAsExact(AlternativesAsExact alternativesAsExactItem) {
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

  public IndexSettings setAdvancedSyntaxFeatures(List<AdvancedSyntaxFeatures> advancedSyntaxFeatures) {
    this.advancedSyntaxFeatures = advancedSyntaxFeatures;
    return this;
  }

  public IndexSettings addAdvancedSyntaxFeatures(AdvancedSyntaxFeatures advancedSyntaxFeaturesItem) {
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

  public IndexSettings setDistinct(Integer distinct) {
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

  public IndexSettings setSynonyms(Boolean synonyms) {
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

  public IndexSettings setReplaceSynonymsInHighlight(Boolean replaceSynonymsInHighlight) {
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

  public IndexSettings setMinProximity(Integer minProximity) {
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

  public IndexSettings setResponseFields(List<String> responseFields) {
    this.responseFields = responseFields;
    return this;
  }

  public IndexSettings addResponseFields(String responseFieldsItem) {
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

  public IndexSettings setMaxFacetHits(Integer maxFacetHits) {
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

  public IndexSettings setAttributeCriteriaComputedByMinProximity(Boolean attributeCriteriaComputedByMinProximity) {
    this.attributeCriteriaComputedByMinProximity = attributeCriteriaComputedByMinProximity;
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

  public IndexSettings setRenderingContent(RenderingContent renderingContent) {
    this.renderingContent = renderingContent;
    return this;
  }

  /**
   * Get renderingContent
   *
   * @return renderingContent
   */
  @javax.annotation.Nullable
  public RenderingContent getRenderingContent() {
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
    IndexSettings indexSettings = (IndexSettings) o;
    return (
      Objects.equals(this.replicas, indexSettings.replicas) &&
      Objects.equals(this.paginationLimitedTo, indexSettings.paginationLimitedTo) &&
      Objects.equals(this.disableTypoToleranceOnWords, indexSettings.disableTypoToleranceOnWords) &&
      Objects.equals(this.attributesToTransliterate, indexSettings.attributesToTransliterate) &&
      Objects.equals(this.camelCaseAttributes, indexSettings.camelCaseAttributes) &&
      Objects.equals(this.decompoundedAttributes, indexSettings.decompoundedAttributes) &&
      Objects.equals(this.indexLanguages, indexSettings.indexLanguages) &&
      Objects.equals(this.disablePrefixOnAttributes, indexSettings.disablePrefixOnAttributes) &&
      Objects.equals(this.allowCompressionOfIntegerArray, indexSettings.allowCompressionOfIntegerArray) &&
      Objects.equals(this.numericAttributesForFiltering, indexSettings.numericAttributesForFiltering) &&
      Objects.equals(this.separatorsToIndex, indexSettings.separatorsToIndex) &&
      Objects.equals(this.searchableAttributes, indexSettings.searchableAttributes) &&
      Objects.equals(this.userData, indexSettings.userData) &&
      Objects.equals(this.customNormalization, indexSettings.customNormalization) &&
      Objects.equals(this.attributesForFaceting, indexSettings.attributesForFaceting) &&
      Objects.equals(this.unretrievableAttributes, indexSettings.unretrievableAttributes) &&
      Objects.equals(this.attributesToRetrieve, indexSettings.attributesToRetrieve) &&
      Objects.equals(this.restrictSearchableAttributes, indexSettings.restrictSearchableAttributes) &&
      Objects.equals(this.ranking, indexSettings.ranking) &&
      Objects.equals(this.customRanking, indexSettings.customRanking) &&
      Objects.equals(this.relevancyStrictness, indexSettings.relevancyStrictness) &&
      Objects.equals(this.attributesToHighlight, indexSettings.attributesToHighlight) &&
      Objects.equals(this.attributesToSnippet, indexSettings.attributesToSnippet) &&
      Objects.equals(this.highlightPreTag, indexSettings.highlightPreTag) &&
      Objects.equals(this.highlightPostTag, indexSettings.highlightPostTag) &&
      Objects.equals(this.snippetEllipsisText, indexSettings.snippetEllipsisText) &&
      Objects.equals(this.restrictHighlightAndSnippetArrays, indexSettings.restrictHighlightAndSnippetArrays) &&
      Objects.equals(this.hitsPerPage, indexSettings.hitsPerPage) &&
      Objects.equals(this.minWordSizefor1Typo, indexSettings.minWordSizefor1Typo) &&
      Objects.equals(this.minWordSizefor2Typos, indexSettings.minWordSizefor2Typos) &&
      Objects.equals(this.typoTolerance, indexSettings.typoTolerance) &&
      Objects.equals(this.allowTyposOnNumericTokens, indexSettings.allowTyposOnNumericTokens) &&
      Objects.equals(this.disableTypoToleranceOnAttributes, indexSettings.disableTypoToleranceOnAttributes) &&
      Objects.equals(this.ignorePlurals, indexSettings.ignorePlurals) &&
      Objects.equals(this.removeStopWords, indexSettings.removeStopWords) &&
      Objects.equals(this.keepDiacriticsOnCharacters, indexSettings.keepDiacriticsOnCharacters) &&
      Objects.equals(this.queryLanguages, indexSettings.queryLanguages) &&
      Objects.equals(this.decompoundQuery, indexSettings.decompoundQuery) &&
      Objects.equals(this.enableRules, indexSettings.enableRules) &&
      Objects.equals(this.enablePersonalization, indexSettings.enablePersonalization) &&
      Objects.equals(this.queryType, indexSettings.queryType) &&
      Objects.equals(this.removeWordsIfNoResults, indexSettings.removeWordsIfNoResults) &&
      Objects.equals(this.advancedSyntax, indexSettings.advancedSyntax) &&
      Objects.equals(this.optionalWords, indexSettings.optionalWords) &&
      Objects.equals(this.disableExactOnAttributes, indexSettings.disableExactOnAttributes) &&
      Objects.equals(this.exactOnSingleWordQuery, indexSettings.exactOnSingleWordQuery) &&
      Objects.equals(this.alternativesAsExact, indexSettings.alternativesAsExact) &&
      Objects.equals(this.advancedSyntaxFeatures, indexSettings.advancedSyntaxFeatures) &&
      Objects.equals(this.distinct, indexSettings.distinct) &&
      Objects.equals(this.synonyms, indexSettings.synonyms) &&
      Objects.equals(this.replaceSynonymsInHighlight, indexSettings.replaceSynonymsInHighlight) &&
      Objects.equals(this.minProximity, indexSettings.minProximity) &&
      Objects.equals(this.responseFields, indexSettings.responseFields) &&
      Objects.equals(this.maxFacetHits, indexSettings.maxFacetHits) &&
      Objects.equals(this.attributeCriteriaComputedByMinProximity, indexSettings.attributeCriteriaComputedByMinProximity) &&
      Objects.equals(this.renderingContent, indexSettings.renderingContent)
    );
  }

  @Override
  public int hashCode() {
    return Objects.hash(
      replicas,
      paginationLimitedTo,
      disableTypoToleranceOnWords,
      attributesToTransliterate,
      camelCaseAttributes,
      decompoundedAttributes,
      indexLanguages,
      disablePrefixOnAttributes,
      allowCompressionOfIntegerArray,
      numericAttributesForFiltering,
      separatorsToIndex,
      searchableAttributes,
      userData,
      customNormalization,
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
    sb.append("class IndexSettings {\n");
    sb.append("    replicas: ").append(toIndentedString(replicas)).append("\n");
    sb.append("    paginationLimitedTo: ").append(toIndentedString(paginationLimitedTo)).append("\n");
    sb.append("    disableTypoToleranceOnWords: ").append(toIndentedString(disableTypoToleranceOnWords)).append("\n");
    sb.append("    attributesToTransliterate: ").append(toIndentedString(attributesToTransliterate)).append("\n");
    sb.append("    camelCaseAttributes: ").append(toIndentedString(camelCaseAttributes)).append("\n");
    sb.append("    decompoundedAttributes: ").append(toIndentedString(decompoundedAttributes)).append("\n");
    sb.append("    indexLanguages: ").append(toIndentedString(indexLanguages)).append("\n");
    sb.append("    disablePrefixOnAttributes: ").append(toIndentedString(disablePrefixOnAttributes)).append("\n");
    sb.append("    allowCompressionOfIntegerArray: ").append(toIndentedString(allowCompressionOfIntegerArray)).append("\n");
    sb.append("    numericAttributesForFiltering: ").append(toIndentedString(numericAttributesForFiltering)).append("\n");
    sb.append("    separatorsToIndex: ").append(toIndentedString(separatorsToIndex)).append("\n");
    sb.append("    searchableAttributes: ").append(toIndentedString(searchableAttributes)).append("\n");
    sb.append("    userData: ").append(toIndentedString(userData)).append("\n");
    sb.append("    customNormalization: ").append(toIndentedString(customNormalization)).append("\n");
    sb.append("    attributesForFaceting: ").append(toIndentedString(attributesForFaceting)).append("\n");
    sb.append("    unretrievableAttributes: ").append(toIndentedString(unretrievableAttributes)).append("\n");
    sb.append("    attributesToRetrieve: ").append(toIndentedString(attributesToRetrieve)).append("\n");
    sb.append("    restrictSearchableAttributes: ").append(toIndentedString(restrictSearchableAttributes)).append("\n");
    sb.append("    ranking: ").append(toIndentedString(ranking)).append("\n");
    sb.append("    customRanking: ").append(toIndentedString(customRanking)).append("\n");
    sb.append("    relevancyStrictness: ").append(toIndentedString(relevancyStrictness)).append("\n");
    sb.append("    attributesToHighlight: ").append(toIndentedString(attributesToHighlight)).append("\n");
    sb.append("    attributesToSnippet: ").append(toIndentedString(attributesToSnippet)).append("\n");
    sb.append("    highlightPreTag: ").append(toIndentedString(highlightPreTag)).append("\n");
    sb.append("    highlightPostTag: ").append(toIndentedString(highlightPostTag)).append("\n");
    sb.append("    snippetEllipsisText: ").append(toIndentedString(snippetEllipsisText)).append("\n");
    sb.append("    restrictHighlightAndSnippetArrays: ").append(toIndentedString(restrictHighlightAndSnippetArrays)).append("\n");
    sb.append("    hitsPerPage: ").append(toIndentedString(hitsPerPage)).append("\n");
    sb.append("    minWordSizefor1Typo: ").append(toIndentedString(minWordSizefor1Typo)).append("\n");
    sb.append("    minWordSizefor2Typos: ").append(toIndentedString(minWordSizefor2Typos)).append("\n");
    sb.append("    typoTolerance: ").append(toIndentedString(typoTolerance)).append("\n");
    sb.append("    allowTyposOnNumericTokens: ").append(toIndentedString(allowTyposOnNumericTokens)).append("\n");
    sb.append("    disableTypoToleranceOnAttributes: ").append(toIndentedString(disableTypoToleranceOnAttributes)).append("\n");
    sb.append("    ignorePlurals: ").append(toIndentedString(ignorePlurals)).append("\n");
    sb.append("    removeStopWords: ").append(toIndentedString(removeStopWords)).append("\n");
    sb.append("    keepDiacriticsOnCharacters: ").append(toIndentedString(keepDiacriticsOnCharacters)).append("\n");
    sb.append("    queryLanguages: ").append(toIndentedString(queryLanguages)).append("\n");
    sb.append("    decompoundQuery: ").append(toIndentedString(decompoundQuery)).append("\n");
    sb.append("    enableRules: ").append(toIndentedString(enableRules)).append("\n");
    sb.append("    enablePersonalization: ").append(toIndentedString(enablePersonalization)).append("\n");
    sb.append("    queryType: ").append(toIndentedString(queryType)).append("\n");
    sb.append("    removeWordsIfNoResults: ").append(toIndentedString(removeWordsIfNoResults)).append("\n");
    sb.append("    advancedSyntax: ").append(toIndentedString(advancedSyntax)).append("\n");
    sb.append("    optionalWords: ").append(toIndentedString(optionalWords)).append("\n");
    sb.append("    disableExactOnAttributes: ").append(toIndentedString(disableExactOnAttributes)).append("\n");
    sb.append("    exactOnSingleWordQuery: ").append(toIndentedString(exactOnSingleWordQuery)).append("\n");
    sb.append("    alternativesAsExact: ").append(toIndentedString(alternativesAsExact)).append("\n");
    sb.append("    advancedSyntaxFeatures: ").append(toIndentedString(advancedSyntaxFeatures)).append("\n");
    sb.append("    distinct: ").append(toIndentedString(distinct)).append("\n");
    sb.append("    synonyms: ").append(toIndentedString(synonyms)).append("\n");
    sb.append("    replaceSynonymsInHighlight: ").append(toIndentedString(replaceSynonymsInHighlight)).append("\n");
    sb.append("    minProximity: ").append(toIndentedString(minProximity)).append("\n");
    sb.append("    responseFields: ").append(toIndentedString(responseFields)).append("\n");
    sb.append("    maxFacetHits: ").append(toIndentedString(maxFacetHits)).append("\n");
    sb
      .append("    attributeCriteriaComputedByMinProximity: ")
      .append(toIndentedString(attributeCriteriaComputedByMinProximity))
      .append("\n");
    sb.append("    renderingContent: ").append(toIndentedString(renderingContent)).append("\n");
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
