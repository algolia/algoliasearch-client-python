// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
// ignore_for_file: unused_element

import 'package:json_annotation/json_annotation.dart';

part 'source.g.dart';

@JsonSerializable()
final class Source {
  /// Returns a new [Source] instance.
  const Source({
    required this.source,
    this.description,
  });

  /// IP address range of the source.
  @JsonKey(name: r'source')
  final String source;

  /// Source description.
  @JsonKey(name: r'description')
  final String? description;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Source &&
          other.source == source &&
          other.description == description;

  @override
  int get hashCode => source.hashCode + description.hashCode;

  factory Source.fromJson(Map<String, dynamic> json) => _$SourceFromJson(json);

  Map<String, dynamic> toJson() => _$SourceToJson(this);

  @override
  String toString() {
    return toJson().toString();
  }
}
