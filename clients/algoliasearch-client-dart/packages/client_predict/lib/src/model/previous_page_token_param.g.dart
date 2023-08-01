// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'previous_page_token_param.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PreviousPageTokenParam _$PreviousPageTokenParamFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'PreviousPageTokenParam',
      json,
      ($checkedConvert) {
        final val = PreviousPageTokenParam(
          previousPageToken:
              $checkedConvert('previousPageToken', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$PreviousPageTokenParamToJson(
    PreviousPageTokenParam instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('previousPageToken', instance.previousPageToken);
  return val;
}
