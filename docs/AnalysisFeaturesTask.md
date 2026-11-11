# AnalysisFeaturesTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 
**family_ids** | **List[str]** |  | [optional] 
**text** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_task import AnalysisFeaturesTask

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesTask from a JSON string
analysis_features_task_instance = AnalysisFeaturesTask.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesTask.to_json())

# convert the object into a dict
analysis_features_task_dict = analysis_features_task_instance.to_dict()
# create an instance of AnalysisFeaturesTask from a dict
analysis_features_task_from_dict = AnalysisFeaturesTask.from_dict(analysis_features_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


