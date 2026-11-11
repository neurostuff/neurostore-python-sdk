# AnalysisFeaturesPreprocessing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smoothing_fwhm_mm** | **List[float]** |  | [optional] 
**software** | **List[str]** |  | [optional] 
**steps** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_preprocessing import AnalysisFeaturesPreprocessing

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesPreprocessing from a JSON string
analysis_features_preprocessing_instance = AnalysisFeaturesPreprocessing.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesPreprocessing.to_json())

# convert the object into a dict
analysis_features_preprocessing_dict = analysis_features_preprocessing_instance.to_dict()
# create an instance of AnalysisFeaturesPreprocessing from a dict
analysis_features_preprocessing_from_dict = AnalysisFeaturesPreprocessing.from_dict(analysis_features_preprocessing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


