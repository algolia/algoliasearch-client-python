// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'added_to_cart_object_ids.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AddedToCartObjectIDs _$AddedToCartObjectIDsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'AddedToCartObjectIDs',
      json,
      ($checkedConvert) {
        final val = AddedToCartObjectIDs(
          eventName: $checkedConvert('eventName', (v) => v as String),
          eventType: $checkedConvert(
              'eventType', (v) => $enumDecode(_$ConversionEventEnumMap, v)),
          eventSubtype: $checkedConvert(
              'eventSubtype', (v) => $enumDecode(_$AddToCartEventEnumMap, v)),
          index: $checkedConvert('index', (v) => v as String),
          objectIDs: $checkedConvert('objectIDs',
              (v) => (v as List<dynamic>).map((e) => e as String).toList()),
          objectData: $checkedConvert(
              'objectData',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => ObjectData.fromJson(e as Map<String, dynamic>))
                  .toList()),
          currency: $checkedConvert('currency', (v) => v as String?),
          userToken: $checkedConvert('userToken', (v) => v as String),
          timestamp: $checkedConvert('timestamp', (v) => v as int?),
          authenticatedUserToken:
              $checkedConvert('authenticatedUserToken', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$AddedToCartObjectIDsToJson(
    AddedToCartObjectIDs instance) {
  final val = <String, dynamic>{
    'eventName': instance.eventName,
    'eventType': instance.eventType.toJson(),
    'eventSubtype': instance.eventSubtype.toJson(),
    'index': instance.index,
    'objectIDs': instance.objectIDs,
  };

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull(
      'objectData', instance.objectData?.map((e) => e.toJson()).toList());
  writeNotNull('currency', instance.currency);
  val['userToken'] = instance.userToken;
  writeNotNull('timestamp', instance.timestamp);
  writeNotNull('authenticatedUserToken', instance.authenticatedUserToken);
  return val;
}

const _$ConversionEventEnumMap = {
  ConversionEvent.conversion: 'conversion',
};

const _$AddToCartEventEnumMap = {
  AddToCartEvent.addToCart: 'addToCart',
};
