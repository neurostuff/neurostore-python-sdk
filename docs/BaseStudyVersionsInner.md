# BaseStudyVersionsInner


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
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 
**source** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**source_updated_at** | **str** |  | [optional] [readonly] 
**analyses** | [**StudyReturnRelationshipsAnalyses**](StudyReturnRelationshipsAnalyses.md) |  | [optional] 
**studysets** | [**List[StudyReturnAllOfStudysets]**](StudyReturnAllOfStudysets.md) |  | [optional] 
**has_coordinates** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**base_study** | **str** |  | [optional] 
**pmcid** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.base_study_versions_inner import BaseStudyVersionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudyVersionsInner from a JSON string
base_study_versions_inner_instance = BaseStudyVersionsInner.from_json(json)
# print the JSON string representation of the object
print(BaseStudyVersionsInner.to_json())

# convert the object into a dict
base_study_versions_inner_dict = base_study_versions_inner_instance.to_dict()
# create an instance of BaseStudyVersionsInner from a dict
base_study_versions_inner_from_dict = BaseStudyVersionsInner.from_dict(base_study_versions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


