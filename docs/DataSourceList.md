# DataSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DataSourceReturn]**](DataSourceReturn.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.data_source_list import DataSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceList from a JSON string
data_source_list_instance = DataSourceList.from_json(json)
# print the JSON string representation of the object
print(DataSourceList.to_json())

# convert the object into a dict
data_source_list_dict = data_source_list_instance.to_dict()
# create an instance of DataSourceList from a dict
data_source_list_from_dict = DataSourceList.from_dict(data_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


