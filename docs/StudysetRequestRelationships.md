# StudysetRequestRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**studies** | [**StudysetRequestRelationshipsStudies**](StudysetRequestRelationshipsStudies.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.studyset_request_relationships import StudysetRequestRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetRequestRelationships from a JSON string
studyset_request_relationships_instance = StudysetRequestRelationships.from_json(json)
# print the JSON string representation of the object
print StudysetRequestRelationships.to_json()

# convert the object into a dict
studyset_request_relationships_dict = studyset_request_relationships_instance.to_dict()
# create an instance of StudysetRequestRelationships from a dict
studyset_request_relationships_form_dict = studyset_request_relationships.from_dict(studyset_request_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


