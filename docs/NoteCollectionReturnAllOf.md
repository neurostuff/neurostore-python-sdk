# NoteCollectionReturnAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from neurostore_sdk.models.note_collection_return_all_of import NoteCollectionReturnAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCollectionReturnAllOf from a JSON string
note_collection_return_all_of_instance = NoteCollectionReturnAllOf.from_json(json)
# print the JSON string representation of the object
print NoteCollectionReturnAllOf.to_json()

# convert the object into a dict
note_collection_return_all_of_dict = note_collection_return_all_of_instance.to_dict()
# create an instance of NoteCollectionReturnAllOf from a dict
note_collection_return_all_of_form_dict = note_collection_return_all_of.from_dict(note_collection_return_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


