# TableCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**footer** | **str** |  | [optional] 
**caption** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.table_common import TableCommon

# TODO update the JSON string below
json = "{}"
# create an instance of TableCommon from a JSON string
table_common_instance = TableCommon.from_json(json)
# print the JSON string representation of the object
print(TableCommon.to_json())

# convert the object into a dict
table_common_dict = table_common_instance.to_dict()
# create an instance of TableCommon from a dict
table_common_from_dict = TableCommon.from_dict(table_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


