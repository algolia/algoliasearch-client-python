// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'destination_update.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DestinationUpdate _$DestinationUpdateFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'DestinationUpdate',
      json,
      ($checkedConvert) {
        final val = DestinationUpdate(
          type: $checkedConvert(
              'type', (v) => $enumDecodeNullable(_$DestinationTypeEnumMap, v)),
          name: $checkedConvert('name', (v) => v as String?),
          input: $checkedConvert('input', (v) => v),
          authenticationID:
              $checkedConvert('authenticationID', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$DestinationUpdateToJson(DestinationUpdate instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('type', instance.type?.toJson());
  writeNotNull('name', instance.name);
  writeNotNull('input', instance.input);
  writeNotNull('authenticationID', instance.authenticationID);
  return val;
}

const _$DestinationTypeEnumMap = {
  DestinationType.search: 'search',
  DestinationType.insights: 'insights',
  DestinationType.flow: 'flow',
  DestinationType.predict: 'predict',
};
