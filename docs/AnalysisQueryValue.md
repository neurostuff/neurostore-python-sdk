# AnalysisQueryValue

Values matched whole: a value, a list of values (any of them), or any/all/none lists. Unlike a text criterion, no pattern and no minimum length. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | **List[str]** |  | [optional] 
**all** | **List[str]** |  | [optional] 
**var_none** | **List[str]** |  | [optional] 
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_value import AnalysisQueryValue

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryValue from a JSON string
analysis_query_value_instance = AnalysisQueryValue.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryValue.to_json())

# convert the object into a dict
analysis_query_value_dict = analysis_query_value_instance.to_dict()
# create an instance of AnalysisQueryValue from a dict
analysis_query_value_from_dict = AnalysisQueryValue.from_dict(analysis_query_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


