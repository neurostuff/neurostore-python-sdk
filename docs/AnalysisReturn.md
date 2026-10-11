# AnalysisReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name of the contrast being performed. | [optional] 
**description** | **str** | A long form description of how the contrast was performed | [optional] 
**weights** | **List[float]** | Weight applied to each condition, must be the same length as the conditions attribute. | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 
**study** | **str** |  | [optional] 
**images** | [**AnalysisReturnRelationshipsImages**](AnalysisReturnRelationshipsImages.md) |  | [optional] 
**points** | [**AnalysisReturnRelationshipsPoints**](AnalysisReturnRelationshipsPoints.md) |  | [optional] 
**conditions** | [**AnalysisReturnRelationshipsConditions**](AnalysisReturnRelationshipsConditions.md) |  | [optional] 
**table_id** | **str** |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**order** | **int** |  | [optional] 
**metadata** | **object** |  | [optional] 
**role** | **str** | What the coordinates are for (study_schema CoordinateRole): &#x60;result&#x60;, &#x60;anchor&#x60;, &#x60;localization&#x60;, &#x60;reference&#x60; or &#x60;other&#x60;; an open vocabulary, so the source&#39;s own wording may appear. Only a result is released in a studyset. Null on an analysis from before roles, which is read as a result, except on a set the study_schema ingester wrote, which is unclassified. | [optional] 
**relabelled_by** | **str** | The parse_id of the reviewed revision whose relabel verdict set &#x60;role&#x60;; a later parse does not replace a relabelled role. Null while the role is the classifier&#39;s, whose name and version are in &#x60;metadata.role_source&#x60; (study_schema&#39;s &#x60;role_source&#x60;). | [optional] 
**outcome** | **str** | Whether anything survived the analysis&#39;s threshold (study_schema AnalysisOutcome), from the extraction record. The ingester sets it only on results. | [optional] 
**from_prior_study** | **bool** | The coordinates are quoted from an earlier study, not this one&#39;s. | [optional] 
**source_id** | **str** | ID of the analysis this one was cloned from, if any. | [optional] [readonly] 
**point_count** | **int** | Number of point coordinates linked to this analysis. | [optional] 
**image_count** | **int** | Number of images linked to this analysis. | [optional] 
**has_coordinates** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**has_z_maps** | **bool** |  | [optional] 
**has_t_maps** | **bool** |  | [optional] 
**has_beta_and_variance_maps** | **bool** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_return import AnalysisReturn

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisReturn from a JSON string
analysis_return_instance = AnalysisReturn.from_json(json)
# print the JSON string representation of the object
print(AnalysisReturn.to_json())

# convert the object into a dict
analysis_return_dict = analysis_return_instance.to_dict()
# create an instance of AnalysisReturn from a dict
analysis_return_from_dict = AnalysisReturn.from_dict(analysis_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


