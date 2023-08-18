# BaseStudyList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BaseStudyReturn]**](BaseStudyReturn.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.base_study_list import BaseStudyList

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudyList from a JSON string
base_study_list_instance = BaseStudyList.from_json(json)
# print the JSON string representation of the object
print BaseStudyList.to_json()

# convert the object into a dict
base_study_list_dict = base_study_list_instance.to_dict()
# create an instance of BaseStudyList from a dict
base_study_list_form_dict = base_study_list.from_dict(base_study_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


