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
**license** | **str** | A value of study_schema&#39;s &#x60;LicenseId&#x60; (https://github.com/neurostuff/study_schema/blob/main/src/study_schema/linkml/neuroimaging-study-storage/license.yaml), such as &#x60;cc_by&#x60; or &#x60;all_rights_reserved&#x60;; any other value is refused. The values it annotates &#x60;redistributable&#x60; let a text be passed on with attribution. | [optional] 
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


