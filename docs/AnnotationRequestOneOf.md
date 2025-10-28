# AnnotationRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name for the annotation. | [optional] 
**description** | **str** | Long form description of the annotation. | [optional] 
**metadata** | **object** | object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation. | [optional] 
**note_keys** | **object** | The keys (columns) in the annotation and the key&#39;s respective data type (such as an integer or string). | [optional] 
**pipelines** | [**List[AnnotationPipelineExtensionPipelinesInner]**](AnnotationPipelineExtensionPipelinesInner.md) | Optional pipeline descriptors used to populate annotation notes with feature columns. Each entry should include the pipeline name and the list of columns to import, along with optional version and config id.  | [optional] 
**notes** | [**AnnotationRequestRelationshipsNotes**](AnnotationRequestRelationshipsNotes.md) |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**studyset** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_request_one_of import AnnotationRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationRequestOneOf from a JSON string
annotation_request_one_of_instance = AnnotationRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(AnnotationRequestOneOf.to_json())

# convert the object into a dict
annotation_request_one_of_dict = annotation_request_one_of_instance.to_dict()
# create an instance of AnnotationRequestOneOf from a dict
annotation_request_one_of_from_dict = AnnotationRequestOneOf.from_dict(annotation_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


