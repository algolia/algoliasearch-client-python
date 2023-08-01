// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'affinity.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Affinity _$AffinityFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Affinity',
      json,
      ($checkedConvert) {
        final val = Affinity(
          name: $checkedConvert('name', (v) => v as String),
          value: $checkedConvert('value', (v) => v),
          probability:
              $checkedConvert('probability', (v) => (v as num).toDouble()),
        );
        return val;
      },
    );

Map<String, dynamic> _$AffinityToJson(Affinity instance) {
  final val = <String, dynamic>{
    'name': instance.name,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('value', instance.value);
  val['probability'] = instance.probability;
  return val;
}
