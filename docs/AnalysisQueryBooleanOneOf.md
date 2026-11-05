# AnalysisQueryBooleanOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_is** | **bool** |  | 
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_boolean_one_of import AnalysisQueryBooleanOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryBooleanOneOf from a JSON string
analysis_query_boolean_one_of_instance = AnalysisQueryBooleanOneOf.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryBooleanOneOf.to_json())

# convert the object into a dict
analysis_query_boolean_one_of_dict = analysis_query_boolean_one_of_instance.to_dict()
# create an instance of AnalysisQueryBooleanOneOf from a dict
analysis_query_boolean_one_of_from_dict = AnalysisQueryBooleanOneOf.from_dict(analysis_query_boolean_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


