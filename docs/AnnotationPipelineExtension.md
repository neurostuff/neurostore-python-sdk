# AnnotationPipelineExtension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipelines** | [**List[AnnotationPipelineExtensionPipelinesInner]**](AnnotationPipelineExtensionPipelinesInner.md) | Optional pipeline descriptors used to populate annotation notes with feature columns. Each entry should include the pipeline name and the list of columns to import, along with optional version and config id.  | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_pipeline_extension import AnnotationPipelineExtension

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationPipelineExtension from a JSON string
annotation_pipeline_extension_instance = AnnotationPipelineExtension.from_json(json)
# print the JSON string representation of the object
print(AnnotationPipelineExtension.to_json())

# convert the object into a dict
annotation_pipeline_extension_dict = annotation_pipeline_extension_instance.to_dict()
# create an instance of AnnotationPipelineExtension from a dict
annotation_pipeline_extension_from_dict = AnnotationPipelineExtension.from_dict(annotation_pipeline_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


