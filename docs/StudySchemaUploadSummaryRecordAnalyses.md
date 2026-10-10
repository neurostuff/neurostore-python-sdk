# StudySchemaUploadSummaryRecordAnalyses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolved** | **int** |  | [optional] 
**unresolved** | **List[str]** | Keys (or local_ids) that resolve to no analysis; stored as FAILURE rows. | [optional] 
**parked** | [**List[StudySchemaSetAside]**](StudySchemaSetAside.md) | Set-aside positional keys, held until a record names them by content. | [optional] 
**superseded** | [**List[StudySchemaUploadSummaryRecordAnalysesSupersededInner]**](StudySchemaUploadSummaryRecordAnalysesSupersededInner.md) | Keys that resolve to history because a revision since split, merged or dropped them. | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_record_analyses import StudySchemaUploadSummaryRecordAnalyses

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummaryRecordAnalyses from a JSON string
study_schema_upload_summary_record_analyses_instance = StudySchemaUploadSummaryRecordAnalyses.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummaryRecordAnalyses.to_json())

# convert the object into a dict
study_schema_upload_summary_record_analyses_dict = study_schema_upload_summary_record_analyses_instance.to_dict()
# create an instance of StudySchemaUploadSummaryRecordAnalyses from a dict
study_schema_upload_summary_record_analyses_from_dict = StudySchemaUploadSummaryRecordAnalyses.from_dict(study_schema_upload_summary_record_analyses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


