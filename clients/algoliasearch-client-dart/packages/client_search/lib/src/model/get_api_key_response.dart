// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
// ignore_for_file: unused_element
import 'package:algolia_client_search/src/model/acl.dart';

import 'package:json_annotation/json_annotation.dart';

part 'get_api_key_response.g.dart';

@JsonSerializable()
final class GetApiKeyResponse {
  /// Returns a new [GetApiKeyResponse] instance.
  const GetApiKeyResponse({
    this.value,
    required this.createdAt,
    required this.acl,
    this.description,
    this.indexes,
    this.maxHitsPerQuery,
    this.maxQueriesPerIPPerHour,
    this.queryParameters,
    this.referers,
    this.validity,
  });

  /// API key.
  @JsonKey(name: r'value')
  final String? value;

  /// Timestamp of creation in milliseconds in [Unix epoch time](https://wikipedia.org/wiki/Unix_time).
  @JsonKey(name: r'createdAt')
  final int createdAt;

  /// [Permissions](https://www.algolia.com/doc/guides/security/api-keys/#access-control-list-acl) associated with the key.
  @JsonKey(name: r'acl')
  final List<Acl> acl;

  /// Description of an API key for you and your team members.
  @JsonKey(name: r'description')
  final String? description;

  /// Restricts this API key to a list of indices or index patterns. If the list is empty, all indices are allowed. Specify either an exact index name or a pattern with a leading or trailing wildcard character (or both). For example: - `dev_*` matches all indices starting with \"dev_\" - `*_dev` matches all indices ending with \"_dev\" - `*_products_*` matches all indices containing \"_products_\".
  @JsonKey(name: r'indexes')
  final List<String>? indexes;

  /// Maximum number of hits this API key can retrieve in one query. If zero, no limit is enforced. > **Note**: Use this parameter to protect you from third-party attempts to retrieve your entire content by massively querying the index.
  @JsonKey(name: r'maxHitsPerQuery')
  final int? maxHitsPerQuery;

  /// Maximum number of API calls per hour allowed from a given IP address or [user token](https://www.algolia.com/doc/guides/sending-events/concepts/usertoken/). Each time an API call is performed with this key, a check is performed. If there were more than the specified number of calls within the last hour, the API returns an error with the status code `429` (Too Many Requests).  > **Note**: Use this parameter to protect you from third-party attempts to retrieve your entire content by massively querying the index.
  @JsonKey(name: r'maxQueriesPerIPPerHour')
  final int? maxQueriesPerIPPerHour;

  /// Force some [query parameters](https://www.algolia.com/doc/api-reference/api-parameters/) to be applied for each query made with this API key. It's a URL-encoded query string.
  @JsonKey(name: r'queryParameters')
  final String? queryParameters;

  /// Restrict this API key to specific [referrers](https://www.algolia.com/doc/guides/security/api-keys/in-depth/api-key-restrictions/#http-referrers). If empty, all referrers are allowed. For example: - `https://algolia.com/_*` matches all referrers starting with \"https://algolia.com/\" - `*.algolia.com` matches all referrers ending with \".algolia.com\" - `*algolia.com*` allows everything in the domain \"algolia.com\".
  @JsonKey(name: r'referers')
  final List<String>? referers;

  /// Validity duration of a key (in seconds).  The key will automatically be removed after this time has expired. The default value of 0 never expires. Short-lived API keys are useful to grant temporary access to your data. For example, in mobile apps, you can't [control when users update your app](https://www.algolia.com/doc/guides/security/security-best-practices/#use-secured-api-keys-in-mobile-apps). So instead of encoding keys into your app as you would for a web app, you should dynamically fetch them from your mobile app's backend.
  @JsonKey(name: r'validity')
  final int? validity;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is GetApiKeyResponse &&
          other.value == value &&
          other.createdAt == createdAt &&
          other.acl == acl &&
          other.description == description &&
          other.indexes == indexes &&
          other.maxHitsPerQuery == maxHitsPerQuery &&
          other.maxQueriesPerIPPerHour == maxQueriesPerIPPerHour &&
          other.queryParameters == queryParameters &&
          other.referers == referers &&
          other.validity == validity;

  @override
  int get hashCode =>
      value.hashCode +
      createdAt.hashCode +
      acl.hashCode +
      description.hashCode +
      indexes.hashCode +
      maxHitsPerQuery.hashCode +
      maxQueriesPerIPPerHour.hashCode +
      queryParameters.hashCode +
      referers.hashCode +
      validity.hashCode;

  factory GetApiKeyResponse.fromJson(Map<String, dynamic> json) =>
      _$GetApiKeyResponseFromJson(json);

  Map<String, dynamic> toJson() => _$GetApiKeyResponseToJson(this);

  @override
  String toString() {
    return toJson().toString();
  }
}
