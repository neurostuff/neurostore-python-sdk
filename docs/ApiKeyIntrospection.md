# ApiKeyIntrospection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | the owner&#39;s external id | [optional] 
**name** | **str** | the owner&#39;s display name | [optional] 
**scopes** | **List[str]** | &#x60;read&#x60; allows GET requests; &#x60;write&#x60; allows every method. | [optional] 

## Example

```python
from neurostore_sdk.models.api_key_introspection import ApiKeyIntrospection

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyIntrospection from a JSON string
api_key_introspection_instance = ApiKeyIntrospection.from_json(json)
# print the JSON string representation of the object
print(ApiKeyIntrospection.to_json())

# convert the object into a dict
api_key_introspection_dict = api_key_introspection_instance.to_dict()
# create an instance of ApiKeyIntrospection from a dict
api_key_introspection_from_dict = ApiKeyIntrospection.from_dict(api_key_introspection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


