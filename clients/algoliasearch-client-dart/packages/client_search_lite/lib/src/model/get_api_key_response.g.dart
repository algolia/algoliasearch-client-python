// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'get_api_key_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

GetApiKeyResponse _$GetApiKeyResponseFromJson(Map<String, dynamic> json) =>
    GetApiKeyResponse(
      value: json['value'] as String?,
      createdAt: json['createdAt'] as int,
      acl: (json['acl'] as List<dynamic>)
          .map((e) => $enumDecode(_$AclEnumMap, e))
          .toList(),
      description: json['description'] as String?,
      indexes:
          (json['indexes'] as List<dynamic>?)?.map((e) => e as String).toList(),
      maxHitsPerQuery: json['maxHitsPerQuery'] as int?,
      maxQueriesPerIPPerHour: json['maxQueriesPerIPPerHour'] as int?,
      queryParameters: json['queryParameters'] as String?,
      referers: (json['referers'] as List<dynamic>?)
          ?.map((e) => e as String)
          .toList(),
      validity: json['validity'] as int?,
    );

Map<String, dynamic> _$GetApiKeyResponseToJson(GetApiKeyResponse instance) =>
    <String, dynamic>{
      'value': instance.value,
      'createdAt': instance.createdAt,
      'acl': instance.acl.map((e) => _$AclEnumMap[e]!).toList(),
      'description': instance.description,
      'indexes': instance.indexes,
      'maxHitsPerQuery': instance.maxHitsPerQuery,
      'maxQueriesPerIPPerHour': instance.maxQueriesPerIPPerHour,
      'queryParameters': instance.queryParameters,
      'referers': instance.referers,
      'validity': instance.validity,
    };

const _$AclEnumMap = {
  Acl.addObject: 'addObject',
  Acl.analytics: 'analytics',
  Acl.browse: 'browse',
  Acl.deleteObject: 'deleteObject',
  Acl.deleteIndex: 'deleteIndex',
  Acl.editSettings: 'editSettings',
  Acl.listIndexes: 'listIndexes',
  Acl.logs: 'logs',
  Acl.personalization: 'personalization',
  Acl.recommendation: 'recommendation',
  Acl.search: 'search',
  Acl.seeUnretrievableAttributes: 'seeUnretrievableAttributes',
  Acl.settings: 'settings',
  Acl.usage: 'usage',
};
