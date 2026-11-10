# AnalysisQueryConnectivity

A connectivity analysis's method and inference target, and its seed and target regions' names. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**inference_target** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**seed** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**target** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_connectivity import AnalysisQueryConnectivity

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryConnectivity from a JSON string
analysis_query_connectivity_instance = AnalysisQueryConnectivity.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryConnectivity.to_json())

# convert the object into a dict
analysis_query_connectivity_dict = analysis_query_connectivity_instance.to_dict()
# create an instance of AnalysisQueryConnectivity from a dict
analysis_query_connectivity_from_dict = AnalysisQueryConnectivity.from_dict(analysis_query_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


