# AnalysisRequestRelationshipsPointsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** | Location of the significant coordinate in three dimensional space. | [optional] 
**space** | **str** | Template space used to determine coordinate Examples include TAL or MNI. | [optional] 
**kind** | **str** | Method of how point was derived (e.g., center of mass) | [optional] 
**label_id** | **str** | If the point is associated with an image, this is the value the point takes in that image. | [optional] 
**image** | **str** |  | [optional] 
**value** | [**PointRelationshipsValue**](PointRelationshipsValue.md) |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**analysis** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_request_relationships_points_inner import AnalysisRequestRelationshipsPointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisRequestRelationshipsPointsInner from a JSON string
analysis_request_relationships_points_inner_instance = AnalysisRequestRelationshipsPointsInner.from_json(json)
# print the JSON string representation of the object
print AnalysisRequestRelationshipsPointsInner.to_json()

# convert the object into a dict
analysis_request_relationships_points_inner_dict = analysis_request_relationships_points_inner_instance.to_dict()
# create an instance of AnalysisRequestRelationshipsPointsInner from a dict
analysis_request_relationships_points_inner_form_dict = analysis_request_relationships_points_inner.from_dict(analysis_request_relationships_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


