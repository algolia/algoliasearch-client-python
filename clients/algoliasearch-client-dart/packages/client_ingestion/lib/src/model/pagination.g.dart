// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'pagination.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Pagination _$PaginationFromJson(Map<String, dynamic> json) => $checkedCreate(
      'Pagination',
      json,
      ($checkedConvert) {
        final val = Pagination(
          nbPages: $checkedConvert('nbPages', (v) => v as int),
          page: $checkedConvert('page', (v) => v as int),
          nbItems: $checkedConvert('nbItems', (v) => v as int),
          itemsPerPage: $checkedConvert('itemsPerPage', (v) => v as int),
        );
        return val;
      },
    );

Map<String, dynamic> _$PaginationToJson(Pagination instance) =>
    <String, dynamic>{
      'nbPages': instance.nbPages,
      'page': instance.page,
      'nbItems': instance.nbItems,
      'itemsPerPage': instance.itemsPerPage,
    };
