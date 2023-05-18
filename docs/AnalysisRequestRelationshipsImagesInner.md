# AnalysisRequestRelationshipsImagesInner


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
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]

## Example

```python
from neurostore_sdk.models.analysis_request_relationships_images_inner import AnalysisRequestRelationshipsImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisRequestRelationshipsImagesInner from a JSON string
analysis_request_relationships_images_inner_instance = AnalysisRequestRelationshipsImagesInner.from_json(json)
# print the JSON string representation of the object
print AnalysisRequestRelationshipsImagesInner.to_json()

# convert the object into a dict
analysis_request_relationships_images_inner_dict = analysis_request_relationships_images_inner_instance.to_dict()
# create an instance of AnalysisRequestRelationshipsImagesInner from a dict
analysis_request_relationships_images_inner_form_dict = analysis_request_relationships_images_inner.from_dict(analysis_request_relationships_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


