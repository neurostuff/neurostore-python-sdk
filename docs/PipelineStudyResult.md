# PipelineStudyResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**pipeline_config_id** | **str** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_study_result import PipelineStudyResult

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineStudyResult from a JSON string
pipeline_study_result_instance = PipelineStudyResult.from_json(json)
# print the JSON string representation of the object
print(PipelineStudyResult.to_json())

# convert the object into a dict
pipeline_study_result_dict = pipeline_study_result_instance.to_dict()
# create an instance of PipelineStudyResult from a dict
pipeline_study_result_from_dict = PipelineStudyResult.from_dict(pipeline_study_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


