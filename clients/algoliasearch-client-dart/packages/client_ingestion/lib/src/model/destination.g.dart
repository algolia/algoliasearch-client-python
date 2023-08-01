// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'destination.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Destination _$DestinationFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Destination',
      json,
      ($checkedConvert) {
        final val = Destination(
          destinationID: $checkedConvert('destinationID', (v) => v as String),
          type: $checkedConvert(
              'type', (v) => $enumDecode(_$DestinationTypeEnumMap, v)),
          name: $checkedConvert('name', (v) => v as String),
          input: $checkedConvert('input', (v) => v),
          createdAt: $checkedConvert('createdAt', (v) => v as String),
          updatedAt: $checkedConvert('updatedAt', (v) => v as String?),
          authenticationID:
              $checkedConvert('authenticationID', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$DestinationToJson(Destination instance) {
  final val = <String, dynamic>{
    'destinationID': instance.destinationID,
    'type': instance.type.toJson(),
    'name': instance.name,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('input', instance.input);
  val['createdAt'] = instance.createdAt;
  writeNotNull('updatedAt', instance.updatedAt);
  writeNotNull('authenticationID', instance.authenticationID);
  return val;
}

const _$DestinationTypeEnumMap = {
  DestinationType.search: 'search',
  DestinationType.insights: 'insights',
  DestinationType.flow: 'flow',
  DestinationType.predict: 'predict',
};
