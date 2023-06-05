// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'dictionary_settings_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

DictionarySettingsParams _$DictionarySettingsParamsFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'DictionarySettingsParams',
      json,
      ($checkedConvert) {
        final val = DictionarySettingsParams(
          disableStandardEntries: $checkedConvert('disableStandardEntries',
              (v) => StandardEntries.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$DictionarySettingsParamsToJson(
        DictionarySettingsParams instance) =>
    <String, dynamic>{
      'disableStandardEntries': instance.disableStandardEntries.toJson(),
    };
