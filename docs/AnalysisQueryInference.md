# AnalysisQueryInference

The analysis's inference settings. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**height_threshold** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**height_threshold_type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**cluster_extent** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**cluster_threshold** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**correction** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**correction_scope** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**alpha** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**tfce** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**permutations** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_inference import AnalysisQueryInference

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryInference from a JSON string
analysis_query_inference_instance = AnalysisQueryInference.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryInference.to_json())

# convert the object into a dict
analysis_query_inference_dict = analysis_query_inference_instance.to_dict()
# create an instance of AnalysisQueryInference from a dict
analysis_query_inference_from_dict = AnalysisQueryInference.from_dict(analysis_query_inference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


