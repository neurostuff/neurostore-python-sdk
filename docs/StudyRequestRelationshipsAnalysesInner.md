# StudyRequestRelationshipsAnalysesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name of the contrast being performed. | [optional] 
**description** | **str** | A long form description of how the contrast was performed | [optional] 
**weights** | **List[float]** | Weight applied to each condition, must be the same length as the conditions attribute. | [optional] 
**study** | **str** |  | [optional] 
**images** | [**List[AnalysisRequestRelationshipsImagesInner]**](AnalysisRequestRelationshipsImagesInner.md) |  | [optional] 
**points** | [**List[AnalysisRequestRelationshipsPointsInner]**](AnalysisRequestRelationshipsPointsInner.md) |  | [optional] 
**conditions** | [**List[AnalysisRequestRelationshipsConditionsInner]**](AnalysisRequestRelationshipsConditionsInner.md) |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]

## Example

```python
from neurostore_sdk.models.study_request_relationships_analyses_inner import StudyRequestRelationshipsAnalysesInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudyRequestRelationshipsAnalysesInner from a JSON string
study_request_relationships_analyses_inner_instance = StudyRequestRelationshipsAnalysesInner.from_json(json)
# print the JSON string representation of the object
print StudyRequestRelationshipsAnalysesInner.to_json()

# convert the object into a dict
study_request_relationships_analyses_inner_dict = study_request_relationships_analyses_inner_instance.to_dict()
# create an instance of StudyRequestRelationshipsAnalysesInner from a dict
study_request_relationships_analyses_inner_form_dict = study_request_relationships_analyses_inner.from_dict(study_request_relationships_analyses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


