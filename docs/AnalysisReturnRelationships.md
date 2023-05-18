# AnalysisReturnRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study** | **str** |  | [optional] 
**images** | [**AnalysisReturnRelationshipsImages**](AnalysisReturnRelationshipsImages.md) |  | [optional] 
**points** | [**AnalysisReturnRelationshipsPoints**](AnalysisReturnRelationshipsPoints.md) |  | [optional] 
**conditions** | [**AnalysisReturnRelationshipsConditions**](AnalysisReturnRelationshipsConditions.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_return_relationships import AnalysisReturnRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReturnRelationships from a JSON string
analysis_return_relationships_instance = AnalysisReturnRelationships.from_json(json)
# print the JSON string representation of the object
print AnalysisReturnRelationships.to_json()

# convert the object into a dict
analysis_return_relationships_dict = analysis_return_relationships_instance.to_dict()
# create an instance of AnalysisReturnRelationships from a dict
analysis_return_relationships_form_dict = analysis_return_relationships.from_dict(analysis_return_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


