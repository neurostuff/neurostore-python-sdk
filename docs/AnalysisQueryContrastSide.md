# AnalysisQueryContrastSide

Criteria on one side of the contrast: what the cells signed onto it carry, through their factor levels. `name` is the side's text (its cells' labels or levels and their conditions' names); has_patients, has_healthy and medical_condition read the side's groups as the top-level criteria read the analysis's; `timepoint` is a timepoint's relation_to_intervention, `arm_kind` an arm's kind, and `facet` one of the side's contrast-key facets (`valence:negative`, `~wording`, a baseline kind such as `fixation`). A text criterion in its place is shorthand for its `name`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any** | **List[str]** |  | [optional] 
**all** | **List[str]** |  | [optional] 
**var_none** | **List[str]** |  | [optional] 
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]
**name** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**has_patients** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**has_healthy** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**medical_condition** | [**AnalysisQueryNormalized**](AnalysisQueryNormalized.md) |  | [optional] 
**timepoint** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**arm_kind** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**facet** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_contrast_side import AnalysisQueryContrastSide

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryContrastSide from a JSON string
analysis_query_contrast_side_instance = AnalysisQueryContrastSide.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryContrastSide.to_json())

# convert the object into a dict
analysis_query_contrast_side_dict = analysis_query_contrast_side_instance.to_dict()
# create an instance of AnalysisQueryContrastSide from a dict
analysis_query_contrast_side_from_dict = AnalysisQueryContrastSide.from_dict(analysis_query_contrast_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


