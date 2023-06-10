# AbstractStudyReturn


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
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when was the resource last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 

## Example

```python
from neurostore_sdk.models.abstract_study_return import AbstractStudyReturn

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractStudyReturn from a JSON string
abstract_study_return_instance = AbstractStudyReturn.from_json(json)
# print the JSON string representation of the object
print AbstractStudyReturn.to_json()

# convert the object into a dict
abstract_study_return_dict = abstract_study_return_instance.to_dict()
# create an instance of AbstractStudyReturn from a dict
abstract_study_return_form_dict = abstract_study_return.from_dict(abstract_study_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


