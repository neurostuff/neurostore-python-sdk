# StudySchemaUploadSummarySkeleton

For a parse, what it did to the study's analyses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 
**superseded** | **int** | Analyses moved to the history study because this version dropped their key. | [optional] 
**omitted_analyses** | **int** | How many text or figure analyses the parse lists as read and left out. Their reasons are kept in the study&#39;s metadata, not returned here.  | [optional] 
**orphaned_claims** | [**List[StudySchemaUploadSummarySkeletonOrphanedClaimsInner]**](StudySchemaUploadSummarySkeletonOrphanedClaimsInner.md) | Entities that hold claims and stayed on a superseded (history) analysis, not copied by a split or merge verdict. A changed name, space or point gives a new key, so the new analysis starts with no claims and the old one&#39;s are reported here. Always present; empty when none.  | [optional] 

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


