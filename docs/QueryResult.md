# QueryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**query** | **Dict[str, str]** | The query as it was read, one key per &#x60;$&#x60; parameter given. | [optional] 
**columns** | [**List[QueryResultColumnsInner]**](QueryResultColumnsInner.md) |  | [optional] 
**rows** | **List[List[object]]** | One array per row, in the order of &#x60;columns&#x60;. | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**refreshed_at** | **datetime** |  | [optional] 

## Example

```python
from neurostore_sdk.models.query_result import QueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResult from a JSON string
query_result_instance = QueryResult.from_json(json)
# print the JSON string representation of the object
print(QueryResult.to_json())

# convert the object into a dict
query_result_dict = query_result_instance.to_dict()
# create an instance of QueryResult from a dict
query_result_from_dict = QueryResult.from_dict(query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


