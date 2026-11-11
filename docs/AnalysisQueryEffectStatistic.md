# AnalysisQueryEffectStatistic

The statistic the analysis reports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**degrees_of_freedom_numerator** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**degrees_of_freedom_denominator** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_effect_statistic import AnalysisQueryEffectStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryEffectStatistic from a JSON string
analysis_query_effect_statistic_instance = AnalysisQueryEffectStatistic.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryEffectStatistic.to_json())

# convert the object into a dict
analysis_query_effect_statistic_dict = analysis_query_effect_statistic_instance.to_dict()
# create an instance of AnalysisQueryEffectStatistic from a dict
analysis_query_effect_statistic_from_dict = AnalysisQueryEffectStatistic.from_dict(analysis_query_effect_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


