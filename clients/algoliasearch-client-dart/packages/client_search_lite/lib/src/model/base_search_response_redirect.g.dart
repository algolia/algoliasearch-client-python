// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'base_search_response_redirect.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

BaseSearchResponseRedirect _$BaseSearchResponseRedirectFromJson(
        Map<String, dynamic> json) =>
    BaseSearchResponseRedirect(
      index: (json['index'] as List<dynamic>?)
          ?.map((e) =>
              RedirectRuleIndexMetadata.fromJson(e as Map<String, dynamic>))
          .toList(),
    );

Map<String, dynamic> _$BaseSearchResponseRedirectToJson(
        BaseSearchResponseRedirect instance) =>
    <String, dynamic>{
      'index': instance.index,
    };
