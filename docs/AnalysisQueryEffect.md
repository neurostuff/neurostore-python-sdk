# AnalysisQueryEffect

The analysis's effect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statistic** | [**AnalysisQueryEffectStatistic**](AnalysisQueryEffectStatistic.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_effect import AnalysisQueryEffect

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryEffect from a JSON string
analysis_query_effect_instance = AnalysisQueryEffect.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryEffect.to_json())

# convert the object into a dict
analysis_query_effect_dict = analysis_query_effect_instance.to_dict()
# create an instance of AnalysisQueryEffect from a dict
analysis_query_effect_from_dict = AnalysisQueryEffect.from_dict(analysis_query_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


