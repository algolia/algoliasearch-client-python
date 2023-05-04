package com.algolia.client.configuration

/**
 * @param url The url to target.
 * @param callType Whether this host should be used for [CallType.Read] or [CallType.Write]
 *   requests.
 */
public data class Host(
  public val url: String,
  public val callType: CallType? = null,
)
