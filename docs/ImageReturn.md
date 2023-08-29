# ImageReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** | Metadata about image such as software and version used and other relevant data about how the image was produced. | [optional] 
**url** | **str** | URL to image file. | [optional] 
**filename** | **str** | Name of the image file. | [optional] 
**space** | **str** | The template space the image is in (e.g., MNI  | [optional] 
**value_type** | **str** | The values the image represents. For example, T-statistic or Z-statistic, or Betas. | [optional] 
**add_date** | **datetime** | Date the image was added. | [optional] [readonly] 
**analysis** | **str** |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**analysis_name** | **str** |  | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when was the resource last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 

## Example

```python
from neurostore_sdk.models.image_return import ImageReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ImageReturn from a JSON string
image_return_instance = ImageReturn.from_json(json)
# print the JSON string representation of the object
print ImageReturn.to_json()

# convert the object into a dict
image_return_dict = image_return_instance.to_dict()
# create an instance of ImageReturn from a dict
image_return_form_dict = image_return.from_dict(image_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


