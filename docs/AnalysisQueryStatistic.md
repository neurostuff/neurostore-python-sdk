# AnalysisQueryStatistic

The statistic the analysis reports. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**df_numerator** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**df_denominator** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_statistic import AnalysisQueryStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryStatistic from a JSON string
analysis_query_statistic_instance = AnalysisQueryStatistic.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryStatistic.to_json())

# convert the object into a dict
analysis_query_statistic_dict = analysis_query_statistic_instance.to_dict()
# create an instance of AnalysisQueryStatistic from a dict
analysis_query_statistic_from_dict = AnalysisQueryStatistic.from_dict(analysis_query_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


