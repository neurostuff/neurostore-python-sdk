# PipelineEmbeddingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PipelineEmbedding]**](PipelineEmbedding.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_embedding_list import PipelineEmbeddingList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineEmbeddingList from a JSON string
pipeline_embedding_list_instance = PipelineEmbeddingList.from_json(json)
# print the JSON string representation of the object
print(PipelineEmbeddingList.to_json())

# convert the object into a dict
pipeline_embedding_list_dict = pipeline_embedding_list_instance.to_dict()
# create an instance of PipelineEmbeddingList from a dict
pipeline_embedding_list_from_dict = PipelineEmbeddingList.from_dict(pipeline_embedding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


