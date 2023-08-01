// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'run_progress.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

RunProgress _$RunProgressFromJson(Map<String, dynamic> json) => $checkedCreate(
      'RunProgress',
      json,
      ($checkedConvert) {
        final val = RunProgress(
          expectedNbOfEvents:
              $checkedConvert('expectedNbOfEvents', (v) => v as int?),
          receivedNbOfEvents:
              $checkedConvert('receivedNbOfEvents', (v) => v as int?),
        );
        return val;
      },
    );

Map<String, dynamic> _$RunProgressToJson(RunProgress instance) {
  final val = <String, dynamic>{};

  void writeNotNull(String key, dynamic value) {
    if (value != null) {
      val[key] = value;
    }
  }

  writeNotNull('expectedNbOfEvents', instance.expectedNbOfEvents);
  writeNotNull('receivedNbOfEvents', instance.receivedNbOfEvents);
  return val;
}
