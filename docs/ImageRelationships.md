# ImageRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | **str** |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**analysis_name** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.image_relationships import ImageRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ImageRelationships from a JSON string
image_relationships_instance = ImageRelationships.from_json(json)
# print the JSON string representation of the object
print(ImageRelationships.to_json())

# convert the object into a dict
image_relationships_dict = image_relationships_instance.to_dict()
# create an instance of ImageRelationships from a dict
image_relationships_form_dict = image_relationships.from_dict(image_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


