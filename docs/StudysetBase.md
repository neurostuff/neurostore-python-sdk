# StudysetBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive and human readable name of the studyset. | [optional] 
**description** | **str** | A longform description of the studyset. | [optional] 
**publication** | **str** | The journal/source the studyset is connected to if the studyset was published. | [optional] 
**doi** | **str** | A DOI connected to the published studyset (may change to being automatically created so each studyset connected to a successful meta-analysis gets a DOI). | [optional] 
**pmid** | **str** | If the article connected to the studyset was published on PubMed, then link the ID here. | [optional] 

## Example

```python
from neurostore_sdk.models.studyset_base import StudysetBase

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetBase from a JSON string
studyset_base_instance = StudysetBase.from_json(json)
# print the JSON string representation of the object
print(StudysetBase.to_json())

# convert the object into a dict
studyset_base_dict = studyset_base_instance.to_dict()
# create an instance of StudysetBase from a dict
studyset_base_form_dict = studyset_base.from_dict(studyset_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


