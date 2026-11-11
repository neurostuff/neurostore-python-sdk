# AnalysisQueryDesign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**assignment_structure** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**blinding** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**arm_kind** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**longitudinal** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_design import AnalysisQueryDesign

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryDesign from a JSON string
analysis_query_design_instance = AnalysisQueryDesign.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryDesign.to_json())

# convert the object into a dict
analysis_query_design_dict = analysis_query_design_instance.to_dict()
# create an instance of AnalysisQueryDesign from a dict
analysis_query_design_from_dict = AnalysisQueryDesign.from_dict(analysis_query_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


