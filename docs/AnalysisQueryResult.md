# AnalysisQueryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **Dict[str, object]** | The query in canonical form, every criterion as any/all/none lists. | [optional] 
**counts** | [**AnalysisQueryResultCounts**](AnalysisQueryResultCounts.md) |  | [optional] 
**searched** | [**AnalysisQueryResultSearched**](AnalysisQueryResultSearched.md) |  | [optional] 
**funnel** | [**List[AnalysisQueryResultFunnelInner]**](AnalysisQueryResultFunnelInner.md) | With &#x60;funnel&#x60;, the criteria in order, each with what remains after it. | [optional] 
**results** | [**List[AnalysisQueryResultResultsInner]**](AnalysisQueryResultResultsInner.md) |  | [optional] 
**study_ids** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_result import AnalysisQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryResult from a JSON string
analysis_query_result_instance = AnalysisQueryResult.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryResult.to_json())

# convert the object into a dict
analysis_query_result_dict = analysis_query_result_instance.to_dict()
# create an instance of AnalysisQueryResult from a dict
analysis_query_result_from_dict = AnalysisQueryResult.from_dict(analysis_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


