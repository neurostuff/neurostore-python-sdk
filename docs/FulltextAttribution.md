# FulltextAttribution

What to credit when passing the text on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**authors** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**publication** | **str** |  | [optional] 
**doi** | **str** |  | [optional] 
**license** | [**LicenseId**](LicenseId.md) |  | [optional] 
**license_statement** | **str** | The licence as its source stated it (a licence URL, name or copyright line). | [optional] 

## Example

```python
from neurostore_sdk.models.fulltext_attribution import FulltextAttribution

# TODO update the JSON string below
json = "{}"
# create an instance of FulltextAttribution from a JSON string
fulltext_attribution_instance = FulltextAttribution.from_json(json)
# print the JSON string representation of the object
print(FulltextAttribution.to_json())

# convert the object into a dict
fulltext_attribution_dict = fulltext_attribution_instance.to_dict()
# create an instance of FulltextAttribution from a dict
fulltext_attribution_from_dict = FulltextAttribution.from_dict(fulltext_attribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


