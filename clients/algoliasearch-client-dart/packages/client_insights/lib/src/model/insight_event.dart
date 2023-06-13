// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
// ignore_for_file: unused_element
import 'package:algolia_client_insights/src/model/event_type.dart';

import 'package:json_annotation/json_annotation.dart';

part 'insight_event.g.dart';

@JsonSerializable()
final class InsightEvent {
  /// Returns a new [InsightEvent] instance.
  const InsightEvent({
    required this.eventType,
    required this.eventName,
    required this.index,
    required this.userToken,
    this.timestamp,
    this.queryID,
    this.objectIDs,
    this.filters,
    this.positions,
  });

  @JsonKey(name: r'eventType')
  final EventType eventType;

  /// A user-defined string used to categorize events.
  @JsonKey(name: r'eventName')
  final String eventName;

  /// Name of the targeted index.
  @JsonKey(name: r'index')
  final String index;

  /// A user identifier. Depending if the user is logged-in or not, several strategies can be used from a sessionId to a technical identifier. You should always send pseudonymous or anonymous userTokens.
  @JsonKey(name: r'userToken')
  final String userToken;

  /// Time of the event expressed in milliseconds since the Unix epoch.
  @JsonKey(name: r'timestamp')
  final int? timestamp;

  /// Algolia queryID. This is required when an event is tied to a search.
  @JsonKey(name: r'queryID')
  final String? queryID;

  /// An array of index objectID. Limited to 20 objects. An event can’t have both objectIDs and filters at the same time.
  @JsonKey(name: r'objectIDs')
  final List<String>? objectIDs;

  /// An array of filters. Limited to 10 filters. An event can’t have both objectIDs and filters at the same time.
  @JsonKey(name: r'filters')
  final List<String>? filters;

  /// Position of the click in the list of Algolia search results. This field is required if a queryID is provided. One position must be provided for each objectID.
  @JsonKey(name: r'positions')
  final List<int>? positions;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is InsightEvent &&
          other.eventType == eventType &&
          other.eventName == eventName &&
          other.index == index &&
          other.userToken == userToken &&
          other.timestamp == timestamp &&
          other.queryID == queryID &&
          other.objectIDs == objectIDs &&
          other.filters == filters &&
          other.positions == positions;

  @override
  int get hashCode =>
      eventType.hashCode +
      eventName.hashCode +
      index.hashCode +
      userToken.hashCode +
      timestamp.hashCode +
      queryID.hashCode +
      objectIDs.hashCode +
      filters.hashCode +
      positions.hashCode;

  factory InsightEvent.fromJson(Map<String, dynamic> json) =>
      _$InsightEventFromJson(json);

  Map<String, dynamic> toJson() => _$InsightEventToJson(this);

  @override
  String toString() {
    return toJson().toString();
  }
}