# AnalysisFeaturesMedicalCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 
**role_ids** | **List[str]** |  | [optional] 
**text** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_medical_condition import AnalysisFeaturesMedicalCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesMedicalCondition from a JSON string
analysis_features_medical_condition_instance = AnalysisFeaturesMedicalCondition.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesMedicalCondition.to_json())

# convert the object into a dict
analysis_features_medical_condition_dict = analysis_features_medical_condition_instance.to_dict()
# create an instance of AnalysisFeaturesMedicalCondition from a dict
analysis_features_medical_condition_from_dict = AnalysisFeaturesMedicalCondition.from_dict(analysis_features_medical_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


