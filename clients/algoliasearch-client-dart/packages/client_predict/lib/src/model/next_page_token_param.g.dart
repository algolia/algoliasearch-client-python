// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'next_page_token_param.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

NextPageTokenParam _$NextPageTokenParamFromJson(Map<String, dynamic> json) =>
    $checkedCreate(
      'NextPageTokenParam',
      json,
      ($checkedConvert) {
        final val = NextPageTokenParam(
          nextPageToken: $checkedConvert('nextPageToken', (v) => v as String?),
        );
        return val;
      },
    );

Map<String, dynamic> _$NextPageTokenParamToJson(NextPageTokenParam instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('nextPageToken', instance.nextPageToken);
  return val;
}
