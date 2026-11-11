# AnalysisQuery

Criteria on a pipeline analysis. Group criteria (medical_condition, species, has_patients, has_healthy) match when any group the analysis ran on matches. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**medical_condition** | [**AnalysisQueryMedicalCondition**](AnalysisQueryMedicalCondition.md) |  | [optional] 
**has_patients** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**has_healthy** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**species** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**task** | [**AnalysisQueryNormalized**](AnalysisQueryNormalized.md) |  | [optional] 
**spatial_scope** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**coordinate_space** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**measure_type** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**measure_family** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**details_type** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**is_meta_analysis** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**n** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**has_coordinates** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**role** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**contrast** | [**AnalysisQueryContrast**](AnalysisQueryContrast.md) |  | [optional] 
**design** | [**AnalysisQueryDesign**](AnalysisQueryDesign.md) |  | [optional] 
**acquisitions** | [**AnalysisQueryAcquisitions**](AnalysisQueryAcquisitions.md) |  | [optional] 
**coordinate_sets** | [**AnalysisQueryCoordinateSets**](AnalysisQueryCoordinateSets.md) |  | [optional] 
**details** | [**AnalysisQueryDetails**](AnalysisQueryDetails.md) |  | [optional] 
**effect** | [**AnalysisQueryEffect**](AnalysisQueryEffect.md) |  | [optional] 
**groups** | [**AnalysisQueryGroups**](AnalysisQueryGroups.md) |  | [optional] 
**inference_settings** | [**AnalysisQueryInferenceSettings**](AnalysisQueryInferenceSettings.md) |  | [optional] 
**model_estimation** | [**AnalysisQueryModelEstimation**](AnalysisQueryModelEstimation.md) |  | [optional] 
**preprocessing** | [**AnalysisQueryPreprocessing**](AnalysisQueryPreprocessing.md) |  | [optional] 
**regions** | [**AnalysisQueryRegions**](AnalysisQueryRegions.md) |  | [optional] 
**tasks** | [**AnalysisQueryTasks**](AnalysisQueryTasks.md) |  | [optional] 
**var_or** | **List[Dict[str, object]]** | Sub-queries, any of which may match; each takes this object&#39;s criteria. (Not a $ref to this schema, which resolvers that inline references cannot expand.)  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query import AnalysisQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQuery from a JSON string
analysis_query_instance = AnalysisQuery.from_json(json)
# print the JSON string representation of the object
print(AnalysisQuery.to_json())

# convert the object into a dict
analysis_query_dict = analysis_query_instance.to_dict()
# create an instance of AnalysisQuery from a dict
analysis_query_from_dict = AnalysisQuery.from_dict(analysis_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


