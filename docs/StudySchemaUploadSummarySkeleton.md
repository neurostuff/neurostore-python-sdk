# StudySchemaUploadSummarySkeleton

For a parse, what it did to the study's analyses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 
**superseded** | **int** | Analyses moved to the history study because this version dropped their key. | [optional] 
**not_uploaded** | **List[str]** | Keys of analyses whose role is not uploaded. | [optional] 
**aliased** | [**List[StudySchemaUploadSummarySkeletonAliasedInner]**](StudySchemaUploadSummarySkeletonAliasedInner.md) | Analyses an original re-parse reads from other cells (same table and name, new key), one pair each; their entities keep the old hash as an alias.  | [optional] 

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


