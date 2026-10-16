# ReviewSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ReviewSourceListMetadata**](ReviewSourceListMetadata.md) |  | 
**results** | [**List[ReviewSource]**](ReviewSource.md) |  | 

## Example

```python
from neurostore_sdk.models.review_source_list import ReviewSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewSourceList from a JSON string
review_source_list_instance = ReviewSourceList.from_json(json)
# print the JSON string representation of the object
print(ReviewSourceList.to_json())

# convert the object into a dict
review_source_list_dict = review_source_list_instance.to_dict()
# create an instance of ReviewSourceList from a dict
review_source_list_from_dict = ReviewSourceList.from_dict(review_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


