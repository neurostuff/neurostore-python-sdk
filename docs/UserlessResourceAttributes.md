# UserlessResourceAttributes

common resource attributes not tied to a specific user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]

## Example

```python
from neurostore_sdk.models.userless_resource_attributes import UserlessResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserlessResourceAttributes from a JSON string
userless_resource_attributes_instance = UserlessResourceAttributes.from_json(json)
# print the JSON string representation of the object
print(UserlessResourceAttributes.to_json())

# convert the object into a dict
userless_resource_attributes_dict = userless_resource_attributes_instance.to_dict()
# create an instance of UserlessResourceAttributes from a dict
userless_resource_attributes_from_dict = UserlessResourceAttributes.from_dict(userless_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


