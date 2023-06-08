# AbstractStudy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**versions** | [**AbstractStudyVersions**](AbstractStudyVersions.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**publication** | **str** |  | [optional] 
**doi** | **str** |  | [optional] 
**pmid** | **str** |  | [optional] 
**authors** | **str** |  | [optional] 
**year** | **str** |  | [optional] 
**level** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.abstract_study import AbstractStudy

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractStudy from a JSON string
abstract_study_instance = AbstractStudy.from_json(json)
# print the JSON string representation of the object
print AbstractStudy.to_json()

# convert the object into a dict
abstract_study_dict = abstract_study_instance.to_dict()
# create an instance of AbstractStudy from a dict
abstract_study_form_dict = abstract_study.from_dict(abstract_study_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


