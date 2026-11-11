# AnalysisFeaturesEffectStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** |  | [optional] 
**degrees_of_freedom_numerator** | **float** |  | [optional] 
**degrees_of_freedom_denominator** | **float** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_effect_statistic import AnalysisFeaturesEffectStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesEffectStatistic from a JSON string
analysis_features_effect_statistic_instance = AnalysisFeaturesEffectStatistic.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesEffectStatistic.to_json())

# convert the object into a dict
analysis_features_effect_statistic_dict = analysis_features_effect_statistic_instance.to_dict()
# create an instance of AnalysisFeaturesEffectStatistic from a dict
analysis_features_effect_statistic_from_dict = AnalysisFeaturesEffectStatistic.from_dict(analysis_features_effect_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


