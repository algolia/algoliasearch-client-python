// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'custom_search_params.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

CustomSearchParams _$CustomSearchParamsFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'CustomSearchParams',
      json,
      ($checkedConvert) {
        final val = CustomSearchParams(
          customSearchParameters:
              $checkedConvert('customSearchParameters', (v) => v as Object),
        );
        return val;
      },
    );

Map<String, dynamic> _$CustomSearchParamsToJson(CustomSearchParams instance) =>
    <String, dynamic>{
      'customSearchParameters': instance.customSearchParameters,
    };
