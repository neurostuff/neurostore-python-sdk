# FulltextReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**base_study_id** | **str** |  | [optional] 
**source** | **str** | The ingestion source the text came from (&#x60;pubget&#x60;, &#x60;elsevier&#x60;, ...). | [optional] 
**source_version** | **str** |  | [optional] 
**license** | **str** | The licence of the copy the text was read from. | [optional] 
**sha256** | **str** |  | [optional] 
**text_copy** | **object** | The copy the text was read from (study_schema&#39;s HeldCopy). | [optional] 
**preferred** | **bool** | Whether this is the base study&#39;s &#x60;fulltext_id&#x60;. | [optional] 
**redistributable** | **bool** | Whether GET /fulltexts/{id} returns the text. | [optional] 
**attribution** | [**FulltextAttribution**](FulltextAttribution.md) |  | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**text** | **str** | The text, when &#x60;redistributable&#x60;; else null. | [optional] 
**text_withheld** | [**FulltextWithheld**](FulltextWithheld.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.fulltext_return import FulltextReturn

# TODO update the JSON string below
json = "{}"
# create an instance of FulltextReturn from a JSON string
fulltext_return_instance = FulltextReturn.from_json(json)
# print the JSON string representation of the object
print(FulltextReturn.to_json())

# convert the object into a dict
fulltext_return_dict = fulltext_return_instance.to_dict()
# create an instance of FulltextReturn from a dict
fulltext_return_from_dict = FulltextReturn.from_dict(fulltext_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


