# AnalysisQueryModel

The analysis's model estimation and the models it takes inputs from. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**software** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**hrf** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**estimator** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**term** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**term_type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_model import AnalysisQueryModel

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryModel from a JSON string
analysis_query_model_instance = AnalysisQueryModel.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryModel.to_json())

# convert the object into a dict
analysis_query_model_dict = analysis_query_model_instance.to_dict()
# create an instance of AnalysisQueryModel from a dict
analysis_query_model_from_dict = AnalysisQueryModel.from_dict(analysis_query_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


