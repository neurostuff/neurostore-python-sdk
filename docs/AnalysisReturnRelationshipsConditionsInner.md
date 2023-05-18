# AnalysisReturnRelationshipsConditionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the condition being applied in the contrast, either psychological, pharmacological, or group based. | [optional] 
**description** | **str** | Long form description of how the condition is operationalized and/or specific meaning. | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when was the resource last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 

## Example

```python
from neurostore_sdk.models.analysis_return_relationships_conditions_inner import AnalysisReturnRelationshipsConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReturnRelationshipsConditionsInner from a JSON string
analysis_return_relationships_conditions_inner_instance = AnalysisReturnRelationshipsConditionsInner.from_json(json)
# print the JSON string representation of the object
print AnalysisReturnRelationshipsConditionsInner.to_json()

# convert the object into a dict
analysis_return_relationships_conditions_inner_dict = analysis_return_relationships_conditions_inner_instance.to_dict()
# create an instance of AnalysisReturnRelationshipsConditionsInner from a dict
analysis_return_relationships_conditions_inner_form_dict = analysis_return_relationships_conditions_inner.from_dict(analysis_return_relationships_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


