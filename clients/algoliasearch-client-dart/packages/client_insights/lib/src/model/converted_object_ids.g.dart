// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'converted_object_ids.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ConvertedObjectIDs _$ConvertedObjectIDsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'ConvertedObjectIDs',
      json,
      ($checkedConvert) {
        final val = ConvertedObjectIDs(
          eventName: $checkedConvert('eventName', (v) => v as String),
          eventType: $checkedConvert(
              'eventType', (v) => $enumDecode(_$ConversionEventEnumMap, v)),
          index: $checkedConvert('index', (v) => v as String),
          objectIDs: $checkedConvert('objectIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
          userToken: $checkedConvert('userToken', (v) => v as String),
          timestamp: $checkedConvert('timestamp', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$ConvertedObjectIDsToJson(ConvertedObjectIDs instance) {
  final val = <String, dynamic>{
    'eventName': instance.eventName,
    'eventType': instance.eventType.toJson(),
    'index': instance.index,
    'objectIDs': instance.objectIDs,
    'userToken': instance.userToken,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('timestamp', instance.timestamp);
  return val;
}

const _$ConversionEventEnumMap = {
  ConversionEvent.conversion: 'conversion',
};
