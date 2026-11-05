# JournalSummary

The journal the paper appeared in, as neurostore identified it; null when it could not be identified. `publication` keeps the name as the source printed it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.journal_summary import JournalSummary

# TODO update the JSON string below
json = "{}"
# create an instance of JournalSummary from a JSON string
journal_summary_instance = JournalSummary.from_json(json)
# print the JSON string representation of the object
print(JournalSummary.to_json())

# convert the object into a dict
journal_summary_dict = journal_summary_instance.to_dict()
# create an instance of JournalSummary from a dict
journal_summary_from_dict = JournalSummary.from_dict(journal_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


