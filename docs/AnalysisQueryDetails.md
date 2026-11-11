# AnalysisQueryDetails

A connectivity analysis's details; regions by their names.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectivity_method** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**inference_target** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**seed_regions** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**target_regions** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_details import AnalysisQueryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryDetails from a JSON string
analysis_query_details_instance = AnalysisQueryDetails.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryDetails.to_json())

# convert the object into a dict
analysis_query_details_dict = analysis_query_details_instance.to_dict()
# create an instance of AnalysisQueryDetails from a dict
analysis_query_details_from_dict = AnalysisQueryDetails.from_dict(analysis_query_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


