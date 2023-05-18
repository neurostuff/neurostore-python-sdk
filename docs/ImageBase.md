# ImageBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** | Metadata about image such as software and version used and other relevant data about how the image was produced. | [optional] 
**url** | **str** | URL to image file. | [optional] 
**filename** | **str** | Name of the image file. | [optional] 
**space** | **str** | The template space the image is in (e.g., MNI  | [optional] 
**value_type** | **str** | The values the image represents. For example, T-statistic or Z-statistic, or Betas. | [optional] 
**add_date** | **datetime** | Date the image was added. | [optional] [readonly] 

## Example

```python
from neurostore_sdk.models.image_base import ImageBase

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBase from a JSON string
image_base_instance = ImageBase.from_json(json)
# print the JSON string representation of the object
print ImageBase.to_json()

# convert the object into a dict
image_base_dict = image_base_instance.to_dict()
# create an instance of ImageBase from a dict
image_base_form_dict = image_base.from_dict(image_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


