# AnalysisQueryRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_range import AnalysisQueryRange

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryRange from a JSON string
analysis_query_range_instance = AnalysisQueryRange.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryRange.to_json())

# convert the object into a dict
analysis_query_range_dict = analysis_query_range_instance.to_dict()
# create an instance of AnalysisQueryRange from a dict
analysis_query_range_from_dict = AnalysisQueryRange.from_dict(analysis_query_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


