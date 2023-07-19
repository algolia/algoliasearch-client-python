// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.

export type ClickThroughRateEvent = {
  /**
   * [Click-through rate (CTR)](https://www.algolia.com/doc/guides/search-analytics/concepts/metrics/#click-through-rate).
   */
  rate: number;

  /**
   * Number of click events.
   */
  clickCount: number;

  /**
   * Number of tracked searches. This is the number of search requests where the `clickAnalytics` parameter is `true`.
   */
  trackedSearchCount: number;

  /**
   * Date of the event in the format YYYY-MM-DD.
   */
  date: string;
};
