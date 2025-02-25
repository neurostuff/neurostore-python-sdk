# StudyRequestRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyses** | [**StudyRequestRelationshipsAnalyses**](StudyRequestRelationshipsAnalyses.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_request_relationships import StudyRequestRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of StudyRequestRelationships from a JSON string
study_request_relationships_instance = StudyRequestRelationships.from_json(json)
# print the JSON string representation of the object
print(StudyRequestRelationships.to_json())

# convert the object into a dict
study_request_relationships_dict = study_request_relationships_instance.to_dict()
# create an instance of StudyRequestRelationships from a dict
study_request_relationships_from_dict = StudyRequestRelationships.from_dict(study_request_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


