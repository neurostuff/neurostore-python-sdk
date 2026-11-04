# StudySchemaUploadPipeline

The pipeline run that produced the record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Default pondie. | [optional] 
**version** | **str** | Default the record&#39;s extraction_metadata.extractor_version. | [optional] 
**commit** | **str** | The commit of the code that produced the record. Two commits of one version are different configs. | [optional] 
**runs** | [**List[StudySchemaRun]**](StudySchemaRun.md) | The runs that made the record: its record run, and the evidence and normalize runs that filled it in, at most one per stage. The record&#39;s config holds them in stage order with every field present, so uploads made by the same runs share one config and any other run gets another. Without runs the config is keyed as before. Validated by the service (422 SCHEMA, DUPLICATE_STAGE, DUPLICATE_RUN_ID, RUN_CONFLICT).  | [optional] 

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


