# StudySchemaUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinate_parse** | **Dict[str, object]** | A study_schema CoordinateParse (neuroimaging-paper-parse); a revision when revision_of is set. | [optional] 
**record** | **Dict[str, object]** | A study_schema extraction record (neuroimaging-study-extraction). | [optional] 
**parsed_paper** | **Dict[str, object]** | The ParsedPaper the parse read, for table captions and the bibliography. | [optional] 
**parse_id** | **str** | For a record uploaded alone, the parse_id of the stored parse it read. | [optional] 
**base_study_id** | **str** | The base study; otherwise found by the parse header&#39;s identifiers. | [optional] 
**run_id** | **str** | The caller&#39;s id for the pipeline run, stored on each result the upload writes. Re-uploading the same documents with the same run_id returns the same results and adds none; a run_id that already stored a different document for the paper is refused (422).  | [optional] 
**pipeline** | [**StudySchemaUploadPipeline**](StudySchemaUploadPipeline.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload import StudySchemaUpload

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUpload from a JSON string
study_schema_upload_instance = StudySchemaUpload.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUpload.to_json())

# convert the object into a dict
study_schema_upload_dict = study_schema_upload_instance.to_dict()
# create an instance of StudySchemaUpload from a dict
study_schema_upload_from_dict = StudySchemaUpload.from_dict(study_schema_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


