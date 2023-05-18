# WriteableResourceAttributes

common resource attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]

## Example

```python
from neurostore_sdk.models.writeable_resource_attributes import WriteableResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WriteableResourceAttributes from a JSON string
writeable_resource_attributes_instance = WriteableResourceAttributes.from_json(json)
# print the JSON string representation of the object
print WriteableResourceAttributes.to_json()

# convert the object into a dict
writeable_resource_attributes_dict = writeable_resource_attributes_instance.to_dict()
# create an instance of WriteableResourceAttributes from a dict
writeable_resource_attributes_form_dict = writeable_resource_attributes.from_dict(writeable_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


