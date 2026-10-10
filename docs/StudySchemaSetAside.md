# StudySchemaSetAside


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | Class[key] for an entity, or absent for an analysis row. | [optional] 
**key** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_set_aside import StudySchemaSetAside

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaSetAside from a JSON string
study_schema_set_aside_instance = StudySchemaSetAside.from_json(json)
# print the JSON string representation of the object
print(StudySchemaSetAside.to_json())

# convert the object into a dict
study_schema_set_aside_dict = study_schema_set_aside_instance.to_dict()
# create an instance of StudySchemaSetAside from a dict
study_schema_set_aside_from_dict = StudySchemaSetAside.from_dict(study_schema_set_aside_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


