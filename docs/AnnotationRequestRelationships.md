# AnnotationRequestRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**AnnotationRequestRelationshipsNotes**](AnnotationRequestRelationshipsNotes.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_request_relationships import AnnotationRequestRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationRequestRelationships from a JSON string
annotation_request_relationships_instance = AnnotationRequestRelationships.from_json(json)
# print the JSON string representation of the object
print(AnnotationRequestRelationships.to_json())

# convert the object into a dict
annotation_request_relationships_dict = annotation_request_relationships_instance.to_dict()
# create an instance of AnnotationRequestRelationships from a dict
annotation_request_relationships_from_dict = AnnotationRequestRelationships.from_dict(annotation_request_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


