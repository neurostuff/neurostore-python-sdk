# AnalysisQueryResultResultsInnerAnalysesInnerFeatures

Only when `detail` is `features`. The analysis's display and the `analysis_features` columns its criteria read, named as stored (`is_meta_analysis`, `species`, `task_ids`, `task_family_ids`, `arm_kinds`, `contrast_positive_timepoints`), with the extraction they were read from. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | The pipeline config of the record the features were read from. | [optional] 
**updated_at** | **datetime** | When the features were last written. Every re-ingest of the paper rewrites them, changed or not.  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_result_results_inner_analyses_inner_features import AnalysisQueryResultResultsInnerAnalysesInnerFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryResultResultsInnerAnalysesInnerFeatures from a JSON string
analysis_query_result_results_inner_analyses_inner_features_instance = AnalysisQueryResultResultsInnerAnalysesInnerFeatures.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryResultResultsInnerAnalysesInnerFeatures.to_json())

# convert the object into a dict
analysis_query_result_results_inner_analyses_inner_features_dict = analysis_query_result_results_inner_analyses_inner_features_instance.to_dict()
# create an instance of AnalysisQueryResultResultsInnerAnalysesInnerFeatures from a dict
analysis_query_result_results_inner_analyses_inner_features_from_dict = AnalysisQueryResultResultsInnerAnalysesInnerFeatures.from_dict(analysis_query_result_results_inner_analyses_inner_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


