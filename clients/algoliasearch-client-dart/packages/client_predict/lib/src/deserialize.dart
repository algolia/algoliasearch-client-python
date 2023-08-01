import 'package:algolia_client_predict/src/model/activate_model_instance_response.dart';
import 'package:algolia_client_predict/src/model/activate_model_params.dart';
import 'package:algolia_client_predict/src/model/affinity.dart';
import 'package:algolia_client_predict/src/model/all_params.dart';
import 'package:algolia_client_predict/src/model/all_update_segment_params.dart';
import 'package:algolia_client_predict/src/model/compatible_sources.dart';
import 'package:algolia_client_predict/src/model/create_segment_params.dart';
import 'package:algolia_client_predict/src/model/create_segment_response.dart';
import 'package:algolia_client_predict/src/model/delete_model_instance_response.dart';
import 'package:algolia_client_predict/src/model/delete_segment_response.dart';
import 'package:algolia_client_predict/src/model/delete_user_profile_response.dart';
import 'package:algolia_client_predict/src/model/error.dart';
import 'package:algolia_client_predict/src/model/error_base.dart';
import 'package:algolia_client_predict/src/model/fetch_all_user_profiles_response.dart';
import 'package:algolia_client_predict/src/model/funnel_stage.dart';
import 'package:algolia_client_predict/src/model/get_available_model_types_response_inner.dart';
import 'package:algolia_client_predict/src/model/get_available_model_types_response_inner_data_requirements.dart';
import 'package:algolia_client_predict/src/model/get_model_instance_config_status.dart';
import 'package:algolia_client_predict/src/model/get_model_metrics_response.dart';
import 'package:algolia_client_predict/src/model/get_segment_users_response.dart';
import 'package:algolia_client_predict/src/model/limit_param.dart';
import 'package:algolia_client_predict/src/model/model_attributes.dart';
import 'package:algolia_client_predict/src/model/model_instance.dart';
import 'package:algolia_client_predict/src/model/model_metrics.dart';
import 'package:algolia_client_predict/src/model/model_status.dart';
import 'package:algolia_client_predict/src/model/models_to_retrieve.dart';
import 'package:algolia_client_predict/src/model/models_to_retrieve_param.dart';
import 'package:algolia_client_predict/src/model/next_page_token_param.dart';
import 'package:algolia_client_predict/src/model/predictions.dart';
import 'package:algolia_client_predict/src/model/predictions_affinities_success.dart';
import 'package:algolia_client_predict/src/model/predictions_funnel_stage_success.dart';
import 'package:algolia_client_predict/src/model/predictions_order_value_success.dart';
import 'package:algolia_client_predict/src/model/previous_page_token_param.dart';
import 'package:algolia_client_predict/src/model/properties.dart';
import 'package:algolia_client_predict/src/model/segment.dart';
import 'package:algolia_client_predict/src/model/segment_affinity_filter.dart';
import 'package:algolia_client_predict/src/model/segment_child_conditions.dart';
import 'package:algolia_client_predict/src/model/segment_condition_operator.dart';
import 'package:algolia_client_predict/src/model/segment_conditions_param.dart';
import 'package:algolia_client_predict/src/model/segment_filter_operator_boolean.dart';
import 'package:algolia_client_predict/src/model/segment_filter_operator_numerical.dart';
import 'package:algolia_client_predict/src/model/segment_filter_probability.dart';
import 'package:algolia_client_predict/src/model/segment_funnel_stage_filter.dart';
import 'package:algolia_client_predict/src/model/segment_name_param.dart';
import 'package:algolia_client_predict/src/model/segment_operand_affinity.dart';
import 'package:algolia_client_predict/src/model/segment_operand_funnel_stage.dart';
import 'package:algolia_client_predict/src/model/segment_operand_order_value.dart';
import 'package:algolia_client_predict/src/model/segment_operand_property.dart';
import 'package:algolia_client_predict/src/model/segment_order_value_filter.dart';
import 'package:algolia_client_predict/src/model/segment_parent_conditions.dart';
import 'package:algolia_client_predict/src/model/segment_property_filter.dart';
import 'package:algolia_client_predict/src/model/segment_status.dart';
import 'package:algolia_client_predict/src/model/segment_type.dart';
import 'package:algolia_client_predict/src/model/segments.dart';
import 'package:algolia_client_predict/src/model/types_to_retrieve.dart';
import 'package:algolia_client_predict/src/model/types_to_retrieve_param.dart';
import 'package:algolia_client_predict/src/model/update_model_instance_response.dart';
import 'package:algolia_client_predict/src/model/update_model_params.dart';
import 'package:algolia_client_predict/src/model/update_segment_response.dart';
import 'package:algolia_client_predict/src/model/user_profile.dart';

final _regList = RegExp(r'^List<(.*)>$');
final _regSet = RegExp(r'^Set<(.*)>$');
final _regMap = RegExp(r'^Map<String,(.*)>$');

ReturnType deserialize<ReturnType, BaseType>(dynamic value, String targetType,
    {bool growable = true}) {
  switch (targetType) {
    case 'String':
      return '$value' as ReturnType;
    case 'int':
      return (value is int ? value : int.parse('$value')) as ReturnType;
    case 'bool':
      if (value is bool) {
        return value as ReturnType;
      }
      final valueString = '$value'.toLowerCase();
      return (valueString == 'true' || valueString == '1') as ReturnType;
    case 'double':
      return (value is double ? value : double.parse('$value')) as ReturnType;
    case 'ActivateModelInstanceResponse':
      return ActivateModelInstanceResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'ActivateModelParams':
      return ActivateModelParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Affinity':
      return Affinity.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'AllParams':
      return AllParams.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'AllUpdateSegmentParams':
      return AllUpdateSegmentParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'CompatibleSources':
      return CompatibleSources.fromJson(value) as ReturnType;
    case 'CreateSegmentParams':
      return CreateSegmentParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'CreateSegmentResponse':
      return CreateSegmentResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DeleteModelInstanceResponse':
      return DeleteModelInstanceResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DeleteSegmentResponse':
      return DeleteSegmentResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'DeleteUserProfileResponse':
      return DeleteUserProfileResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Error':
      return Error.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ErrorBase':
      return ErrorBase.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'FetchAllUserProfilesResponse':
      return FetchAllUserProfilesResponse.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'FunnelStage':
      return FunnelStage.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'GetAvailableModelTypesResponseInner':
      return GetAvailableModelTypesResponseInner.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetAvailableModelTypesResponseInnerDataRequirements':
      return GetAvailableModelTypesResponseInnerDataRequirements.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'GetModelInstanceConfigStatus':
      return GetModelInstanceConfigStatus.fromJson(value) as ReturnType;
    case 'GetModelMetricsResponse':
      return GetModelMetricsResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'GetSegmentUsersResponse':
      return GetSegmentUsersResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'LimitParam':
      return LimitParam.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ModelAttributes':
      return ModelAttributes.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ModelInstance':
      return ModelInstance.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'ModelMetrics':
      return ModelMetrics.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'ModelStatus':
      return ModelStatus.fromJson(value) as ReturnType;
    case 'ModelsToRetrieve':
      return ModelsToRetrieve.fromJson(value) as ReturnType;
    case 'ModelsToRetrieveParam':
      return ModelsToRetrieveParam.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'NextPageTokenParam':
      return NextPageTokenParam.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Predictions':
      return Predictions.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'PredictionsAffinitiesSuccess':
      return PredictionsAffinitiesSuccess.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'PredictionsFunnelStageSuccess':
      return PredictionsFunnelStageSuccess.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'PredictionsOrderValueSuccess':
      return PredictionsOrderValueSuccess.fromJson(
          value as Map<String, dynamic>) as ReturnType;
    case 'PreviousPageTokenParam':
      return PreviousPageTokenParam.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'Properties':
      return Properties.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'Segment':
      return Segment.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'SegmentAffinityFilter':
      return SegmentAffinityFilter.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentChildConditions':
      return SegmentChildConditions.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentConditionOperator':
      return SegmentConditionOperator.fromJson(value) as ReturnType;
    case 'SegmentConditionsParam':
      return SegmentConditionsParam.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentFilterOperatorBoolean':
      return SegmentFilterOperatorBoolean.fromJson(value) as ReturnType;
    case 'SegmentFilterOperatorNumerical':
      return SegmentFilterOperatorNumerical.fromJson(value) as ReturnType;
    case 'SegmentFilterProbability':
      return SegmentFilterProbability.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentFunnelStageFilter':
      return SegmentFunnelStageFilter.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentNameParam':
      return SegmentNameParam.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentOperandAffinity':
      return SegmentOperandAffinity.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentOperandFunnelStage':
      return SegmentOperandFunnelStage.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentOperandOrderValue':
      return SegmentOperandOrderValue.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentOperandProperty':
      return SegmentOperandProperty.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentOrderValueFilter':
      return SegmentOrderValueFilter.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentParentConditions':
      return SegmentParentConditions.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentPropertyFilter':
      return SegmentPropertyFilter.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'SegmentStatus':
      return SegmentStatus.fromJson(value) as ReturnType;
    case 'SegmentType':
      return SegmentType.fromJson(value) as ReturnType;
    case 'Segments':
      return Segments.fromJson(value as Map<String, dynamic>) as ReturnType;
    case 'TypesToRetrieve':
      return TypesToRetrieve.fromJson(value) as ReturnType;
    case 'TypesToRetrieveParam':
      return TypesToRetrieveParam.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'UpdateModelInstanceResponse':
      return UpdateModelInstanceResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'UpdateModelParams':
      return UpdateModelParams.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'UpdateSegmentResponse':
      return UpdateSegmentResponse.fromJson(value as Map<String, dynamic>)
          as ReturnType;
    case 'UserProfile':
      return UserProfile.fromJson(value as Map<String, dynamic>) as ReturnType;
    default:
      RegExpMatch? match;

      if (value is List && (match = _regList.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return value
            .map<BaseType>((dynamic v) => deserialize<BaseType, BaseType>(
                v, targetType,
                growable: growable))
            .toList(growable: growable) as ReturnType;
      }
      if (value is Set && (match = _regSet.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return value
            .map<BaseType>((dynamic v) => deserialize<BaseType, BaseType>(
                v, targetType,
                growable: growable))
            .toSet() as ReturnType;
      }
      if (value is Map && (match = _regMap.firstMatch(targetType)) != null) {
        targetType = match![1]!; // ignore: parameter_assignments
        return Map<dynamic, BaseType>.fromIterables(
          value.keys,
          value.values.map((dynamic v) => deserialize<BaseType, BaseType>(
              v, targetType,
              growable: growable)),
        ) as ReturnType;
      }
      if (targetType == 'Object') {
        return value;
      }
      break;
  }
  throw Exception('Cannot deserialize');
}
