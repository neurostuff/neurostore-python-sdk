# AnalysisRequestRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study** | **str** |  | [optional] 
**images** | [**AnalysisRequestRelationshipsImages**](AnalysisRequestRelationshipsImages.md) |  | [optional] 
**points** | [**AnalysisRequestRelationshipsPoints**](AnalysisRequestRelationshipsPoints.md) |  | [optional] 
**conditions** | [**AnalysisRequestRelationshipsConditions**](AnalysisRequestRelationshipsConditions.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_request_relationships import AnalysisRequestRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisRequestRelationships from a JSON string
analysis_request_relationships_instance = AnalysisRequestRelationships.from_json(json)
# print the JSON string representation of the object
print(AnalysisRequestRelationships.to_json())

# convert the object into a dict
analysis_request_relationships_dict = analysis_request_relationships_instance.to_dict()
# create an instance of AnalysisRequestRelationships from a dict
analysis_request_relationships_from_dict = AnalysisRequestRelationships.from_dict(analysis_request_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


