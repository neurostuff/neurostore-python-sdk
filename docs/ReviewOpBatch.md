# ReviewOpBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_last_seq** | **int** | The review&#39;s last_seq the batch was made against. | 
**ops** | **List[object]** |  | 

## Example

```python
from neurostore_sdk.models.review_op_batch import ReviewOpBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewOpBatch from a JSON string
review_op_batch_instance = ReviewOpBatch.from_json(json)
# print the JSON string representation of the object
print(ReviewOpBatch.to_json())

# convert the object into a dict
review_op_batch_dict = review_op_batch_instance.to_dict()
# create an instance of ReviewOpBatch from a dict
review_op_batch_from_dict = ReviewOpBatch.from_dict(review_op_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


