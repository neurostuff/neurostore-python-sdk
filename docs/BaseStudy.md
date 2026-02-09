# BaseStudy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**versions** | [**List[BaseStudyVersionsInner]**](BaseStudyVersionsInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**publication** | **str** |  | [optional] 
**doi** | **str** |  | [optional] 
**pmid** | **str** |  | [optional] 
**authors** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**level** | **str** |  | [optional] 
**is_oa** | **bool** |  | [optional] 
**pmcid** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.base_study import BaseStudy

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudy from a JSON string
base_study_instance = BaseStudy.from_json(json)
# print the JSON string representation of the object
print(BaseStudy.to_json())

# convert the object into a dict
base_study_dict = base_study_instance.to_dict()
# create an instance of BaseStudy from a dict
base_study_from_dict = BaseStudy.from_dict(base_study_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


