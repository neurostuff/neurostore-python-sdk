# AnalysisQueryMedicalCondition

analysis-query-normalized, and `role` (primary, comorbid, none), which narrows the ids to the conditions ns-pond gave that role; a criterion with a role takes ids and no text. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**AnalysisQueryStrings**](AnalysisQueryStrings.md) |  | [optional] 
**text** | [**AnalysisQueryStrings**](AnalysisQueryStrings.md) |  | [optional] 
**all** | [**AnalysisQueryTerms**](AnalysisQueryTerms.md) |  | [optional] 
**var_none** | [**AnalysisQueryTerms**](AnalysisQueryTerms.md) |  | [optional] 
**descendants** | **bool** | Whether an id also matches the terms below it in its vocabulary. | [optional] [default to True]
**role** | [**AnalysisQueryMedicalConditionOneOfRole**](AnalysisQueryMedicalConditionOneOfRole.md) |  | [optional] 
**when_unmapped** | **str** |  | [optional] [default to 'exclude']
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_medical_condition import AnalysisQueryMedicalCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryMedicalCondition from a JSON string
analysis_query_medical_condition_instance = AnalysisQueryMedicalCondition.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryMedicalCondition.to_json())

# convert the object into a dict
analysis_query_medical_condition_dict = analysis_query_medical_condition_instance.to_dict()
# create an instance of AnalysisQueryMedicalCondition from a dict
analysis_query_medical_condition_from_dict = AnalysisQueryMedicalCondition.from_dict(analysis_query_medical_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


