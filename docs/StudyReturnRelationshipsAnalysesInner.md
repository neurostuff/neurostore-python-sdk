# StudyReturnRelationshipsAnalysesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name of the contrast being performed. | [optional] 
**description** | **str** | A long form description of how the contrast was performed | [optional] 
**weights** | **List[float]** | Weight applied to each condition, must be the same length as the conditions attribute. | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when was the resource last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**study** | **str** |  | [optional] 
**images** | [**List[AnalysisReturnRelationshipsImagesInner]**](AnalysisReturnRelationshipsImagesInner.md) |  | [optional] 
**points** | [**List[AnalysisReturnRelationshipsPointsInner]**](AnalysisReturnRelationshipsPointsInner.md) |  | [optional] 
**conditions** | [**List[AnalysisReturnRelationshipsConditionsInner]**](AnalysisReturnRelationshipsConditionsInner.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_return_relationships_analyses_inner import StudyReturnRelationshipsAnalysesInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudyReturnRelationshipsAnalysesInner from a JSON string
study_return_relationships_analyses_inner_instance = StudyReturnRelationshipsAnalysesInner.from_json(json)
# print the JSON string representation of the object
print StudyReturnRelationshipsAnalysesInner.to_json()

# convert the object into a dict
study_return_relationships_analyses_inner_dict = study_return_relationships_analyses_inner_instance.to_dict()
# create an instance of StudyReturnRelationshipsAnalysesInner from a dict
study_return_relationships_analyses_inner_form_dict = study_return_relationships_analyses_inner.from_dict(study_return_relationships_analyses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


