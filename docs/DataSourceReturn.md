# DataSourceReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The data source&#39;s key, e.g. &#x60;ukb&#x60;, given when it is created and never changed, so records made outside neurostore can name it before it is uploaded. | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**kinds** | **List[str]** |  | [optional] 
**modalities** | **List[str]** |  | [optional] 
**part_of** | **str** | The data source (repository or consortium) this one is hosted by or part of. | [optional] 
**url** | **str** |  | [optional] 
**url_kind** | **str** | Where the url came from or what it points to, e.g. &#x60;rrid&#x60;, &#x60;re3data&#x60;, &#x60;jpnd&#x60;, &#x60;checked:official&#x60;, &#x60;checked:registry&#x60;, &#x60;checked:publication&#x60;. | [optional] 
**rrids** | **List[str]** |  | [optional] 
**re3data_ids** | **List[str]** |  | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**user** | **str** | The owner&#39;s Auth0 id, served only to the owner; null for anyone else, who sees &#x60;username&#x60;. | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 

## Example

```python
from neurostore_sdk.models.data_source_return import DataSourceReturn

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceReturn from a JSON string
data_source_return_instance = DataSourceReturn.from_json(json)
# print the JSON string representation of the object
print(DataSourceReturn.to_json())

# convert the object into a dict
data_source_return_dict = data_source_return_instance.to_dict()
# create an instance of DataSourceReturn from a dict
data_source_return_from_dict = DataSourceReturn.from_dict(data_source_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


