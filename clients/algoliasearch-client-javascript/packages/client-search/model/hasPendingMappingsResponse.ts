// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.

export type HasPendingMappingsResponse = {
  /**
   * Indicates whether there are clusters undergoing migration, creation, or deletion.
   */
  pending: boolean;

  /**
   * Cluster pending mapping state: migrating, creating, deleting.
   */
  clusters?: Record<string, string[]>;
};
