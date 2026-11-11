# AnalysisQueryAcquisitions

The analysis's acquisitions; a number matches when any acquisition's does. The voxel size is an acquisition's largest dimension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modality** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**magnetic_field_strength_tesla** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**repetition_time_seconds** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**echo_time_seconds** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**acquisition_voxel_size_mm** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**device** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_acquisitions import AnalysisQueryAcquisitions

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryAcquisitions from a JSON string
analysis_query_acquisitions_instance = AnalysisQueryAcquisitions.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryAcquisitions.to_json())

# convert the object into a dict
analysis_query_acquisitions_dict = analysis_query_acquisitions_instance.to_dict()
# create an instance of AnalysisQueryAcquisitions from a dict
analysis_query_acquisitions_from_dict = AnalysisQueryAcquisitions.from_dict(analysis_query_acquisitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


