// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_search_response_redirect.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseSearchResponseRedirect _$BaseSearchResponseRedirectFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'BaseSearchResponseRedirect',
      json,
      ($checkedConvert) {
        final val = BaseSearchResponseRedirect(
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

Map<String, dynamic> _$BaseSearchResponseRedirectToJson(
    BaseSearchResponseRedirect instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('index', instance.index?.map((e) => e.toJson()).toList());
  return val;
}
