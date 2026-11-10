# AnalysisQueryPreprocessing

The preprocessing of the analysis's model and of the models it takes inputs from. Smoothing FWHM in millimetres. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smoothing_fwhm** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**software** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**steps** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_preprocessing import AnalysisQueryPreprocessing

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryPreprocessing from a JSON string
analysis_query_preprocessing_instance = AnalysisQueryPreprocessing.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryPreprocessing.to_json())

# convert the object into a dict
analysis_query_preprocessing_dict = analysis_query_preprocessing_instance.to_dict()
# create an instance of AnalysisQueryPreprocessing from a dict
analysis_query_preprocessing_from_dict = AnalysisQueryPreprocessing.from_dict(analysis_query_preprocessing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


