# NeurostoreStudysetReleasesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**NeurostoreStudysetReleasesGet200ResponseMetadata**](NeurostoreStudysetReleasesGet200ResponseMetadata.md) |  | [optional] 
**results** | **List[object]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.neurostore_studyset_releases_get200_response import NeurostoreStudysetReleasesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of NeurostoreStudysetReleasesGet200Response from a JSON string
neurostore_studyset_releases_get200_response_instance = NeurostoreStudysetReleasesGet200Response.from_json(json)
# print the JSON string representation of the object
print(NeurostoreStudysetReleasesGet200Response.to_json())

# convert the object into a dict
neurostore_studyset_releases_get200_response_dict = neurostore_studyset_releases_get200_response_instance.to_dict()
# create an instance of NeurostoreStudysetReleasesGet200Response from a dict
neurostore_studyset_releases_get200_response_from_dict = NeurostoreStudysetReleasesGet200Response.from_dict(neurostore_studyset_releases_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


