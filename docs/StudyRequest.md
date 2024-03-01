# StudyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doi** | **str** | Digital object identifier of the study. | [optional] 
**name** | **str** | Title of the study. | [optional] 
**metadata** | **object** | Metadata associated with the study not covered by the other study attributes. | [optional] 
**description** | **str** | Long form description of the study, typically the abstract. | [optional] 
**publication** | **str** | The journal/place of publication for the study. | [optional] 
**pmid** | **str** | If the study was published on PubMed, place the PubMed ID here. | [optional] 
**authors** | **str** | The authors on the publication of this study. | [optional] 
**year** | **int** | The year this study was published. | [optional] 
**analyses** | [**StudyRequestRelationshipsAnalyses**](StudyRequestRelationshipsAnalyses.md) |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**pmcid** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.study_request import StudyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StudyRequest from a JSON string
study_request_instance = StudyRequest.from_json(json)
# print the JSON string representation of the object
print StudyRequest.to_json()

# convert the object into a dict
study_request_dict = study_request_instance.to_dict()
# create an instance of StudyRequest from a dict
study_request_form_dict = study_request.from_dict(study_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


