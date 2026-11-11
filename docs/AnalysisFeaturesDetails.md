# AnalysisFeaturesDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectivity_method** | **str** |  | [optional] 
**inference_target** | **str** |  | [optional] 
**seed_regions** | **List[str]** |  | [optional] 
**target_regions** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_details import AnalysisFeaturesDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesDetails from a JSON string
analysis_features_details_instance = AnalysisFeaturesDetails.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesDetails.to_json())

# convert the object into a dict
analysis_features_details_dict = analysis_features_details_instance.to_dict()
# create an instance of AnalysisFeaturesDetails from a dict
analysis_features_details_from_dict = AnalysisFeaturesDetails.from_dict(analysis_features_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


