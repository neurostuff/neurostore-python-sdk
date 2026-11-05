# JournalReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**openalex_id** | **str** | OpenAlex&#39;s source id, bare (&#x60;S121666818&#x60;). | [optional] 
**title** | **str** | OpenAlex&#39;s name for the source. | [optional] 
**abbreviation** | **str** | NLM&#39;s ISO abbreviation, else its MEDLINE abbreviation. | [optional] 
**kind** | [**JournalKind**](JournalKind.md) |  | [optional] 
**issns** | **List[str]** | Every ISSN of the title, print and electronic. | [optional] 
**issn_l** | **str** | Which of &#x60;issns&#x60; links the title&#39;s print and electronic versions. | [optional] 
**nlm_id** | **str** | The NLM Catalog&#39;s id for the title. | [optional] 
**wikidata_id** | **str** | Wikidata&#39;s item for the title (&#x60;Q5936947&#x60;). | [optional] 

## Example

```python
from neurostore_sdk.models.journal_return import JournalReturn

# TODO update the JSON string below
json = "{}"
# create an instance of JournalReturn from a JSON string
journal_return_instance = JournalReturn.from_json(json)
# print the JSON string representation of the object
print(JournalReturn.to_json())

# convert the object into a dict
journal_return_dict = journal_return_instance.to_dict()
# create an instance of JournalReturn from a dict
journal_return_from_dict = JournalReturn.from_dict(journal_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


