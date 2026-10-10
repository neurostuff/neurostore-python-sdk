# StudySchemaUploadsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provenance** | [**Dict[str, PipelineRunProvenance]**](PipelineRunProvenance.md) | The stored run behind each part of the upload, keyed parse and record. | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_uploads_post200_response import StudySchemaUploadsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadsPost200Response from a JSON string
study_schema_uploads_post200_response_instance = StudySchemaUploadsPost200Response.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadsPost200Response.to_json())

# convert the object into a dict
study_schema_uploads_post200_response_dict = study_schema_uploads_post200_response_instance.to_dict()
# create an instance of StudySchemaUploadsPost200Response from a dict
study_schema_uploads_post200_response_from_dict = StudySchemaUploadsPost200Response.from_dict(study_schema_uploads_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


