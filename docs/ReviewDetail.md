# ReviewDetail


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
**record** | **object** | The extraction record with the review&#39;s ops applied. | [optional] 
**coordinate_revision** | **object** |  | [optional] 
**provenance** | **object** |  | [optional] 
**annotations** | **object** |  | [optional] 
**ops** | [**List[ReviewStoredOp]**](ReviewStoredOp.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.review_detail import ReviewDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewDetail from a JSON string
review_detail_instance = ReviewDetail.from_json(json)
# print the JSON string representation of the object
print(ReviewDetail.to_json())

# convert the object into a dict
review_detail_dict = review_detail_instance.to_dict()
# create an instance of ReviewDetail from a dict
review_detail_from_dict = ReviewDetail.from_dict(review_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


