# AnalysisTermList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AnalysisTermListResultsInner]**](AnalysisTermListResultsInner.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_term_list import AnalysisTermList

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisTermList from a JSON string
analysis_term_list_instance = AnalysisTermList.from_json(json)
# print the JSON string representation of the object
print(AnalysisTermList.to_json())

# convert the object into a dict
analysis_term_list_dict = analysis_term_list_instance.to_dict()
# create an instance of AnalysisTermList from a dict
analysis_term_list_from_dict = AnalysisTermList.from_dict(analysis_term_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


