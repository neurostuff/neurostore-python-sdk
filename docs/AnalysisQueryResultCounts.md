# AnalysisQueryResultCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyses** | **int** |  | [optional] 
**studies** | **int** |  | [optional] 
**base_studies** | **int** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_result_counts import AnalysisQueryResultCounts

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryResultCounts from a JSON string
analysis_query_result_counts_instance = AnalysisQueryResultCounts.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryResultCounts.to_json())

# convert the object into a dict
analysis_query_result_counts_dict = analysis_query_result_counts_instance.to_dict()
# create an instance of AnalysisQueryResultCounts from a dict
analysis_query_result_counts_from_dict = AnalysisQueryResultCounts.from_dict(analysis_query_result_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


