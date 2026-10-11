# StudySchemaUploadSummarySkeletonOrphanedClaimsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The superseded analysis&#39;s key. | [optional] 
**var_class** | **str** | The entity class. | [optional] 
**entity_id** | **str** |  | [optional] 
**claims** | **int** | How many claims the entity holds. | [optional] 
**reason** | **str** | Why the claims stayed; free text. | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_skeleton_orphaned_claims_inner import StudySchemaUploadSummarySkeletonOrphanedClaimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummarySkeletonOrphanedClaimsInner from a JSON string
study_schema_upload_summary_skeleton_orphaned_claims_inner_instance = StudySchemaUploadSummarySkeletonOrphanedClaimsInner.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummarySkeletonOrphanedClaimsInner.to_json())

# convert the object into a dict
study_schema_upload_summary_skeleton_orphaned_claims_inner_dict = study_schema_upload_summary_skeleton_orphaned_claims_inner_instance.to_dict()
# create an instance of StudySchemaUploadSummarySkeletonOrphanedClaimsInner from a dict
study_schema_upload_summary_skeleton_orphaned_claims_inner_from_dict = StudySchemaUploadSummarySkeletonOrphanedClaimsInner.from_dict(study_schema_upload_summary_skeleton_orphaned_claims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


