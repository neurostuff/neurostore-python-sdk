# AnnotationReturnOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] [readonly] 
**annotation_csv** | **str** | annotation object expressed as a CSV | 

## Example

```python
from neurostore_sdk.models.annotation_return_one_of import AnnotationReturnOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationReturnOneOf from a JSON string
annotation_return_one_of_instance = AnnotationReturnOneOf.from_json(json)
# print the JSON string representation of the object
print(AnnotationReturnOneOf.to_json())

# convert the object into a dict
annotation_return_one_of_dict = annotation_return_one_of_instance.to_dict()
# create an instance of AnnotationReturnOneOf from a dict
annotation_return_one_of_from_dict = AnnotationReturnOneOf.from_dict(annotation_return_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


