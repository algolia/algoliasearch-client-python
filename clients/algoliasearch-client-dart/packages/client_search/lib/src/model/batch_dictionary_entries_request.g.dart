// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'batch_dictionary_entries_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BatchDictionaryEntriesRequest _$BatchDictionaryEntriesRequestFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BatchDictionaryEntriesRequest',
      json,
      ($checkedConvert) {
        final val = BatchDictionaryEntriesRequest(
          action: $checkedConvert(
              'action', (v) => $enumDecode(_$DictionaryActionEnumMap, v)),
          body: $checkedConvert('body',
              (v) => DictionaryEntry.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$BatchDictionaryEntriesRequestToJson(
        BatchDictionaryEntriesRequest instance) =>
    <String, dynamic>{
      'action': _$DictionaryActionEnumMap[instance.action]!,
      'body': instance.body.toJson(),
    };

const _$DictionaryActionEnumMap = {
  DictionaryAction.addEntry: 'addEntry',
  DictionaryAction.deleteEntry: 'deleteEntry',
};
