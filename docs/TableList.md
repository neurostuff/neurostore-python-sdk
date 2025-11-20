# TableList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TableReturn]**](TableReturn.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.table_list import TableList

# TODO update the JSON string below
json = "{}"
# create an instance of TableList from a JSON string
table_list_instance = TableList.from_json(json)
# print the JSON string representation of the object
print(TableList.to_json())

# convert the object into a dict
table_list_dict = table_list_instance.to_dict()
# create an instance of TableList from a dict
table_list_from_dict = TableList.from_dict(table_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


