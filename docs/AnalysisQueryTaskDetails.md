# AnalysisQueryTaskDetails

The analysis's tasks beyond their paradigm: stimuli and stimulus content, modalities, design, instructions and performance measures. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stimuli** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**stimulus_modality** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**response_modality** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**design_type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**instructions** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**performance** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_task_details import AnalysisQueryTaskDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryTaskDetails from a JSON string
analysis_query_task_details_instance = AnalysisQueryTaskDetails.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryTaskDetails.to_json())

# convert the object into a dict
analysis_query_task_details_dict = analysis_query_task_details_instance.to_dict()
# create an instance of AnalysisQueryTaskDetails from a dict
analysis_query_task_details_from_dict = AnalysisQueryTaskDetails.from_dict(analysis_query_task_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


