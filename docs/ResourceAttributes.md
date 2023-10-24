# ResourceAttributes

common attributes for user owned resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 

## Example

```python
from neurostore_sdk.models.resource_attributes import ResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAttributes from a JSON string
resource_attributes_instance = ResourceAttributes.from_json(json)
# print the JSON string representation of the object
print ResourceAttributes.to_json()

# convert the object into a dict
resource_attributes_dict = resource_attributes_instance.to_dict()
# create an instance of ResourceAttributes from a dict
resource_attributes_form_dict = resource_attributes.from_dict(resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


