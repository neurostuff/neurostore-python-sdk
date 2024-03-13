# NoteCollectionReturn


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
**id** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.note_collection_return import NoteCollectionReturn

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCollectionReturn from a JSON string
note_collection_return_instance = NoteCollectionReturn.from_json(json)
# print the JSON string representation of the object
print NoteCollectionReturn.to_json()

# convert the object into a dict
note_collection_return_dict = note_collection_return_instance.to_dict()
# create an instance of NoteCollectionReturn from a dict
note_collection_return_form_dict = note_collection_return.from_dict(note_collection_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


