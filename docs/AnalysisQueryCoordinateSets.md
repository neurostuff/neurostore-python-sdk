# AnalysisQueryCoordinateSets

The coordinate sets that name the analysis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**result_kind** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**anchor_kind** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_coordinate_sets import AnalysisQueryCoordinateSets

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryCoordinateSets from a JSON string
analysis_query_coordinate_sets_instance = AnalysisQueryCoordinateSets.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryCoordinateSets.to_json())

# convert the object into a dict
analysis_query_coordinate_sets_dict = analysis_query_coordinate_sets_instance.to_dict()
# create an instance of AnalysisQueryCoordinateSets from a dict
analysis_query_coordinate_sets_from_dict = AnalysisQueryCoordinateSets.from_dict(analysis_query_coordinate_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


