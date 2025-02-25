# AnnotationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** | object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation. | [optional] 
**annotation_csv** | **str** | annotation object expressed as a CSV | 
**name** | **str** | Descriptive name for the annotation. | [optional] 
**description** | **str** | Long form description of the annotation. | [optional] 
**note_keys** | **object** | The keys (columns) in the annotation and the key&#39;s respective data type (such as an integer or string). | [optional] 
**notes** | [**AnnotationRequestRelationshipsNotes**](AnnotationRequestRelationshipsNotes.md) |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**studyset** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_request import AnnotationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationRequest from a JSON string
annotation_request_instance = AnnotationRequest.from_json(json)
# print the JSON string representation of the object
print(AnnotationRequest.to_json())

# convert the object into a dict
annotation_request_dict = annotation_request_instance.to_dict()
# create an instance of AnnotationRequest from a dict
annotation_request_from_dict = AnnotationRequest.from_dict(annotation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


