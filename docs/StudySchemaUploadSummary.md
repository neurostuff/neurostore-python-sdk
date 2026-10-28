# StudySchemaUploadSummary

What one upload changed. Keys appear for the parts uploaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**base_study_id** | **str** |  | [optional] 
**merged_from** | **List[str]** | The base study the upload named, and each one between it and base_study_id, when it was merged into base_study_id and the upload followed the merge. Absent otherwise.  | [optional] 
**took_ownership_from** | **str** | The user who owned the base study before this upload, which leaves it owned by no one and public. Absent when no one did.  | [optional] 
**study_id** | **str** | The paper&#39;s pipeline-owned study. | [optional] 
**parse_id** | **str** |  | [optional] 
**skeleton** | [**StudySchemaUploadSummarySkeleton**](StudySchemaUploadSummarySkeleton.md) |  | [optional] 
**carried** | [**StudySchemaCarried**](StudySchemaCarried.md) |  | [optional] 
**set_aside_resolved** | [**List[StudySchemaUploadSummarySetAsideResolvedInner]**](StudySchemaUploadSummarySetAsideResolvedInner.md) | For a parse: stored records whose set-aside keys (no earlier parse held them) this parse holds, re-ingested onto the new entities.  | [optional] 
**record** | [**StudySchemaUploadSummaryRecord**](StudySchemaUploadSummaryRecord.md) |  | [optional] 
**provenance** | [**Dict[str, PipelineRunProvenance]**](PipelineRunProvenance.md) | The stored run behind each part of the upload, keyed parse and record. | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary import StudySchemaUploadSummary

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummary from a JSON string
study_schema_upload_summary_instance = StudySchemaUploadSummary.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummary.to_json())

# convert the object into a dict
study_schema_upload_summary_dict = study_schema_upload_summary_instance.to_dict()
# create an instance of StudySchemaUploadSummary from a dict
study_schema_upload_summary_from_dict = StudySchemaUploadSummary.from_dict(study_schema_upload_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


