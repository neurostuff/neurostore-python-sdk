# FulltextWithheld

Why the text is not returned; null when it is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | &#x60;license&#x60;: the copy&#39;s licence does not allow passing the text on. &#x60;access&#x60;: the copy was obtained under text-and-data-mining terms, or how it was obtained was not recorded. &#x60;no_copy_record&#x60;: nothing records the copy, so its licence is unknown. | [optional] 
**message** | **str** |  | [optional] 
**read_at** | **str** | Where a reader can get the paper (its DOI, else its PubMed Central page). | [optional] 

## Example

```python
from neurostore_sdk.models.fulltext_withheld import FulltextWithheld

# TODO update the JSON string below
json = "{}"
# create an instance of FulltextWithheld from a JSON string
fulltext_withheld_instance = FulltextWithheld.from_json(json)
# print the JSON string representation of the object
print(FulltextWithheld.to_json())

# convert the object into a dict
fulltext_withheld_dict = fulltext_withheld_instance.to_dict()
# create an instance of FulltextWithheld from a dict
fulltext_withheld_from_dict = FulltextWithheld.from_dict(fulltext_withheld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


