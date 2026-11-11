# AnalysisFeaturesModelEstimation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_family** | **List[str]** |  | [optional] 
**model_type** | **List[str]** |  | [optional] 
**software** | **List[str]** |  | [optional] 
**hrf_model** | **List[str]** |  | [optional] 
**estimator** | **List[str]** |  | [optional] 
**terms** | [**AnalysisFeaturesModelEstimationTerms**](AnalysisFeaturesModelEstimationTerms.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_model_estimation import AnalysisFeaturesModelEstimation

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesModelEstimation from a JSON string
analysis_features_model_estimation_instance = AnalysisFeaturesModelEstimation.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesModelEstimation.to_json())

# convert the object into a dict
analysis_features_model_estimation_dict = analysis_features_model_estimation_instance.to_dict()
# create an instance of AnalysisFeaturesModelEstimation from a dict
analysis_features_model_estimation_from_dict = AnalysisFeaturesModelEstimation.from_dict(analysis_features_model_estimation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


