# AnalysisQueryGroups

The groups the analysis ran on; a number with an item per group (an age) matches when any group's does. Ages are in years; counts are summed over the groups; the female share is of those whose sex (or, where only that is reported, gender) is counted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_mean** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**age_standard_deviation** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**age_minimum** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**age_maximum** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**age_median** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**female_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**male_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**female_percent** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**handedness** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**enrolled_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**acquired_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**excluded_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**diagnostic_instrument** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**diagnostic_system** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**clinical_characteristics** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**education_summary** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_groups import AnalysisQueryGroups

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryGroups from a JSON string
analysis_query_groups_instance = AnalysisQueryGroups.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryGroups.to_json())

# convert the object into a dict
analysis_query_groups_dict = analysis_query_groups_instance.to_dict()
# create an instance of AnalysisQueryGroups from a dict
analysis_query_groups_from_dict = AnalysisQueryGroups.from_dict(analysis_query_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


