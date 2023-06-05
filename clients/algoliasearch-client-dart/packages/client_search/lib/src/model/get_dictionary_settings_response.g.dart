// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_dictionary_settings_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetDictionarySettingsResponse _$GetDictionarySettingsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'GetDictionarySettingsResponse',
      json,
      ($checkedConvert) {
        final val = GetDictionarySettingsResponse(
          disableStandardEntries: $checkedConvert('disableStandardEntries',
              (v) => StandardEntries.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$GetDictionarySettingsResponseToJson(
        GetDictionarySettingsResponse instance) =>
    <String, dynamic>{
      'disableStandardEntries': instance.disableStandardEntries.toJson(),
    };
