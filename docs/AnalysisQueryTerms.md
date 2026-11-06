# AnalysisQueryTerms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**AnalysisQueryStrings**](AnalysisQueryStrings.md) |  | [optional] 
**text** | [**AnalysisQueryStrings**](AnalysisQueryStrings.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_terms import AnalysisQueryTerms

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryTerms from a JSON string
analysis_query_terms_instance = AnalysisQueryTerms.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryTerms.to_json())

# convert the object into a dict
analysis_query_terms_dict = analysis_query_terms_instance.to_dict()
# create an instance of AnalysisQueryTerms from a dict
analysis_query_terms_from_dict = AnalysisQueryTerms.from_dict(analysis_query_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


