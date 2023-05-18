# AnnotationRequestRelationshipsNotesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **object** | The note will contain all note_keys as keys and have a value of either null or the value type specified in note_keys. | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]

## Example

```python
from neurostore_sdk.models.annotation_request_relationships_notes_inner import AnnotationRequestRelationshipsNotesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationRequestRelationshipsNotesInner from a JSON string
annotation_request_relationships_notes_inner_instance = AnnotationRequestRelationshipsNotesInner.from_json(json)
# print the JSON string representation of the object
print AnnotationRequestRelationshipsNotesInner.to_json()

# convert the object into a dict
annotation_request_relationships_notes_inner_dict = annotation_request_relationships_notes_inner_instance.to_dict()
# create an instance of AnnotationRequestRelationshipsNotesInner from a dict
annotation_request_relationships_notes_inner_form_dict = annotation_request_relationships_notes_inner.from_dict(annotation_request_relationships_notes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


