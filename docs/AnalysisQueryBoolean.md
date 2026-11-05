# AnalysisQueryBoolean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_is** | **bool** |  | 
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_boolean import AnalysisQueryBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryBoolean from a JSON string
analysis_query_boolean_instance = AnalysisQueryBoolean.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryBoolean.to_json())

# convert the object into a dict
analysis_query_boolean_dict = analysis_query_boolean_instance.to_dict()
# create an instance of AnalysisQueryBoolean from a dict
analysis_query_boolean_from_dict = AnalysisQueryBoolean.from_dict(analysis_query_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


