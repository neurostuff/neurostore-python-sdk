# ReviewStatePatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**ReviewState**](ReviewState.md) |  | 
**reason** | [**ReviewSetAsideReason**](ReviewSetAsideReason.md) |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.review_state_patch import ReviewStatePatch

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewStatePatch from a JSON string
review_state_patch_instance = ReviewStatePatch.from_json(json)
# print the JSON string representation of the object
print(ReviewStatePatch.to_json())

# convert the object into a dict
review_state_patch_dict = review_state_patch_instance.to_dict()
# create an instance of ReviewStatePatch from a dict
review_state_patch_from_dict = ReviewStatePatch.from_dict(review_state_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


