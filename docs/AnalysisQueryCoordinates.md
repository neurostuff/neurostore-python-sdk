# AnalysisQueryCoordinates

The coordinate sets that name the analysis. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**result_kind** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**anchor_kind** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_coordinates import AnalysisQueryCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryCoordinates from a JSON string
analysis_query_coordinates_instance = AnalysisQueryCoordinates.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryCoordinates.to_json())

# convert the object into a dict
analysis_query_coordinates_dict = analysis_query_coordinates_instance.to_dict()
# create an instance of AnalysisQueryCoordinates from a dict
analysis_query_coordinates_from_dict = AnalysisQueryCoordinates.from_dict(analysis_query_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


