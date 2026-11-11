# AnalysisQueryContrastSideOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**has_patients** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**has_healthy** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**medical_condition** | [**AnalysisQueryNormalized**](AnalysisQueryNormalized.md) |  | [optional] 
**timepoint** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**arm_kind** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**facet** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_contrast_side_one_of import AnalysisQueryContrastSideOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryContrastSideOneOf from a JSON string
analysis_query_contrast_side_one_of_instance = AnalysisQueryContrastSideOneOf.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryContrastSideOneOf.to_json())

# convert the object into a dict
analysis_query_contrast_side_one_of_dict = analysis_query_contrast_side_one_of_instance.to_dict()
# create an instance of AnalysisQueryContrastSideOneOf from a dict
analysis_query_contrast_side_one_of_from_dict = AnalysisQueryContrastSideOneOf.from_dict(analysis_query_contrast_side_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


