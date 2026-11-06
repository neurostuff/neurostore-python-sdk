# AnalysisQueryNormalizedIdsOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**AnalysisQueryStrings**](AnalysisQueryStrings.md) |  | [optional] 
**all** | [**AnalysisQueryIds**](AnalysisQueryIds.md) |  | [optional] 
**var_none** | [**AnalysisQueryIds**](AnalysisQueryIds.md) |  | [optional] 
**descendants** | **bool** | Whether an id also matches the terms below it in its vocabulary. | [optional] [default to True]
**when_unmapped** | **str** |  | [optional] [default to 'exclude']
**when_silent** | [**AnalysisQueryWhenSilent**](AnalysisQueryWhenSilent.md) |  | [optional] [default to AnalysisQueryWhenSilent.EXCLUDE]

## Example

```python
from neurostore_sdk.models.analysis_query_normalized_ids_one_of import AnalysisQueryNormalizedIdsOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryNormalizedIdsOneOf from a JSON string
analysis_query_normalized_ids_one_of_instance = AnalysisQueryNormalizedIdsOneOf.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryNormalizedIdsOneOf.to_json())

# convert the object into a dict
analysis_query_normalized_ids_one_of_dict = analysis_query_normalized_ids_one_of_instance.to_dict()
# create an instance of AnalysisQueryNormalizedIdsOneOf from a dict
analysis_query_normalized_ids_one_of_from_dict = AnalysisQueryNormalizedIdsOneOf.from_dict(analysis_query_normalized_ids_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


