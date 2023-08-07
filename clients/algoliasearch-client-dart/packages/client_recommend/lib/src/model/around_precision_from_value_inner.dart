// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
// ignore_for_file: unused_element

import 'package:json_annotation/json_annotation.dart';

part 'around_precision_from_value_inner.g.dart';

@JsonSerializable()
final class AroundPrecisionFromValueInner {
  /// Returns a new [AroundPrecisionFromValueInner] instance.
  const AroundPrecisionFromValueInner({
    this.from,
    this.value,
  });

  @JsonKey(name: r'from')
  final int? from;

  @JsonKey(name: r'value')
  final int? value;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is AroundPrecisionFromValueInner &&
          other.from == from &&
          other.value == value;

  @override
  int get hashCode => from.hashCode + value.hashCode;

  factory AroundPrecisionFromValueInner.fromJson(Map<String, dynamic> json) =>
      _$AroundPrecisionFromValueInnerFromJson(json);

  Map<String, dynamic> toJson() => _$AroundPrecisionFromValueInnerToJson(this);

  @override
  String toString() {
    return toJson().toString();
  }
}
