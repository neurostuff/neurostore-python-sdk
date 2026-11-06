# AnalysisQueryResultResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | **str** |  | [optional] 
**study** | **str** |  | [optional] 
**base_study** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**matched_by** | **Dict[str, str]** | How the analysis matched each normalized criterion, by its path (&#x60;medical_condition&#x60;, &#x60;or[0].task&#x60;): by id, by text, as unmapped or as silent (under &#x60;include&#x60;). Absent where a mapped analysis matched only through &#x60;none&#x60;.  | [optional] 
**features** | **Dict[str, object]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_result_results_inner import AnalysisQueryResultResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryResultResultsInner from a JSON string
analysis_query_result_results_inner_instance = AnalysisQueryResultResultsInner.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryResultResultsInner.to_json())

# convert the object into a dict
analysis_query_result_results_inner_dict = analysis_query_result_results_inner_instance.to_dict()
# create an instance of AnalysisQueryResultResultsInner from a dict
analysis_query_result_results_inner_from_dict = AnalysisQueryResultResultsInner.from_dict(analysis_query_result_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


