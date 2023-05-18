# AnnotationReturnRelationshipsNotesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **object** | The note will contain all note_keys as keys and have a value of either null or the value type specified in note_keys. | [optional] 
**analysis** | **str** |  | [optional] [readonly] 
**analysis_name** | **str** |  | [optional] [readonly] 
**study** | **str** |  | [optional] [readonly] 
**study_name** | **str** |  | [optional] [readonly] 
**annotation** | **str** |  | [optional] [readonly] 
**study_year** | **int** |  | [optional] [readonly] 
**publication** | **str** |  | [optional] [readonly] 
**authors** | **str** |  | [optional] [readonly] 

## Example

```python
from neurostore_sdk.models.annotation_return_relationships_notes_inner import AnnotationReturnRelationshipsNotesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationReturnRelationshipsNotesInner from a JSON string
annotation_return_relationships_notes_inner_instance = AnnotationReturnRelationshipsNotesInner.from_json(json)
# print the JSON string representation of the object
print AnnotationReturnRelationshipsNotesInner.to_json()

# convert the object into a dict
annotation_return_relationships_notes_inner_dict = annotation_return_relationships_notes_inner_instance.to_dict()
# create an instance of AnnotationReturnRelationshipsNotesInner from a dict
annotation_return_relationships_notes_inner_form_dict = annotation_return_relationships_notes_inner.from_dict(annotation_return_relationships_notes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


