# AnalysisTermListResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**parent** | **str** | The term directly above it (a task&#39;s or a contrast&#39;s family). | [optional] 
**children** | **List[str]** | The terms directly under it. | [optional] 
**synonyms** | **List[str]** |  | [optional] 
**analyses** | **int** |  | [optional] 
**base_studies** | **int** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_term_list_results_inner import AnalysisTermListResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisTermListResultsInner from a JSON string
analysis_term_list_results_inner_instance = AnalysisTermListResultsInner.from_json(json)
# print the JSON string representation of the object
print(AnalysisTermListResultsInner.to_json())

# convert the object into a dict
analysis_term_list_results_inner_dict = analysis_term_list_results_inner_instance.to_dict()
# create an instance of AnalysisTermListResultsInner from a dict
analysis_term_list_results_inner_from_dict = AnalysisTermListResultsInner.from_dict(analysis_term_list_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


