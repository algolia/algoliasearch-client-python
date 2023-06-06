// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'redirect_rule_index_metadata_data.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RedirectRuleIndexMetadataData _$RedirectRuleIndexMetadataDataFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'RedirectRuleIndexMetadataData',
      json,
      ($checkedConvert) {
        final val = RedirectRuleIndexMetadataData(
          ruleObjectID: $checkedConvert('ruleObjectID', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$RedirectRuleIndexMetadataDataToJson(
        RedirectRuleIndexMetadataData instance) =>
    <String, dynamic>{
      'ruleObjectID': instance.ruleObjectID,
    };
