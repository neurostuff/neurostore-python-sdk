# NoteCollectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **object** | The note will contain all note_keys as keys and have a value of either null or the value type specified in note_keys. | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]

## Example

```python
from neurostore_sdk.models.note_collection_request import NoteCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCollectionRequest from a JSON string
note_collection_request_instance = NoteCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(NoteCollectionRequest.to_json())

# convert the object into a dict
note_collection_request_dict = note_collection_request_instance.to_dict()
# create an instance of NoteCollectionRequest from a dict
note_collection_request_from_dict = NoteCollectionRequest.from_dict(note_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


