# StudySchemaUploadSummarySkeletonAliasConflictsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**holder_id** | **str** | The entity that already holds the new hash. | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_skeleton_alias_conflicts_inner import StudySchemaUploadSummarySkeletonAliasConflictsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummarySkeletonAliasConflictsInner from a JSON string
study_schema_upload_summary_skeleton_alias_conflicts_inner_instance = StudySchemaUploadSummarySkeletonAliasConflictsInner.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummarySkeletonAliasConflictsInner.to_json())

# convert the object into a dict
study_schema_upload_summary_skeleton_alias_conflicts_inner_dict = study_schema_upload_summary_skeleton_alias_conflicts_inner_instance.to_dict()
# create an instance of StudySchemaUploadSummarySkeletonAliasConflictsInner from a dict
study_schema_upload_summary_skeleton_alias_conflicts_inner_from_dict = StudySchemaUploadSummarySkeletonAliasConflictsInner.from_dict(study_schema_upload_summary_skeleton_alias_conflicts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


