// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'rule_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RuleResponse _$RuleResponseFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'RuleResponse',
      json,
      ($checkedConvert) {
        final val = RuleResponse(
          metadata: $checkedConvert(
              '_metadata',
              (v) => v == null
                  ? null
                  : RuleResponseMetadata.fromJson(v as Map<String, dynamic>)),
          objectID: $checkedConvert('objectID', (v) => v as String),
          conditions: $checkedConvert(
              'conditions',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => Condition.fromJson(e as Map<String, dynamic>))
                  .toList()),
          consequence: $checkedConvert(
              'consequence',
              (v) => v == null
                  ? null
                  : Consequence.fromJson(v as Map<String, dynamic>)),
          description: $checkedConvert('description', (v) => v as String?),
          enabled: $checkedConvert('enabled', (v) => v as bool?),
        );
        return val;
      },
      fieldKeyMap: const {'metadata': '_metadata'},
    );

Map<String, dynamic> _$RuleResponseToJson(RuleResponse instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('_metadata', instance.metadata?.toJson());
  val['objectID'] = instance.objectID;
  writeNotNull(
      'conditions', instance.conditions?.map((e) => e.toJson()).toList());
  writeNotNull('consequence', instance.consequence?.toJson());
  writeNotNull('description', instance.description);
  writeNotNull('enabled', instance.enabled);
  return val;
}
