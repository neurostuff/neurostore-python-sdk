# NoteCollectionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **object** | The note will contain all note_keys as keys and have a value of either null or the value type specified in note_keys. | [optional] 

## Example

```python
from neurostore_sdk.models.note_collection_base import NoteCollectionBase

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCollectionBase from a JSON string
note_collection_base_instance = NoteCollectionBase.from_json(json)
# print the JSON string representation of the object
print(NoteCollectionBase.to_json())

# convert the object into a dict
note_collection_base_dict = note_collection_base_instance.to_dict()
# create an instance of NoteCollectionBase from a dict
note_collection_base_from_dict = NoteCollectionBase.from_dict(note_collection_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


