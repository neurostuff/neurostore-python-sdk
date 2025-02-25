# StudyBase


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

## Example

```python
from neurostore_sdk.models.study_base import StudyBase

# TODO update the JSON string below
json = "{}"
# create an instance of StudyBase from a JSON string
study_base_instance = StudyBase.from_json(json)
# print the JSON string representation of the object
print(StudyBase.to_json())

# convert the object into a dict
study_base_dict = study_base_instance.to_dict()
# create an instance of StudyBase from a dict
study_base_from_dict = StudyBase.from_dict(study_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


