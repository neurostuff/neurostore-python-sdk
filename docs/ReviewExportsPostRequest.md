# ReviewExportsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ids** | **List[str]** |  | [optional] 
**base_study_ids** | **List[str]** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 
**states** | **List[str]** |  | [optional] 
**include_unreviewed** | **bool** |  | [optional] [default to False]

## Example

```python
from neurostore_sdk.models.review_exports_post_request import ReviewExportsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewExportsPostRequest from a JSON string
review_exports_post_request_instance = ReviewExportsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ReviewExportsPostRequest.to_json())

# convert the object into a dict
review_exports_post_request_dict = review_exports_post_request_instance.to_dict()
# create an instance of ReviewExportsPostRequest from a dict
review_exports_post_request_from_dict = ReviewExportsPostRequest.from_dict(review_exports_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


