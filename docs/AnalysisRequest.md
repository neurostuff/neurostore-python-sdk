# AnalysisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name of the contrast being performed. | [optional] 
**description** | **str** | A long form description of how the contrast was performed | [optional] 
**weights** | **List[float]** | Weight applied to each condition, must be the same length as the conditions attribute. | [optional] 
**study** | **str** |  | [optional] 
**images** | [**AnalysisRequestRelationshipsImages**](AnalysisRequestRelationshipsImages.md) |  | [optional] 
**points** | [**AnalysisRequestRelationshipsPoints**](AnalysisRequestRelationshipsPoints.md) |  | [optional] 
**conditions** | [**AnalysisRequestRelationshipsConditions**](AnalysisRequestRelationshipsConditions.md) |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**order** | **int** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_request import AnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisRequest from a JSON string
analysis_request_instance = AnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(AnalysisRequest.to_json())

# convert the object into a dict
analysis_request_dict = analysis_request_instance.to_dict()
# create an instance of AnalysisRequest from a dict
analysis_request_from_dict = AnalysisRequest.from_dict(analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


