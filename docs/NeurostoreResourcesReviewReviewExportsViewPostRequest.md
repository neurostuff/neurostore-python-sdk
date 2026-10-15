# NeurostoreResourcesReviewReviewExportsViewPostRequest


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
from neurostore_sdk.models.neurostore_resources_review_review_exports_view_post_request import NeurostoreResourcesReviewReviewExportsViewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NeurostoreResourcesReviewReviewExportsViewPostRequest from a JSON string
neurostore_resources_review_review_exports_view_post_request_instance = NeurostoreResourcesReviewReviewExportsViewPostRequest.from_json(json)
# print the JSON string representation of the object
print(NeurostoreResourcesReviewReviewExportsViewPostRequest.to_json())

# convert the object into a dict
neurostore_resources_review_review_exports_view_post_request_dict = neurostore_resources_review_review_exports_view_post_request_instance.to_dict()
# create an instance of NeurostoreResourcesReviewReviewExportsViewPostRequest from a dict
neurostore_resources_review_review_exports_view_post_request_from_dict = NeurostoreResourcesReviewReviewExportsViewPostRequest.from_dict(neurostore_resources_review_review_exports_view_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


