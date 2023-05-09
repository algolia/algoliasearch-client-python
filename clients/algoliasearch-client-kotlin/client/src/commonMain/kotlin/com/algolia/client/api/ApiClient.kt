package com.algolia.client.api

import com.algolia.client.configuration.ClientOptions
import com.algolia.client.transport.Requester

/**
 * An interface representing an API client with specific properties and options.
 *
 * @property appId The unique identifier for the application using the API client.
 * @property apiKey The API key used for authentication.
 * @property options A set of custom client options to configure the behavior of the API client.
 */
public sealed interface ApiClient {
  public val appId: String
  public val apiKey: String
  public val options: ClientOptions
  public val requester: Requester
}
