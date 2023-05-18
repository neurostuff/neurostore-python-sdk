# JsonLd

JSON-LD elements for data tracking

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** | URI of the resource | [optional] 
**type** | **str** | One of the NiMADS data types | [optional] 

## Example

```python
from neurostore_sdk.models.json_ld import JsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of JsonLd from a JSON string
json_ld_instance = JsonLd.from_json(json)
# print the JSON string representation of the object
print JsonLd.to_json()

# convert the object into a dict
json_ld_dict = json_ld_instance.to_dict()
# create an instance of JsonLd from a dict
json_ld_form_dict = json_ld.from_dict(json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


