// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'consequence.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Consequence _$ConsequenceFromJson(Map<String, dynamic> json) => Consequence(
      params: json['params'] == null
          ? null
          : ConsequenceParams.fromJson(json['params'] as Map<String, dynamic>),
      promote: json['promote'] as List<dynamic>?,
      filterPromotes: json['filterPromotes'] as bool?,
      hide_: (json['hide'] as List<dynamic>?)
          ?.map((e) => ConsequenceHide.fromJson(e as Map<String, dynamic>))
          .toList(),
      userData: json['userData'],
    );

Map<String, dynamic> _$ConsequenceToJson(Consequence instance) =>
    <String, dynamic>{
      'params': instance.params,
      'promote': instance.promote?.toList(),
      'filterPromotes': instance.filterPromotes,
      'hide': instance.hide_,
      'userData': instance.userData,
    };
