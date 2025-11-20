# TableReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 
**t_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**footer** | **str** |  | [optional] 
**caption** | **str** |  | [optional] 
**study** | **str** |  | [optional] 
**analyses** | [**StudyReturnRelationshipsAnalyses**](StudyReturnRelationshipsAnalyses.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.table_return import TableReturn

# TODO update the JSON string below
json = "{}"
# create an instance of TableReturn from a JSON string
table_return_instance = TableReturn.from_json(json)
# print the JSON string representation of the object
print(TableReturn.to_json())

# convert the object into a dict
table_return_dict = table_return_instance.to_dict()
# create an instance of TableReturn from a dict
table_return_from_dict = TableReturn.from_dict(table_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


