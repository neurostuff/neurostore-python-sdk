# AnnotationBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name for the annotation. | [optional] 
**description** | **str** | Long form description of the annotation. | [optional] 
**metadata** | **object** | object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation. | [optional] 
**note_keys** | **object** | The keys (columns) in the annotation and the key&#39;s respective data type (such as an integer or string). | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_base import AnnotationBase

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationBase from a JSON string
annotation_base_instance = AnnotationBase.from_json(json)
# print the JSON string representation of the object
print(AnnotationBase.to_json())

# convert the object into a dict
annotation_base_dict = annotation_base_instance.to_dict()
# create an instance of AnnotationBase from a dict
annotation_base_from_dict = AnnotationBase.from_dict(annotation_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


