# StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** |  | [optional] 
**level** | **str** | The cell&#39;s level, or its label when it has no level. | [optional] 
**reason** | **str** | both_directions: a level is given both positive and negative; one conflict per level, even when it appears under two labels. shared_name: two cells would name the same condition.  | [optional] 
**name** | **str** | The condition name the cells share. Only for shared_name. | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_record_condition_conflicts_inner_cells_inner import StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner from a JSON string
study_schema_upload_summary_record_condition_conflicts_inner_cells_inner_instance = StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner.to_json())

# convert the object into a dict
study_schema_upload_summary_record_condition_conflicts_inner_cells_inner_dict = study_schema_upload_summary_record_condition_conflicts_inner_cells_inner_instance.to_dict()
# create an instance of StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner from a dict
study_schema_upload_summary_record_condition_conflicts_inner_cells_inner_from_dict = StudySchemaUploadSummaryRecordConditionConflictsInnerCellsInner.from_dict(study_schema_upload_summary_record_condition_conflicts_inner_cells_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


