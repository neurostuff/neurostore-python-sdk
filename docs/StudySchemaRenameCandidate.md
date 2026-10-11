# StudySchemaRenameCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** |  | [optional] 
**var_from** | **str** | The old name or key. | [optional] 
**to** | **str** | The new name or key. | [optional] 
**entity_id** | **str** | The old entity. | [optional] 
**candidate_id** | **str** | The entity for the new name. | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_rename_candidate import StudySchemaRenameCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaRenameCandidate from a JSON string
study_schema_rename_candidate_instance = StudySchemaRenameCandidate.from_json(json)
# print the JSON string representation of the object
print(StudySchemaRenameCandidate.to_json())

# convert the object into a dict
study_schema_rename_candidate_dict = study_schema_rename_candidate_instance.to_dict()
# create an instance of StudySchemaRenameCandidate from a dict
study_schema_rename_candidate_from_dict = StudySchemaRenameCandidate.from_dict(study_schema_rename_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


