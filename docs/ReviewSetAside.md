# ReviewSetAside

Present only while the review is set aside.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**ReviewSetAsideReason**](ReviewSetAsideReason.md) |  | 
**note** | **str** |  | 

## Example

```python
from neurostore_sdk.models.review_set_aside import ReviewSetAside

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewSetAside from a JSON string
review_set_aside_instance = ReviewSetAside.from_json(json)
# print the JSON string representation of the object
print(ReviewSetAside.to_json())

# convert the object into a dict
review_set_aside_dict = review_set_aside_instance.to_dict()
# create an instance of ReviewSetAside from a dict
review_set_aside_from_dict = ReviewSetAside.from_dict(review_set_aside_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


