# QueryDatasetColumnsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.query_dataset_columns_inner import QueryDatasetColumnsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDatasetColumnsInner from a JSON string
query_dataset_columns_inner_instance = QueryDatasetColumnsInner.from_json(json)
# print the JSON string representation of the object
print(QueryDatasetColumnsInner.to_json())

# convert the object into a dict
query_dataset_columns_inner_dict = query_dataset_columns_inner_instance.to_dict()
# create an instance of QueryDatasetColumnsInner from a dict
query_dataset_columns_inner_from_dict = QueryDatasetColumnsInner.from_dict(query_dataset_columns_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


