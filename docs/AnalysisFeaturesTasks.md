# AnalysisFeaturesTasks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stimuli** | **List[str]** |  | [optional] 
**stimulus_modality** | **List[str]** |  | [optional] 
**response_modality** | **List[str]** |  | [optional] 
**design_type** | **List[str]** |  | [optional] 
**instructions** | **List[str]** |  | [optional] 
**performance_measures** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_tasks import AnalysisFeaturesTasks

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesTasks from a JSON string
analysis_features_tasks_instance = AnalysisFeaturesTasks.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesTasks.to_json())

# convert the object into a dict
analysis_features_tasks_dict = analysis_features_tasks_instance.to_dict()
# create an instance of AnalysisFeaturesTasks from a dict
analysis_features_tasks_from_dict = AnalysisFeaturesTasks.from_dict(analysis_features_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


