// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'list_authentications_response.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ListAuthenticationsResponse _$ListAuthenticationsResponseFromJson(
        Map<String, dynamic> json) =>
    $checkedCreate(
      'ListAuthenticationsResponse',
      json,
      ($checkedConvert) {
        final val = ListAuthenticationsResponse(
          authentications: $checkedConvert(
              'authentications',
              (v) => (v as List<dynamic>)
                  .map(
                      (e) => Authentication.fromJson(e as Map<String, dynamic>))
                  .toList()),
          pagination: $checkedConvert('pagination',
              (v) => Pagination.fromJson(v as Map<String, dynamic>)),
        );
        return val;
      },
    );

Map<String, dynamic> _$ListAuthenticationsResponseToJson(
        ListAuthenticationsResponse instance) =>
    <String, dynamic>{
      'authentications':
          instance.authentications.map((e) => e.toJson()).toList(),
      'pagination': instance.pagination.toJson(),
    };
