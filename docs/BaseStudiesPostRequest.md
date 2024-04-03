# BaseStudiesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**versions** | [**BaseStudyVersions**](BaseStudyVersions.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**publication** | **str** |  | [optional] 
**doi** | **str** |  | [optional] 
**pmid** | **str** |  | [optional] 
**authors** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**level** | **str** |  | [optional] 
**pmcid** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.base_studies_post_request import BaseStudiesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudiesPostRequest from a JSON string
base_studies_post_request_instance = BaseStudiesPostRequest.from_json(json)
# print the JSON string representation of the object
print(BaseStudiesPostRequest.to_json())

# convert the object into a dict
base_studies_post_request_dict = base_studies_post_request_instance.to_dict()
# create an instance of BaseStudiesPostRequest from a dict
base_studies_post_request_form_dict = base_studies_post_request.from_dict(base_studies_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


