# JsonLdContext

Context for the shorthand names

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vocab** | **str** | common URI prefix for @type | [optional] 

## Example

```python
from neurostore_sdk.models.json_ld_context import JsonLdContext

# TODO update the JSON string below
json = "{}"
# create an instance of JsonLdContext from a JSON string
json_ld_context_instance = JsonLdContext.from_json(json)
# print the JSON string representation of the object
print(JsonLdContext.to_json())

# convert the object into a dict
json_ld_context_dict = json_ld_context_instance.to_dict()
# create an instance of JsonLdContext from a dict
json_ld_context_form_dict = json_ld_context.from_dict(json_ld_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


