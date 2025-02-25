# AnnotationCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**studyset** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_common import AnnotationCommon

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationCommon from a JSON string
annotation_common_instance = AnnotationCommon.from_json(json)
# print the JSON string representation of the object
print(AnnotationCommon.to_json())

# convert the object into a dict
annotation_common_dict = annotation_common_instance.to_dict()
# create an instance of AnnotationCommon from a dict
annotation_common_from_dict = AnnotationCommon.from_dict(annotation_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


