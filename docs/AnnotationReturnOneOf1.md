# AnnotationReturnOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name for the annotation. | [optional] 
**description** | **str** | Long form description of the annotation. | [optional] 
**metadata** | **object** | object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation. | [optional] 
**note_keys** | **object** | The keys (columns) in the annotation and the key&#39;s respective data type (such as an integer or string). | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 
**source** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_updated_at** | **str** |  | [optional] [readonly] 
**notes** | [**AnnotationReturnRelationshipsNotes**](AnnotationReturnRelationshipsNotes.md) |  | [optional] 
**studyset** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_return_one_of1 import AnnotationReturnOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationReturnOneOf1 from a JSON string
annotation_return_one_of1_instance = AnnotationReturnOneOf1.from_json(json)
# print the JSON string representation of the object
print(AnnotationReturnOneOf1.to_json())

# convert the object into a dict
annotation_return_one_of1_dict = annotation_return_one_of1_instance.to_dict()
# create an instance of AnnotationReturnOneOf1 from a dict
annotation_return_one_of1_from_dict = AnnotationReturnOneOf1.from_dict(annotation_return_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


