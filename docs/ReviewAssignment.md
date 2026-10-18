# ReviewAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_study_id** | **str** |  | 
**user_id** | **str** |  | 
**name** | **str** |  | 
**assigned_by_id** | **str** |  | 

## Example

```python
from neurostore_sdk.models.review_assignment import ReviewAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewAssignment from a JSON string
review_assignment_instance = ReviewAssignment.from_json(json)
# print the JSON string representation of the object
print(ReviewAssignment.to_json())

# convert the object into a dict
review_assignment_dict = review_assignment_instance.to_dict()
# create an instance of ReviewAssignment from a dict
review_assignment_from_dict = ReviewAssignment.from_dict(review_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


