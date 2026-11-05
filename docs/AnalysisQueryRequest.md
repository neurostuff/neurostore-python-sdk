# AnalysisQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**AnalysisQuery**](AnalysisQuery.md) |  | 
**limit** | **int** | How many selected analyses to list; counts and study_ids cover them all. | [optional] [default to 100]
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


