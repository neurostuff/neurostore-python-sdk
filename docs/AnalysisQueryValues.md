# AnalysisQueryValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | **List[str]** |  | [optional] 
**all** | **List[str]** |  | [optional] 
**var_none** | **List[str]** |  | [optional] 
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_values import AnalysisQueryValues

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryValues from a JSON string
analysis_query_values_instance = AnalysisQueryValues.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryValues.to_json())

# convert the object into a dict
analysis_query_values_dict = analysis_query_values_instance.to_dict()
# create an instance of AnalysisQueryValues from a dict
analysis_query_values_from_dict = AnalysisQueryValues.from_dict(analysis_query_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


