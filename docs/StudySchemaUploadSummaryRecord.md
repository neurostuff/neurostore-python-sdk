# StudySchemaUploadSummaryRecord

For a record, how its analyses and claims resolved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** |  | [optional] 
**analyses** | [**StudySchemaUploadSummaryRecordAnalyses**](StudySchemaUploadSummaryRecordAnalyses.md) |  | [optional] 
**condition_conflicts** | [**List[StudySchemaUploadSummaryRecordConditionConflictsInner]**](StudySchemaUploadSummaryRecordConditionConflictsInner.md) | Record analyses whose effect cells set no conditions (the analysis gets none) because the cells contradict each other. One entry per record entry, keyed by its key, or its local_id when it has none.  | [optional] 
**claims** | [**StudySchemaUploadSummaryRecordClaims**](StudySchemaUploadSummaryRecordClaims.md) |  | [optional] 
**carried** | [**StudySchemaCarried**](StudySchemaCarried.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_record import StudySchemaUploadSummaryRecord

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummaryRecord from a JSON string
study_schema_upload_summary_record_instance = StudySchemaUploadSummaryRecord.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummaryRecord.to_json())

# convert the object into a dict
study_schema_upload_summary_record_dict = study_schema_upload_summary_record_instance.to_dict()
# create an instance of StudySchemaUploadSummaryRecord from a dict
study_schema_upload_summary_record_from_dict = StudySchemaUploadSummaryRecord.from_dict(study_schema_upload_summary_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


