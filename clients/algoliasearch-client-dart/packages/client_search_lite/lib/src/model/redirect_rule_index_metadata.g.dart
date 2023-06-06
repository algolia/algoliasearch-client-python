// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'redirect_rule_index_metadata.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RedirectRuleIndexMetadata _$RedirectRuleIndexMetadataFromJson(
        Map<String, dynamic> json) =>
    RedirectRuleIndexMetadata(
      source_: json['source'] as String,
      dest: json['dest'] as String,
      reason: json['reason'] as String,
      succeed: json['succeed'] as bool,
      data: RedirectRuleIndexMetadataData.fromJson(
          json['data'] as Map<String, dynamic>),
    );

Map<String, dynamic> _$RedirectRuleIndexMetadataToJson(
        RedirectRuleIndexMetadata instance) =>
    <String, dynamic>{
      'source': instance.source_,
      'dest': instance.dest,
      'reason': instance.reason,
      'succeed': instance.succeed,
      'data': instance.data,
    };
