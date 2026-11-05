# JournalList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[JournalReturn]**](JournalReturn.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.journal_list import JournalList

# TODO update the JSON string below
json = "{}"
# create an instance of JournalList from a JSON string
journal_list_instance = JournalList.from_json(json)
# print the JSON string representation of the object
print(JournalList.to_json())

# convert the object into a dict
journal_list_dict = journal_list_instance.to_dict()
# create an instance of JournalList from a dict
journal_list_from_dict = JournalList.from_dict(journal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


