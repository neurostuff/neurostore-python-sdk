# AnnotationReturnRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**AnnotationReturnRelationshipsNotes**](AnnotationReturnRelationshipsNotes.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_return_relationships import AnnotationReturnRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationReturnRelationships from a JSON string
annotation_return_relationships_instance = AnnotationReturnRelationships.from_json(json)
# print the JSON string representation of the object
print(AnnotationReturnRelationships.to_json())

# convert the object into a dict
annotation_return_relationships_dict = annotation_return_relationships_instance.to_dict()
# create an instance of AnnotationReturnRelationships from a dict
annotation_return_relationships_form_dict = annotation_return_relationships.from_dict(annotation_return_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


