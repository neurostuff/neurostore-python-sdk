# ReadableResourceAttributes

common readable resource attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 

## Example

```python
from neurostore_sdk.models.readable_resource_attributes import ReadableResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ReadableResourceAttributes from a JSON string
readable_resource_attributes_instance = ReadableResourceAttributes.from_json(json)
# print the JSON string representation of the object
print ReadableResourceAttributes.to_json()

# convert the object into a dict
readable_resource_attributes_dict = readable_resource_attributes_instance.to_dict()
# create an instance of ReadableResourceAttributes from a dict
readable_resource_attributes_form_dict = readable_resource_attributes.from_dict(readable_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


