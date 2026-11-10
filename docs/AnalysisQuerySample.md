# AnalysisQuerySample

The groups the analysis ran on; a criterion on an item of each group (an age) matches when any group's does. Ages are in years; counts are summed over the groups. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_mean** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**age_sd** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**age_min** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**age_max** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**age_median** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**female_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**male_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**female_percent** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**handedness** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**enrolled_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**acquired_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**excluded_count** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**diagnostic_instrument** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**diagnostic_system** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**clinical_characteristics** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**education** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_sample import AnalysisQuerySample

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQuerySample from a JSON string
analysis_query_sample_instance = AnalysisQuerySample.from_json(json)
# print the JSON string representation of the object
print(AnalysisQuerySample.to_json())

# convert the object into a dict
analysis_query_sample_dict = analysis_query_sample_instance.to_dict()
# create an instance of AnalysisQuerySample from a dict
analysis_query_sample_from_dict = AnalysisQuerySample.from_dict(analysis_query_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


