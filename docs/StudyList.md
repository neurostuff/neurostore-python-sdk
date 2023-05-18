# StudyList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[StudyReturn]**](StudyReturn.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_list import StudyList

# TODO update the JSON string below
json = "{}"
# create an instance of StudyList from a JSON string
study_list_instance = StudyList.from_json(json)
# print the JSON string representation of the object
print StudyList.to_json()

# convert the object into a dict
study_list_dict = study_list_instance.to_dict()
# create an instance of StudyList from a dict
study_list_form_dict = study_list.from_dict(study_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


