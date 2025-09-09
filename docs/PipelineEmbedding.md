# PipelineEmbedding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**config_id** | **str** |  | 
**base_study_id** | **str** |  | [optional] 
**date_executed** | **datetime** |  | [optional] 
**file_inputs** | **object** |  | [optional] 
**status** | **str** | Current status of the pipeline execution (e.g. SUCCESS, FAILURE, ERROR, UNKNOWN) | 
**embedding** | **List[float]** |  | 

## Example

```python
from neurostore_sdk.models.pipeline_embedding import PipelineEmbedding

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineEmbedding from a JSON string
pipeline_embedding_instance = PipelineEmbedding.from_json(json)
# print the JSON string representation of the object
print(PipelineEmbedding.to_json())

# convert the object into a dict
pipeline_embedding_dict = pipeline_embedding_instance.to_dict()
# create an instance of PipelineEmbedding from a dict
pipeline_embedding_from_dict = PipelineEmbedding.from_dict(pipeline_embedding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


