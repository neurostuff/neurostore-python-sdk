# AnalysisFeaturesGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_mean** | **List[float]** |  | [optional] 
**age_standard_deviation** | **List[float]** |  | [optional] 
**age_minimum** | **List[float]** |  | [optional] 
**age_maximum** | **List[float]** |  | [optional] 
**age_median** | **List[float]** |  | [optional] 
**female_count** | **int** |  | [optional] 
**male_count** | **int** |  | [optional] 
**female_percent** | **float** |  | [optional] 
**handedness** | **List[str]** |  | [optional] 
**enrolled_count** | **int** |  | [optional] 
**acquired_count** | **int** |  | [optional] 
**excluded_count** | **int** |  | [optional] 
**diagnostic_instrument** | **List[str]** |  | [optional] 
**diagnostic_system** | **List[str]** |  | [optional] 
**clinical_characteristics** | **List[str]** |  | [optional] 
**education_summary** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_groups import AnalysisFeaturesGroups

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesGroups from a JSON string
analysis_features_groups_instance = AnalysisFeaturesGroups.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesGroups.to_json())

# convert the object into a dict
analysis_features_groups_dict = analysis_features_groups_instance.to_dict()
# create an instance of AnalysisFeaturesGroups from a dict
analysis_features_groups_from_dict = AnalysisFeaturesGroups.from_dict(analysis_features_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


