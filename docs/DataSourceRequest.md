# DataSourceRequest


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
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]

## Example

```python
from neurostore_sdk.models.data_source_request import DataSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceRequest from a JSON string
data_source_request_instance = DataSourceRequest.from_json(json)
# print the JSON string representation of the object
print(DataSourceRequest.to_json())

# convert the object into a dict
data_source_request_dict = data_source_request_instance.to_dict()
# create an instance of DataSourceRequest from a dict
data_source_request_from_dict = DataSourceRequest.from_dict(data_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


