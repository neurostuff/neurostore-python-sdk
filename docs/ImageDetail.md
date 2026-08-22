# ImageDetail

Read-only image fields that are withheld unless a request asks for them by name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_summary** | [**ImageValueSummary**](ImageValueSummary.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.image_detail import ImageDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ImageDetail from a JSON string
image_detail_instance = ImageDetail.from_json(json)
# print the JSON string representation of the object
print(ImageDetail.to_json())

# convert the object into a dict
image_detail_dict = image_detail_instance.to_dict()
# create an instance of ImageDetail from a dict
image_detail_from_dict = ImageDetail.from_dict(image_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


