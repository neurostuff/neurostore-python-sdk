# ReviewOpResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ops** | [**List[ReviewStoredOp]**](ReviewStoredOp.md) |  | [optional] 
**last_seq** | **int** |  | [optional] 
**record** | **object** |  | [optional] 
**coordinate_revision** | **object** |  | [optional] 
**provenance** | **object** |  | [optional] 
**annotations** | **object** |  | [optional] 
**hidden** | **object** | The hidden set of the new record, as in the bundle. | [optional] 
**entities** | **List[object]** | The entity index of the new record, as in the bundle. | [optional] 

## Example

```python
from neurostore_sdk.models.review_op_result import ReviewOpResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewOpResult from a JSON string
review_op_result_instance = ReviewOpResult.from_json(json)
# print the JSON string representation of the object
print(ReviewOpResult.to_json())

# convert the object into a dict
review_op_result_dict = review_op_result_instance.to_dict()
# create an instance of ReviewOpResult from a dict
review_op_result_from_dict = ReviewOpResult.from_dict(review_op_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


