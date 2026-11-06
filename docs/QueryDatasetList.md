# QueryDatasetList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refreshed_at** | **datetime** | When the datasets were last refreshed. | [optional] 
**results** | [**List[QueryDataset]**](QueryDataset.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.query_dataset_list import QueryDatasetList

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDatasetList from a JSON string
query_dataset_list_instance = QueryDatasetList.from_json(json)
# print the JSON string representation of the object
print(QueryDatasetList.to_json())

# convert the object into a dict
query_dataset_list_dict = query_dataset_list_instance.to_dict()
# create an instance of QueryDatasetList from a dict
query_dataset_list_from_dict = QueryDatasetList.from_dict(query_dataset_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


