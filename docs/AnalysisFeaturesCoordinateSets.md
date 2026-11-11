# AnalysisFeaturesCoordinateSets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **List[str]** |  | [optional] 
**result_kind** | **List[str]** |  | [optional] 
**anchor_kind** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_coordinate_sets import AnalysisFeaturesCoordinateSets

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesCoordinateSets from a JSON string
analysis_features_coordinate_sets_instance = AnalysisFeaturesCoordinateSets.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesCoordinateSets.to_json())

# convert the object into a dict
analysis_features_coordinate_sets_dict = analysis_features_coordinate_sets_instance.to_dict()
# create an instance of AnalysisFeaturesCoordinateSets from a dict
analysis_features_coordinate_sets_from_dict = AnalysisFeaturesCoordinateSets.from_dict(analysis_features_coordinate_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


