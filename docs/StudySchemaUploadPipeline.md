# StudySchemaUploadPipeline

The pipeline that produced the record (name; default pondie).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_pipeline import StudySchemaUploadPipeline

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadPipeline from a JSON string
study_schema_upload_pipeline_instance = StudySchemaUploadPipeline.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadPipeline.to_json())

# convert the object into a dict
study_schema_upload_pipeline_dict = study_schema_upload_pipeline_instance.to_dict()
# create an instance of StudySchemaUploadPipeline from a dict
study_schema_upload_pipeline_from_dict = StudySchemaUploadPipeline.from_dict(study_schema_upload_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


