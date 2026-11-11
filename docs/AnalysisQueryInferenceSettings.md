# AnalysisQueryInferenceSettings

The analysis's inference settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inference_level** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**height_threshold_value** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**height_threshold_type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**cluster_extent_threshold** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**clusterwise_threshold_value** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**multiple_comparison_method** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**correction_scope** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**alpha_level** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**tfce_used** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**permutation_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_inference_settings import AnalysisQueryInferenceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryInferenceSettings from a JSON string
analysis_query_inference_settings_instance = AnalysisQueryInferenceSettings.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryInferenceSettings.to_json())

# convert the object into a dict
analysis_query_inference_settings_dict = analysis_query_inference_settings_instance.to_dict()
# create an instance of AnalysisQueryInferenceSettings from a dict
analysis_query_inference_settings_from_dict = AnalysisQueryInferenceSettings.from_dict(analysis_query_inference_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


