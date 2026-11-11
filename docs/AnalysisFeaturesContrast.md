# AnalysisFeaturesContrast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**AnalysisFeaturesContrastKey**](AnalysisFeaturesContrastKey.md) |  | [optional] 
**set** | [**AnalysisFeaturesContrastKey**](AnalysisFeaturesContrastKey.md) |  | [optional] 
**kind** | **str** |  | [optional] 
**groups** | **str** |  | [optional] 
**positive** | [**AnalysisFeaturesContrastPositive**](AnalysisFeaturesContrastPositive.md) |  | [optional] 
**negative** | [**AnalysisFeaturesContrastPositive**](AnalysisFeaturesContrastPositive.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_contrast import AnalysisFeaturesContrast

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesContrast from a JSON string
analysis_features_contrast_instance = AnalysisFeaturesContrast.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesContrast.to_json())

# convert the object into a dict
analysis_features_contrast_dict = analysis_features_contrast_instance.to_dict()
# create an instance of AnalysisFeaturesContrast from a dict
analysis_features_contrast_from_dict = AnalysisFeaturesContrast.from_dict(analysis_features_contrast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


