# StudySchemaUploadSummaryRecordClaims


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**matched** | **int** |  | [optional] 
**rejected_paths** | **List[str]** |  | [optional] 
**unkeyed_entities** | **List[str]** | Record entities with no key to identify them by. | [optional] 
**parked_entities** | [**List[StudySchemaSetAside]**](StudySchemaSetAside.md) | Set-aside entities: positional keys, or keys no stored parse holds (resolved later by a parse that holds them; see set_aside_resolved).  | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_upload_summary_record_claims import StudySchemaUploadSummaryRecordClaims

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaUploadSummaryRecordClaims from a JSON string
study_schema_upload_summary_record_claims_instance = StudySchemaUploadSummaryRecordClaims.from_json(json)
# print the JSON string representation of the object
print(StudySchemaUploadSummaryRecordClaims.to_json())

# convert the object into a dict
study_schema_upload_summary_record_claims_dict = study_schema_upload_summary_record_claims_instance.to_dict()
# create an instance of StudySchemaUploadSummaryRecordClaims from a dict
study_schema_upload_summary_record_claims_from_dict = StudySchemaUploadSummaryRecordClaims.from_dict(study_schema_upload_summary_record_claims_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


