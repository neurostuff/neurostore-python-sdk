# ReviewAssigneeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ReviewAssignee]**](ReviewAssignee.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.review_assignee_list import ReviewAssigneeList

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewAssigneeList from a JSON string
review_assignee_list_instance = ReviewAssigneeList.from_json(json)
# print the JSON string representation of the object
print(ReviewAssigneeList.to_json())

# convert the object into a dict
review_assignee_list_dict = review_assignee_list_instance.to_dict()
# create an instance of ReviewAssigneeList from a dict
review_assignee_list_from_dict = ReviewAssigneeList.from_dict(review_assignee_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


