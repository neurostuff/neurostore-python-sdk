# AnalysisQueryTasks

The analysis's tasks beyond their paradigm; stimuli include their stimulus content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stimuli** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**stimulus_modality** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**response_modality** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**design_type** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**instructions** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**performance_measures** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_tasks import AnalysisQueryTasks

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryTasks from a JSON string
analysis_query_tasks_instance = AnalysisQueryTasks.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryTasks.to_json())

# convert the object into a dict
analysis_query_tasks_dict = analysis_query_tasks_instance.to_dict()
# create an instance of AnalysisQueryTasks from a dict
analysis_query_tasks_from_dict = AnalysisQueryTasks.from_dict(analysis_query_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


