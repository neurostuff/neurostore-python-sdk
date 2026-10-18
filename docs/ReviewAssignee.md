# ReviewAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from neurostore_sdk.models.review_assignee import ReviewAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewAssignee from a JSON string
review_assignee_instance = ReviewAssignee.from_json(json)
# print the JSON string representation of the object
print(ReviewAssignee.to_json())

# convert the object into a dict
review_assignee_dict = review_assignee_instance.to_dict()
# create an instance of ReviewAssignee from a dict
review_assignee_from_dict = ReviewAssignee.from_dict(review_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


