# BaseStudyReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **object** |  | [optional] 
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
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 

## Example

```python
from neurostore_sdk.models.base_study_return import BaseStudyReturn

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudyReturn from a JSON string
base_study_return_instance = BaseStudyReturn.from_json(json)
# print the JSON string representation of the object
print(BaseStudyReturn.to_json())

# convert the object into a dict
base_study_return_dict = base_study_return_instance.to_dict()
# create an instance of BaseStudyReturn from a dict
base_study_return_from_dict = BaseStudyReturn.from_dict(base_study_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


