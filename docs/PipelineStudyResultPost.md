# PipelineStudyResultPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study_ids** | **List[str]** |  | 
**id** | **str** |  | 
**pipeline_config_id** | **str** |  | [optional] 
**base_study_id** | **str** |  | [optional] 
**config_id** | **str** |  | [optional] 
**date_executed** | **datetime** |  | [optional] 
**file_inputs** | **object** |  | [optional] 
**result_data** | **object** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_study_result_post import PipelineStudyResultPost

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineStudyResultPost from a JSON string
pipeline_study_result_post_instance = PipelineStudyResultPost.from_json(json)
# print the JSON string representation of the object
print(PipelineStudyResultPost.to_json())

# convert the object into a dict
pipeline_study_result_post_dict = pipeline_study_result_post_instance.to_dict()
# create an instance of PipelineStudyResultPost from a dict
pipeline_study_result_post_from_dict = PipelineStudyResultPost.from_dict(pipeline_study_result_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


