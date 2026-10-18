# ReviewSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**source_id** | **str** |  | 
**user_id** | **str** |  | 
**state** | [**ReviewState**](ReviewState.md) |  | 
**set_aside** | [**ReviewSetAside**](ReviewSetAside.md) |  | [optional] 
**last_seq** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from neurostore_sdk.models.review_summary import ReviewSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewSummary from a JSON string
review_summary_instance = ReviewSummary.from_json(json)
# print the JSON string representation of the object
print(ReviewSummary.to_json())

# convert the object into a dict
review_summary_dict = review_summary_instance.to_dict()
# create an instance of ReviewSummary from a dict
review_summary_from_dict = ReviewSummary.from_dict(review_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


