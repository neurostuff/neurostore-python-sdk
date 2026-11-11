# AnalysisFeaturesContrastPositive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **List[str]** |  | [optional] 
**has_patients** | **bool** |  | [optional] 
**has_healthy** | **bool** |  | [optional] 
**medical_condition** | [**AnalysisFeaturesContrastKey**](AnalysisFeaturesContrastKey.md) |  | [optional] 
**timepoint** | **List[str]** |  | [optional] 
**arm_kind** | **List[str]** |  | [optional] 
**facet** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_contrast_positive import AnalysisFeaturesContrastPositive

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesContrastPositive from a JSON string
analysis_features_contrast_positive_instance = AnalysisFeaturesContrastPositive.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesContrastPositive.to_json())

# convert the object into a dict
analysis_features_contrast_positive_dict = analysis_features_contrast_positive_instance.to_dict()
# create an instance of AnalysisFeaturesContrastPositive from a dict
analysis_features_contrast_positive_from_dict = AnalysisFeaturesContrastPositive.from_dict(analysis_features_contrast_positive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


