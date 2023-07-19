// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.

/**
 * Settings for the semantic search part of NeuralSearch. Only used when `mode` is _neuralSearch_.
 */
export type IndexSettingsAsSearchParamsSemanticSearch = {
  /**
   * Indices from which to collect click and conversion events. If null, the current index and replica group will be used as the event source.
   */
  eventSources?: string[] | null;
};
