# StudySchemaUploadSummarySkeleton

For a parse, what it did to the study's analyses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 
**superseded** | **int** | Analyses moved to the history study because this version dropped their key. | [optional] 
**omitted_analyses** | **int** | How many text or figure analyses the parse lists as read and left out. Their reasons are kept in the study&#39;s metadata, not returned here.  | [optional] 
**aliased** | [**List[StudySchemaUploadSummarySkeletonAliasedInner]**](StudySchemaUploadSummarySkeletonAliasedInner.md) | Analyses an original re-parse reads from other cells (same table and name, new key), one pair each; their entities keep the old hash as an alias.  | [optional] 
**alias_conflicts** | [**List[StudySchemaUploadSummarySkeletonAliasConflictsInner]**](StudySchemaUploadSummarySkeletonAliasConflictsInner.md) | Re-read analyses whose new hash already belongs to another entity; nothing is re-hashed for that entity class and its claims stay where they are. Present for an original parse, absent for a revision.  | [optional] 
**rename_candidates** | [**List[StudySchemaRenameCandidate]**](StudySchemaRenameCandidate.md) | Analyses read from the same place under a new name. Each old entity is linked to a candidate entity for the new name as renamed_by_extractor; no claims move. Present for an original parse, absent for a revision.  | [optional] 
**orphaned_claims** | [**List[StudySchemaUploadSummarySkeletonOrphanedClaimsInner]**](StudySchemaUploadSummarySkeletonOrphanedClaimsInner.md) | Entities that hold claims and stayed on a superseded (history) analysis: not re-hashed onto a successor, not linked as a rename candidate, and not copied by a split or merge verdict. Always present; empty when none.  | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_skeleton import StudySchemaUploadSummarySkeleton

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummarySkeleton from a JSON string
study_schema_upload_summary_skeleton_instance = StudySchemaUploadSummarySkeleton.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummarySkeleton.to_json())

# convert the object into a dict
study_schema_upload_summary_skeleton_dict = study_schema_upload_summary_skeleton_instance.to_dict()
# create an instance of StudySchemaUploadSummarySkeleton from a dict
study_schema_upload_summary_skeleton_from_dict = StudySchemaUploadSummarySkeleton.from_dict(study_schema_upload_summary_skeleton_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


