# AnalysisFeaturesRegions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **List[str]** |  | [optional] 
**atlas** | **List[str]** |  | [optional] 
**region_type** | **List[str]** |  | [optional] 
**definition_method** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_regions import AnalysisFeaturesRegions

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesRegions from a JSON string
analysis_features_regions_instance = AnalysisFeaturesRegions.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesRegions.to_json())

# convert the object into a dict
analysis_features_regions_dict = analysis_features_regions_instance.to_dict()
# create an instance of AnalysisFeaturesRegions from a dict
analysis_features_regions_from_dict = AnalysisFeaturesRegions.from_dict(analysis_features_regions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


