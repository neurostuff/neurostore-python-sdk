# StudySchemaUploadSummaryRecordClaims


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**matched** | **int** |  | [optional] 
**rejected_paths** | **List[str]** |  | [optional] 
**entities** | [**StudySchemaUploadSummaryRecordClaimsEntities**](StudySchemaUploadSummaryRecordClaimsEntities.md) |  | [optional] 
**unlocated** | **List[str]** | Paths of analysis or coordinate-set items that name no content key; they are not stored as entities. | [optional] 
**unidentified** | **List[str]** | Paths of entity lists that are not lists, and of their items that are not objects; not stored as entities. | [optional] 
**duplicates** | **List[str]** | Paths of items whose hash an earlier item of the record already has (two items naming one content key); not stored. | [optional] 
**rename_candidates** | [**List[StudySchemaRenameCandidate]**](StudySchemaRenameCandidate.md) | Entities the record names differently from a stored sibling of the same class and parent, each the only unmatched one there. They are linked as renamed_by_extractor candidates; claims stay on the old entity until a curator links them. Analyses and coordinate sets are never candidates: a new name is a new key.  | [optional] 
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


