# AnalysisQueryNormalizedOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**AnalysisQueryStrings**](AnalysisQueryStrings.md) |  | [optional] 
**text** | [**AnalysisQueryStrings**](AnalysisQueryStrings.md) |  | [optional] 
**all** | [**AnalysisQueryTerms**](AnalysisQueryTerms.md) |  | [optional] 
**var_none** | [**AnalysisQueryTerms**](AnalysisQueryTerms.md) |  | [optional] 
**descendants** | **bool** | Whether an id also matches the terms below it in its vocabulary. | [optional] [default to True]
**when_unmapped** | **str** |  | [optional] [default to 'exclude']
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_normalized_one_of import AnalysisQueryNormalizedOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryNormalizedOneOf from a JSON string
analysis_query_normalized_one_of_instance = AnalysisQueryNormalizedOneOf.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryNormalizedOneOf.to_json())

# convert the object into a dict
analysis_query_normalized_one_of_dict = analysis_query_normalized_one_of_instance.to_dict()
# create an instance of AnalysisQueryNormalizedOneOf from a dict
analysis_query_normalized_one_of_from_dict = AnalysisQueryNormalizedOneOf.from_dict(analysis_query_normalized_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


