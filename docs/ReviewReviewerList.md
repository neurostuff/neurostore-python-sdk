# ReviewReviewerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ReviewAssignee]**](ReviewAssignee.md) |  | 

## Example

```python
from neurostore_sdk.models.review_reviewer_list import ReviewReviewerList

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewReviewerList from a JSON string
review_reviewer_list_instance = ReviewReviewerList.from_json(json)
# print the JSON string representation of the object
print(ReviewReviewerList.to_json())

# convert the object into a dict
review_reviewer_list_dict = review_reviewer_list_instance.to_dict()
# create an instance of ReviewReviewerList from a dict
review_reviewer_list_from_dict = ReviewReviewerList.from_dict(review_reviewer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


