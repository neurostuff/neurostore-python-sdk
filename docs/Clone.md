# Clone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_updated_at** | **str** |  | [optional] [readonly] 

## Example

```python
from neurostore_sdk.models.clone import Clone

# TODO update the JSON string below
json = "{}"
# create an instance of Clone from a JSON string
clone_instance = Clone.from_json(json)
# print the JSON string representation of the object
print(Clone.to_json())

# convert the object into a dict
clone_dict = clone_instance.to_dict()
# create an instance of Clone from a dict
clone_from_dict = Clone.from_dict(clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


