# NoteCollectionList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[NoteCollectionReturn]**](NoteCollectionReturn.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.note_collection_list import NoteCollectionList

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCollectionList from a JSON string
note_collection_list_instance = NoteCollectionList.from_json(json)
# print the JSON string representation of the object
print NoteCollectionList.to_json()

# convert the object into a dict
note_collection_list_dict = note_collection_list_instance.to_dict()
# create an instance of NoteCollectionList from a dict
note_collection_list_form_dict = note_collection_list.from_dict(note_collection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


