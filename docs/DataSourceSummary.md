# DataSourceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.data_source_summary import DataSourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceSummary from a JSON string
data_source_summary_instance = DataSourceSummary.from_json(json)
# print the JSON string representation of the object
print(DataSourceSummary.to_json())

# convert the object into a dict
data_source_summary_dict = data_source_summary_instance.to_dict()
# create an instance of DataSourceSummary from a dict
data_source_summary_from_dict = DataSourceSummary.from_dict(data_source_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


