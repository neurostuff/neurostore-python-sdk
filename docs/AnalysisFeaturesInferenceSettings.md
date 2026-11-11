# AnalysisFeaturesInferenceSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inference_level** | **List[str]** |  | [optional] 
**height_threshold_value** | **float** |  | [optional] 
**height_threshold_type** | **List[str]** |  | [optional] 
**cluster_extent_threshold** | **int** |  | [optional] 
**clusterwise_threshold_value** | **float** |  | [optional] 
**multiple_comparison_method** | **List[str]** |  | [optional] 
**correction_scope** | **str** |  | [optional] 
**alpha_level** | **float** |  | [optional] 
**tfce_used** | **bool** |  | [optional] 
**permutation_count** | **int** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_inference_settings import AnalysisFeaturesInferenceSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesInferenceSettings from a JSON string
analysis_features_inference_settings_instance = AnalysisFeaturesInferenceSettings.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesInferenceSettings.to_json())

# convert the object into a dict
analysis_features_inference_settings_dict = analysis_features_inference_settings_instance.to_dict()
# create an instance of AnalysisFeaturesInferenceSettings from a dict
analysis_features_inference_settings_from_dict = AnalysisFeaturesInferenceSettings.from_dict(analysis_features_inference_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


