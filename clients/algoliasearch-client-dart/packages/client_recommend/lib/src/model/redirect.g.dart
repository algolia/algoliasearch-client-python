// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'redirect.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Redirect _$RedirectFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Redirect',
      json,
      ($checkedConvert) {
        final val = Redirect(
          index: $checkedConvert(
              'index',
              (v) => (v as List<dynamic>?)
                  ?.map((e) => RedirectRuleIndexMetadata.fromJson(
                      e as Map<String, dynamic>))
                  .toList()),
        );
        return val;
      },
    );

Map<String, dynamic> _$RedirectToJson(Redirect instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('index', instance.index?.map((e) => e.toJson()).toList());
  return val;
}
