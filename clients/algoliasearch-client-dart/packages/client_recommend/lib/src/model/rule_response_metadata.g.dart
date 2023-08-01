// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'rule_response_metadata.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RuleResponseMetadata _$RuleResponseMetadataFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'RuleResponseMetadata',
      json,
      ($checkedConvert) {
        final val = RuleResponseMetadata(
          lastUpdate: $checkedConvert('lastUpdate', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$RuleResponseMetadataToJson(
    RuleResponseMetadata instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('lastUpdate', instance.lastUpdate);
  return val;
}
