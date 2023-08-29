# StudysetReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive and human readable name of the studyset. | [optional] 
**description** | **str** | A longform description of the studyset. | [optional] 
**publication** | **str** | The journal/source the studyset is connected to if the studyset was published. | [optional] 
**doi** | **str** | A DOI connected to the published studyset (may change to being automatically created so each studyset connected to a successful meta-analysis gets a DOI). | [optional] 
**pmid** | **str** | If the article connected to the studyset was published on PubMed, then link the ID here. | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when was the resource last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 
**source** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_updated_at** | **str** |  | [optional] [readonly] 
**studies** | [**StudysetReturnRelationshipsStudies**](StudysetReturnRelationshipsStudies.md) |  | [optional] 
**level** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.studyset_return import StudysetReturn

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetReturn from a JSON string
studyset_return_instance = StudysetReturn.from_json(json)
# print the JSON string representation of the object
print StudysetReturn.to_json()

# convert the object into a dict
studyset_return_dict = studyset_return_instance.to_dict()
# create an instance of StudysetReturn from a dict
studyset_return_form_dict = studyset_return.from_dict(studyset_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


