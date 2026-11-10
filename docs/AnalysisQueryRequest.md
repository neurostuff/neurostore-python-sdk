# AnalysisQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**AnalysisQuery**](AnalysisQuery.md) |  | 
**page** | **int** | Which page of studies to list, in order of paper. | [optional] [default to 1]
**page_size** | **int** | How many studies a page lists, each with all its selected analyses; 0 lists none.  | [optional] [default to 20]
**paginate** | **bool** | False lists every selected study, whatever &#x60;page&#x60; and &#x60;page_size&#x60; say. | [optional] [default to True]
**detail** | **str** | How much each listed study carries: &#x60;studies&#x60; only its ids, &#x60;analyses&#x60; also its selected analyses&#39; ids, names and matches, &#x60;features&#x60; also their features. With &#x60;paginate: false&#x60;, &#x60;studies&#x60; lists every selected study&#39;s id at once.  | [optional] [default to 'features']
**base_study_ids** | **List[str]** | Only the analyses of these papers. The counts, results and funnel cover the same restricted set, so an empty query lists every analysis with features that these papers have.  | [optional] 
**study_ids** | **List[str]** | Only the analyses of these studies (the pipeline studies the results name). With &#x60;base_study_ids&#x60;, an analysis must be in both.  | [optional] 
**funnel** | **bool** | Also return &#x60;searched&#x60; and &#x60;funnel&#x60;: what each criterion in turn keeps and drops, and how many analyses it finds silent. It counts once per criterion, so it costs most when criteria keep most analyses.  | [optional] [default to False]

## Example

```python
from neurostore_sdk.models.analysis_query_request import AnalysisQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryRequest from a JSON string
analysis_query_request_instance = AnalysisQueryRequest.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryRequest.to_json())

# convert the object into a dict
analysis_query_request_dict = analysis_query_request_instance.to_dict()
# create an instance of AnalysisQueryRequest from a dict
analysis_query_request_from_dict = AnalysisQueryRequest.from_dict(analysis_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


