# ReviewStoredOp

An applied op as the review stores it: StoredOp of store/backend/neurostore/review/schema/review-bundle.schema.json. In an op result each one also carries `inverse`, the ops that undo it without their client_op_ids, unless it is a note; the bundle's stored ops do not. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverse** | **List[object]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.review_stored_op import ReviewStoredOp

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewStoredOp from a JSON string
review_stored_op_instance = ReviewStoredOp.from_json(json)
# print the JSON string representation of the object
print(ReviewStoredOp.to_json())

# convert the object into a dict
review_stored_op_dict = review_stored_op_instance.to_dict()
# create an instance of ReviewStoredOp from a dict
review_stored_op_from_dict = ReviewStoredOp.from_dict(review_stored_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


