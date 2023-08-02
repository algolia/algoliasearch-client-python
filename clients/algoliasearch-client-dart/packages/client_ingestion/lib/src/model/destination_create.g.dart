// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'destination_create.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DestinationCreate _$DestinationCreateFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'DestinationCreate',
      json,
      ($checkedConvert) {
        final val = DestinationCreate(
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$DestinationTypeEnumMap, v)),
          name: $checkedConvert('name', (v) => v as String),
          input: $checkedConvert('input', (v) => v),
          authenticationID:
              $checkedConvert('authenticationID', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$DestinationCreateToJson(DestinationCreate instance) {
  final val = <String, dynamic>{
    'type': instance.type.toJson(),
    'name': instance.name,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('input', instance.input);
  writeNotNull('authenticationID', instance.authenticationID);
  return val;
}

const _$DestinationTypeEnumMap = {
  DestinationType.search: 'search',
  DestinationType.insights: 'insights',
  DestinationType.flow: 'flow',
};
