# AnalysisQueryText

A value, a list of values (any of them), or any/all/none lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | **List[str]** |  | [optional] 
**all** | **List[str]** |  | [optional] 
**var_none** | **List[str]** |  | [optional] 
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_text import AnalysisQueryText

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryText from a JSON string
analysis_query_text_instance = AnalysisQueryText.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryText.to_json())

# convert the object into a dict
analysis_query_text_dict = analysis_query_text_instance.to_dict()
# create an instance of AnalysisQueryText from a dict
analysis_query_text_from_dict = AnalysisQueryText.from_dict(analysis_query_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


