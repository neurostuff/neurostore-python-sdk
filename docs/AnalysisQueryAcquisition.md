# AnalysisQueryAcquisition

The analysis's acquisitions; a criterion on a number matches when any acquisition's does. Field strength in tesla, repetition and echo time in seconds, voxel size as the largest dimension in millimetres. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modality** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**field_strength** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**repetition_time** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**echo_time** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**voxel_size** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**scanner** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_acquisition import AnalysisQueryAcquisition

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryAcquisition from a JSON string
analysis_query_acquisition_instance = AnalysisQueryAcquisition.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryAcquisition.to_json())

# convert the object into a dict
analysis_query_acquisition_dict = analysis_query_acquisition_instance.to_dict()
# create an instance of AnalysisQueryAcquisition from a dict
analysis_query_acquisition_from_dict = AnalysisQueryAcquisition.from_dict(analysis_query_acquisition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


