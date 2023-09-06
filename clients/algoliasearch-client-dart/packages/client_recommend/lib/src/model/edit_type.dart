// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
// ignore_for_file: unused_element
import 'package:json_annotation/json_annotation.dart';

/// Type of edit.
@JsonEnum(valueField: 'raw')
enum EditType {
  remove(r'remove'),
  replace(r'replace');

  const EditType(this.raw);
  final dynamic raw;

  dynamic toJson() => raw;

  static EditType fromJson(dynamic json) {
    for (final value in values) {
      if (value.raw == json) return value;
    }
    throw ArgumentError.value(json, "raw", "No enum value with that value");
  }

  @override
  String toString() => raw.toString();
}
