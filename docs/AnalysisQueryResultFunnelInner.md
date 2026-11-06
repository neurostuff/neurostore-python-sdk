# AnalysisQueryResultFunnelInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterion** | **str** |  | [optional] 
**analyses** | **int** |  | [optional] 
**base_studies** | **int** |  | [optional] 
**dropped** | **int** |  | [optional] 
**silent** | **int** | Analyses left by the criteria before this one whose record says nothing on it. | [optional] 
**unmapped** | **int** | For a normalized criterion, the analyses left by the criteria before this one whose record states the feature but maps none of it.  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_result_funnel_inner import AnalysisQueryResultFunnelInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryResultFunnelInner from a JSON string
analysis_query_result_funnel_inner_instance = AnalysisQueryResultFunnelInner.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryResultFunnelInner.to_json())

# convert the object into a dict
analysis_query_result_funnel_inner_dict = analysis_query_result_funnel_inner_instance.to_dict()
# create an instance of AnalysisQueryResultFunnelInner from a dict
analysis_query_result_funnel_inner_from_dict = AnalysisQueryResultFunnelInner.from_dict(analysis_query_result_funnel_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


