# ReviewProgress

One reviewer's review of a paper, as the paper list shows it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**state** | [**ReviewState**](ReviewState.md) |  | [optional] 
**last_seq** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**edited** | **int** | Targets the reviewer edited, added or removed. | [optional] 
**verified** | **int** | Targets the reviewer checked and left unchanged. | [optional] 

## Example

```python
from neurostore_sdk.models.review_progress import ReviewProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewProgress from a JSON string
review_progress_instance = ReviewProgress.from_json(json)
# print the JSON string representation of the object
print(ReviewProgress.to_json())

# convert the object into a dict
review_progress_dict = review_progress_instance.to_dict()
# create an instance of ReviewProgress from a dict
review_progress_from_dict = ReviewProgress.from_dict(review_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


