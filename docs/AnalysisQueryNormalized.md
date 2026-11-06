# AnalysisQueryNormalized

Text (a pattern, or a list of them, any of which may match), or ids and text. `ids` and `text` are any-of, and either may match; `all` needs every one and `none` refuses each. `when_unmapped` decides an analysis whose record states the feature but maps none of it: `exclude` (the default), `include`, or `text`, matching it by its wording alone, so a criterion without text excludes it. 

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
from neurostore_sdk.models.analysis_query_normalized import AnalysisQueryNormalized

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryNormalized from a JSON string
analysis_query_normalized_instance = AnalysisQueryNormalized.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryNormalized.to_json())

# convert the object into a dict
analysis_query_normalized_dict = analysis_query_normalized_instance.to_dict()
# create an instance of AnalysisQueryNormalized from a dict
analysis_query_normalized_from_dict = AnalysisQueryNormalized.from_dict(analysis_query_normalized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


