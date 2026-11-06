# AnalysisQueryNormalizedIds

Ids (an id, or a list of them, any of which may match), as analysis-query-normalized without text. An analysis whose record states the feature but maps none of it is excluded unless `when_unmapped` is `include`. 

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
from neurostore_sdk.models.analysis_query_normalized_ids import AnalysisQueryNormalizedIds

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryNormalizedIds from a JSON string
analysis_query_normalized_ids_instance = AnalysisQueryNormalizedIds.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryNormalizedIds.to_json())

# convert the object into a dict
analysis_query_normalized_ids_dict = analysis_query_normalized_ids_instance.to_dict()
# create an instance of AnalysisQueryNormalizedIds from a dict
analysis_query_normalized_ids_from_dict = AnalysisQueryNormalizedIds.from_dict(analysis_query_normalized_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


