# AnalysisQueryResultSearched

With `funnel`, how many analyses and papers have features.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyses** | **int** |  | [optional] 
**base_studies** | **int** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_result_searched import AnalysisQueryResultSearched

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryResultSearched from a JSON string
analysis_query_result_searched_instance = AnalysisQueryResultSearched.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryResultSearched.to_json())

# convert the object into a dict
analysis_query_result_searched_dict = analysis_query_result_searched_instance.to_dict()
# create an instance of AnalysisQueryResultSearched from a dict
analysis_query_result_searched_from_dict = AnalysisQueryResultSearched.from_dict(analysis_query_result_searched_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


