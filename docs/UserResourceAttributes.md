# UserResourceAttributes

common resource attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | who owns the resource | [optional] [readonly] 

## Example

```python
from neurostore_sdk.models.user_resource_attributes import UserResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserResourceAttributes from a JSON string
user_resource_attributes_instance = UserResourceAttributes.from_json(json)
# print the JSON string representation of the object
print UserResourceAttributes.to_json()

# convert the object into a dict
user_resource_attributes_dict = user_resource_attributes_instance.to_dict()
# create an instance of UserResourceAttributes from a dict
user_resource_attributes_form_dict = user_resource_attributes.from_dict(user_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


