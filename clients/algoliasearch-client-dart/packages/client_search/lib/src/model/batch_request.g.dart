// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'batch_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BatchRequest _$BatchRequestFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'BatchRequest',
      json,
      ($checkedConvert) {
        final val = BatchRequest(
          action:
              $checkedConvert('action', (v) => $enumDecode(_$ActionEnumMap, v)),
          body: $checkedConvert('body', (v) => v as Object),
        );
        return val;
      },
    );

Map<String, dynamic> _$BatchRequestToJson(BatchRequest instance) =>
    <String, dynamic>{
      'action': instance.action.toJson(),
      'body': instance.body,
    };

const _$ActionEnumMap = {
  Action.addObject: 'addObject',
  Action.updateObject: 'updateObject',
  Action.partialUpdateObject: 'partialUpdateObject',
  Action.partialUpdateObjectNoCreate: 'partialUpdateObjectNoCreate',
  Action.deleteObject: 'deleteObject',
  Action.delete: 'delete',
  Action.clear: 'clear',
};
