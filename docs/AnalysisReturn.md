# AnalysisReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name of the contrast being performed. | [optional] 
**description** | **str** | A long form description of how the contrast was performed | [optional] 
**weights** | **List[float]** | Weight applied to each condition, must be the same length as the conditions attribute. | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 
**study** | **str** |  | [optional] 
**images** | [**AnalysisReturnRelationshipsImages**](AnalysisReturnRelationshipsImages.md) |  | [optional] 
**points** | [**AnalysisReturnRelationshipsPoints**](AnalysisReturnRelationshipsPoints.md) |  | [optional] 
**conditions** | [**AnalysisReturnRelationshipsConditions**](AnalysisReturnRelationshipsConditions.md) |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**order** | **int** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_return import AnalysisReturn

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReturn from a JSON string
analysis_return_instance = AnalysisReturn.from_json(json)
# print the JSON string representation of the object
print AnalysisReturn.to_json()

# convert the object into a dict
analysis_return_dict = analysis_return_instance.to_dict()
# create an instance of AnalysisReturn from a dict
analysis_return_form_dict = analysis_return.from_dict(analysis_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


