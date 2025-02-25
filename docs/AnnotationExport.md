# AnnotationExport

exporting an annotation as a CSV for easier editing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] [readonly] 
**annotation_csv** | **str** | annotation object expressed as a CSV | 

## Example

```python
from neurostore_sdk.models.annotation_export import AnnotationExport

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationExport from a JSON string
annotation_export_instance = AnnotationExport.from_json(json)
# print the JSON string representation of the object
print(AnnotationExport.to_json())

# convert the object into a dict
annotation_export_dict = annotation_export_instance.to_dict()
# create an instance of AnnotationExport from a dict
annotation_export_from_dict = AnnotationExport.from_dict(annotation_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


