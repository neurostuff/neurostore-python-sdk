# StudySchemaUploadSummaryRecordConditionConflictsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**cells** | [**List[StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner]**](StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_record_condition_conflicts_inner import StudySchemaUploadSummaryRecordConditionConflictsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummaryRecordConditionConflictsInner from a JSON string
study_schema_upload_summary_record_condition_conflicts_inner_instance = StudySchemaUploadSummaryRecordConditionConflictsInner.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummaryRecordConditionConflictsInner.to_json())

# convert the object into a dict
study_schema_upload_summary_record_condition_conflicts_inner_dict = study_schema_upload_summary_record_condition_conflicts_inner_instance.to_dict()
# create an instance of StudySchemaUploadSummaryRecordConditionConflictsInner from a dict
study_schema_upload_summary_record_condition_conflicts_inner_from_dict = StudySchemaUploadSummaryRecordConditionConflictsInner.from_dict(study_schema_upload_summary_record_condition_conflicts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


