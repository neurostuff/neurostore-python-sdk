# StudysetReturnRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**studies** | [**StudysetReturnRelationshipsStudies**](StudysetReturnRelationshipsStudies.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.studyset_return_relationships import StudysetReturnRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetReturnRelationships from a JSON string
studyset_return_relationships_instance = StudysetReturnRelationships.from_json(json)
# print the JSON string representation of the object
print(StudysetReturnRelationships.to_json())

# convert the object into a dict
studyset_return_relationships_dict = studyset_return_relationships_instance.to_dict()
# create an instance of StudysetReturnRelationships from a dict
studyset_return_relationships_from_dict = StudysetReturnRelationships.from_dict(studyset_return_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


