# BaseStudiesPost200Response


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
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 

## Example

```python
from neurostore_sdk.models.base_studies_post200_response import BaseStudiesPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudiesPost200Response from a JSON string
base_studies_post200_response_instance = BaseStudiesPost200Response.from_json(json)
# print the JSON string representation of the object
print BaseStudiesPost200Response.to_json()

# convert the object into a dict
base_studies_post200_response_dict = base_studies_post200_response_instance.to_dict()
# create an instance of BaseStudiesPost200Response from a dict
base_studies_post200_response_form_dict = base_studies_post200_response.from_dict(base_studies_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


