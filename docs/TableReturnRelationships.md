# TableReturnRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study** | **str** |  | [optional] 
**analyses** | [**StudyReturnRelationshipsAnalyses**](StudyReturnRelationshipsAnalyses.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.table_return_relationships import TableReturnRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of TableReturnRelationships from a JSON string
table_return_relationships_instance = TableReturnRelationships.from_json(json)
# print the JSON string representation of the object
print(TableReturnRelationships.to_json())

# convert the object into a dict
table_return_relationships_dict = table_return_relationships_instance.to_dict()
# create an instance of TableReturnRelationships from a dict
table_return_relationships_from_dict = TableReturnRelationships.from_dict(table_return_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


