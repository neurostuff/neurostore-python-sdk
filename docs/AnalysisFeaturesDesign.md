# AnalysisFeaturesDesign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | **str** |  | [optional] 
**assignment_structure** | **str** |  | [optional] 
**blinding** | **str** |  | [optional] 
**arm_kind** | **List[str]** |  | [optional] 
**longitudinal** | **bool** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features_design import AnalysisFeaturesDesign

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeaturesDesign from a JSON string
analysis_features_design_instance = AnalysisFeaturesDesign.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeaturesDesign.to_json())

# convert the object into a dict
analysis_features_design_dict = analysis_features_design_instance.to_dict()
# create an instance of AnalysisFeaturesDesign from a dict
analysis_features_design_from_dict = AnalysisFeaturesDesign.from_dict(analysis_features_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


