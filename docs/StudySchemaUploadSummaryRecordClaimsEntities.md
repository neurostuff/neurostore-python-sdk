# StudySchemaUploadSummaryRecordClaimsEntities

The record's entities that were created or matched to stored ones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**matched** | **int** |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_record_claims_entities import StudySchemaUploadSummaryRecordClaimsEntities

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummaryRecordClaimsEntities from a JSON string
study_schema_upload_summary_record_claims_entities_instance = StudySchemaUploadSummaryRecordClaimsEntities.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummaryRecordClaimsEntities.to_json())

# convert the object into a dict
study_schema_upload_summary_record_claims_entities_dict = study_schema_upload_summary_record_claims_entities_instance.to_dict()
# create an instance of StudySchemaUploadSummaryRecordClaimsEntities from a dict
study_schema_upload_summary_record_claims_entities_from_dict = StudySchemaUploadSummaryRecordClaimsEntities.from_dict(study_schema_upload_summary_record_claims_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


