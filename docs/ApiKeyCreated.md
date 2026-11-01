# ApiKeyCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**prefix** | **str** | the first characters of the key, to tell keys apart | [optional] 
**scopes** | **List[str]** | &#x60;read&#x60; allows GET requests; &#x60;write&#x60; allows every method. | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_used_at** | **datetime** |  | [optional] 
**revoked_at** | **datetime** |  | [optional] 
**key** | **str** | the full key; it cannot be retrieved again | [optional] 

## Example

```python
from neurostore_sdk.models.api_key_created import ApiKeyCreated

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyCreated from a JSON string
api_key_created_instance = ApiKeyCreated.from_json(json)
# print the JSON string representation of the object
print(ApiKeyCreated.to_json())

# convert the object into a dict
api_key_created_dict = api_key_created_instance.to_dict()
# create an instance of ApiKeyCreated from a dict
api_key_created_from_dict = ApiKeyCreated.from_dict(api_key_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


