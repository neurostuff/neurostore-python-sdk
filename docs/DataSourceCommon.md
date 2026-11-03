# DataSourceCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | A short stable key, e.g. &#x60;ukb&#x60;. | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**kinds** | **List[str]** |  | [optional] 
**modalities** | **List[str]** |  | [optional] 
**part_of** | **str** | The data source (repository or consortium) this one is hosted by or part of. | [optional] 
**url** | **str** |  | [optional] 
**url_kind** | **str** | Where the url came from or what it points to, e.g. &#x60;rrid&#x60;, &#x60;re3data&#x60;, &#x60;jpnd&#x60;, &#x60;checked:official&#x60;, &#x60;checked:registry&#x60;, &#x60;checked:publication&#x60;. | [optional] 
**rrids** | **List[str]** |  | [optional] 
**re3data_ids** | **List[str]** |  | [optional] 
**listed_in** | **List[str]** | The catalogues the data source was found in. | [optional] 
**aliases** | [**List[DataSourceAlias]**](DataSourceAlias.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.data_source_common import DataSourceCommon

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceCommon from a JSON string
data_source_common_instance = DataSourceCommon.from_json(json)
# print the JSON string representation of the object
print(DataSourceCommon.to_json())

# convert the object into a dict
data_source_common_dict = data_source_common_instance.to_dict()
# create an instance of DataSourceCommon from a dict
data_source_common_from_dict = DataSourceCommon.from_dict(data_source_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


