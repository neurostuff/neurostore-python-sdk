# AnnotationPipelineExtensionPipelinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pipeline extractor name. | 
**version** | **str** | Optional pipeline version to use; latest is selected when omitted. | [optional] 
**config_id** | **str** | Optional specific pipeline config identifier to use. | [optional] 
**columns** | **List[str]** | Feature columns to add to each annotation note. | 

## Example

```python
from neurostore_sdk.models.annotation_pipeline_extension_pipelines_inner import AnnotationPipelineExtensionPipelinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationPipelineExtensionPipelinesInner from a JSON string
annotation_pipeline_extension_pipelines_inner_instance = AnnotationPipelineExtensionPipelinesInner.from_json(json)
# print the JSON string representation of the object
print(AnnotationPipelineExtensionPipelinesInner.to_json())

# convert the object into a dict
annotation_pipeline_extension_pipelines_inner_dict = annotation_pipeline_extension_pipelines_inner_instance.to_dict()
# create an instance of AnnotationPipelineExtensionPipelinesInner from a dict
annotation_pipeline_extension_pipelines_inner_from_dict = AnnotationPipelineExtensionPipelinesInner.from_dict(annotation_pipeline_extension_pipelines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


