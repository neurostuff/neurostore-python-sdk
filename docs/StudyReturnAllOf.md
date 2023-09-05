# StudyReturnAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**studysets** | [**List[StudyReturnAllOfStudysets]**](StudyReturnAllOfStudysets.md) |  | [optional] 
**has_coordinates** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_return_all_of import StudyReturnAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of StudyReturnAllOf from a JSON string
study_return_all_of_instance = StudyReturnAllOf.from_json(json)
# print the JSON string representation of the object
print StudyReturnAllOf.to_json()

# convert the object into a dict
study_return_all_of_dict = study_return_all_of_instance.to_dict()
# create an instance of StudyReturnAllOf from a dict
study_return_all_of_form_dict = study_return_all_of.from_dict(study_return_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


