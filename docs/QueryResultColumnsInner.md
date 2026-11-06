# QueryResultColumnsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.query_result_columns_inner import QueryResultColumnsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultColumnsInner from a JSON string
query_result_columns_inner_instance = QueryResultColumnsInner.from_json(json)
# print the JSON string representation of the object
print(QueryResultColumnsInner.to_json())

# convert the object into a dict
query_result_columns_inner_dict = query_result_columns_inner_instance.to_dict()
# create an instance of QueryResultColumnsInner from a dict
query_result_columns_inner_from_dict = QueryResultColumnsInner.from_dict(query_result_columns_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


