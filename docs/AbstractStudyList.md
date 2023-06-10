# AbstractStudyList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AbstractStudyReturn]**](AbstractStudyReturn.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.abstract_study_list import AbstractStudyList

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractStudyList from a JSON string
abstract_study_list_instance = AbstractStudyList.from_json(json)
# print the JSON string representation of the object
print AbstractStudyList.to_json()

# convert the object into a dict
abstract_study_list_dict = abstract_study_list_instance.to_dict()
# create an instance of AbstractStudyList from a dict
abstract_study_list_form_dict = abstract_study_list.from_dict(abstract_study_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


