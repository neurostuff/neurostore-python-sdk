# AnnotationReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** | object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation. | [optional] 
**annotation_csv** | **str** | annotation object expressed as a CSV | 
**name** | **str** | Descriptive name for the annotation. | [optional] 
**description** | **str** | Long form description of the annotation. | [optional] 
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
from neurostore_sdk.models.annotation_return import AnnotationReturn

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationReturn from a JSON string
annotation_return_instance = AnnotationReturn.from_json(json)
# print the JSON string representation of the object
print AnnotationReturn.to_json()

# convert the object into a dict
annotation_return_dict = annotation_return_instance.to_dict()
# create an instance of AnnotationReturn from a dict
annotation_return_form_dict = annotation_return.from_dict(annotation_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


