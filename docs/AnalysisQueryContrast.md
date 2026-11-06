# AnalysisQueryContrast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positive** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**negative** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**key** | [**AnalysisQueryNormalizedIds**](AnalysisQueryNormalizedIds.md) |  | [optional] 
**set** | [**AnalysisQueryNormalizedIds**](AnalysisQueryNormalizedIds.md) |  | [optional] 
**kind** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**groups** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_contrast import AnalysisQueryContrast

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryContrast from a JSON string
analysis_query_contrast_instance = AnalysisQueryContrast.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryContrast.to_json())

# convert the object into a dict
analysis_query_contrast_dict = analysis_query_contrast_instance.to_dict()
# create an instance of AnalysisQueryContrast from a dict
analysis_query_contrast_from_dict = AnalysisQueryContrast.from_dict(analysis_query_contrast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


