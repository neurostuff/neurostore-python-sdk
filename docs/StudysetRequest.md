# StudysetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive and human readable name of the studyset. | [optional] 
**description** | **str** | A longform description of the studyset. | [optional] 
**publication** | **str** | The journal/source the studyset is connected to if the studyset was published. | [optional] 
**doi** | **str** | A DOI connected to the published studyset (may change to being automatically created so each studyset connected to a successful meta-analysis gets a DOI). | [optional] 
**pmid** | **str** | If the article connected to the studyset was published on PubMed, then link the ID here. | [optional] 
**studies** | **List[object]** |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**level** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.studyset_request import StudysetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StudysetRequest from a JSON string
studyset_request_instance = StudysetRequest.from_json(json)
# print the JSON string representation of the object
print(StudysetRequest.to_json())

# convert the object into a dict
studyset_request_dict = studyset_request_instance.to_dict()
# create an instance of StudysetRequest from a dict
studyset_request_form_dict = studyset_request.from_dict(studyset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


