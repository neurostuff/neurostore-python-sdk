# AnalysisQueryModelEstimation

The analysis's model estimation and the models it takes inputs from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_family** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**model_type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**software** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**hrf_model** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**estimator** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**terms** | [**AnalysisQueryModelEstimationTerms**](AnalysisQueryModelEstimationTerms.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_model_estimation import AnalysisQueryModelEstimation

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryModelEstimation from a JSON string
analysis_query_model_estimation_instance = AnalysisQueryModelEstimation.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryModelEstimation.to_json())

# convert the object into a dict
analysis_query_model_estimation_dict = analysis_query_model_estimation_instance.to_dict()
# create an instance of AnalysisQueryModelEstimation from a dict
analysis_query_model_estimation_from_dict = AnalysisQueryModelEstimation.from_dict(analysis_query_model_estimation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


