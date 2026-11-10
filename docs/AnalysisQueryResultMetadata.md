# AnalysisQueryResultMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | How many studies the query selects, over every page. | [optional] 
**analysis_count** | **int** | How many analyses the query selects, over every page. | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_result_metadata import AnalysisQueryResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryResultMetadata from a JSON string
analysis_query_result_metadata_instance = AnalysisQueryResultMetadata.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryResultMetadata.to_json())

# convert the object into a dict
analysis_query_result_metadata_dict = analysis_query_result_metadata_instance.to_dict()
# create an instance of AnalysisQueryResultMetadata from a dict
analysis_query_result_metadata_from_dict = AnalysisQueryResultMetadata.from_dict(analysis_query_result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


