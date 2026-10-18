# ReviewMe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**name** | **str** |  | 
**lead** | **bool** | Whether the caller is a lead reviewer (admin-reviewer and admin). | 

## Example

```python
from neurostore_sdk.models.review_me import ReviewMe

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewMe from a JSON string
review_me_instance = ReviewMe.from_json(json)
# print the JSON string representation of the object
print(ReviewMe.to_json())

# convert the object into a dict
review_me_dict = review_me_instance.to_dict()
# create an instance of ReviewMe from a dict
review_me_from_dict = ReviewMe.from_dict(review_me_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


