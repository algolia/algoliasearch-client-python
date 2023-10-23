// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'identify.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Identify _$IdentifyFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Identify',
      json,
      ($checkedConvert) {
        final val = Identify(
          eventType: $checkedConvert(
              'eventType', (v) => $enumDecode(_$IdentifyEventEnumMap, v)),
          userToken: $checkedConvert('userToken', (v) => v as String),
          authenticatedUserToken:
              $checkedConvert('authenticatedUserToken', (v) => v as String),
        );
        return val;
      },
    );

Map<String, dynamic> _$IdentifyToJson(Identify instance) => <String, dynamic>{
      'eventType': instance.eventType.toJson(),
      'userToken': instance.userToken,
      'authenticatedUserToken': instance.authenticatedUserToken,
    };

const _$IdentifyEventEnumMap = {
  IdentifyEvent.identify: 'identify',
};
