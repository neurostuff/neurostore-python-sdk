# AnalysisFeaturesAcquisitions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modality** | **List[str]** |  | [optional] 
**magnetic_field_strength_tesla** | **List[float]** |  | [optional] 
**repetition_time_seconds** | **List[float]** |  | [optional] 
**echo_time_seconds** | **List[float]** |  | [optional] 
**acquisition_voxel_size_mm** | **List[float]** |  | [optional] 
**device** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_acquisitions import AnalysisFeaturesAcquisitions

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesAcquisitions from a JSON string
analysis_features_acquisitions_instance = AnalysisFeaturesAcquisitions.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesAcquisitions.to_json())

# convert the object into a dict
analysis_features_acquisitions_dict = analysis_features_acquisitions_instance.to_dict()
# create an instance of AnalysisFeaturesAcquisitions from a dict
analysis_features_acquisitions_from_dict = AnalysisFeaturesAcquisitions.from_dict(analysis_features_acquisitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


