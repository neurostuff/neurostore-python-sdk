# FulltextSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**base_study_id** | **str** |  | [optional] 
**source** | **str** | The ingestion source the text came from (&#x60;pubget&#x60;, &#x60;elsevier&#x60;, ...). | [optional] 
**source_version** | **str** |  | [optional] 
**license** | [**LicenseId**](LicenseId.md) | The licence of the copy the text was read from. | [optional] 
**sha256** | **str** |  | [optional] 
**text_copy** | **object** | The copy the text was read from (study_schema&#39;s HeldCopy). | [optional] 
**preferred** | **bool** | Whether this is the base study&#39;s &#x60;fulltext_id&#x60;. | [optional] 
**redistributable** | **bool** | Whether GET /fulltexts/{id} returns the text. | [optional] 
**attribution** | [**FulltextAttribution**](FulltextAttribution.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.fulltext_summary import FulltextSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FulltextSummary from a JSON string
fulltext_summary_instance = FulltextSummary.from_json(json)
# print the JSON string representation of the object
print(FulltextSummary.to_json())

# convert the object into a dict
fulltext_summary_dict = fulltext_summary_instance.to_dict()
# create an instance of FulltextSummary from a dict
fulltext_summary_from_dict = FulltextSummary.from_dict(fulltext_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


