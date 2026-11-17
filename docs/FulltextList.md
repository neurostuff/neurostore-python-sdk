# FulltextList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FulltextSummary]**](FulltextSummary.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.fulltext_list import FulltextList

# TODO update the JSON string below
json = "{}"
# create an instance of FulltextList from a JSON string
fulltext_list_instance = FulltextList.from_json(json)
# print the JSON string representation of the object
print(FulltextList.to_json())

# convert the object into a dict
fulltext_list_dict = fulltext_list_instance.to_dict()
# create an instance of FulltextList from a dict
fulltext_list_from_dict = FulltextList.from_dict(fulltext_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


