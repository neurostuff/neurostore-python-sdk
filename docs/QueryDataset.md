# QueryDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**key** | **List[str]** | The columns that identify a row. | [optional] 
**columns** | [**List[QueryDatasetColumnsInner]**](QueryDatasetColumnsInner.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.query_dataset import QueryDataset

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDataset from a JSON string
query_dataset_instance = QueryDataset.from_json(json)
# print the JSON string representation of the object
print(QueryDataset.to_json())

# convert the object into a dict
query_dataset_dict = query_dataset_instance.to_dict()
# create an instance of QueryDataset from a dict
query_dataset_from_dict = QueryDataset.from_dict(query_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


