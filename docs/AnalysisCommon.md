# AnalysisCommon

attributes common between request and return objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study** | **str** |  | [optional] 
**table_id** | **str** |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**order** | **int** |  | [optional] 
**metadata** | **object** |  | [optional] 
**role** | **str** | What the coordinates are for (study_schema CoordinateRole): &#x60;result&#x60;, &#x60;anchor&#x60;, &#x60;localization&#x60;, &#x60;reference&#x60; or &#x60;other&#x60;; an open vocabulary, so the source&#39;s own wording may appear. Only a result is released in a studyset. Null on an analysis from before roles, which is read as a result, except on a set the study_schema ingester wrote, which is unclassified. | [optional] 
**relabelled_by** | **str** | The parse_id of the reviewed revision whose relabel verdict set &#x60;role&#x60;; a later parse does not replace a relabelled role. Null while the role is the classifier&#39;s, whose name and version are in &#x60;metadata.role_source&#x60; (study_schema&#39;s &#x60;role_source&#x60;). | [optional] 
**outcome** | **str** | Whether anything survived the analysis&#39;s threshold (study_schema AnalysisOutcome), from the extraction record. The ingester sets it only on results. | [optional] 
**from_prior_study** | **bool** | The coordinates are quoted from an earlier study, not this one&#39;s. | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_common import AnalysisCommon

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCommon from a JSON string
analysis_common_instance = AnalysisCommon.from_json(json)
# print the JSON string representation of the object
print(AnalysisCommon.to_json())

# convert the object into a dict
analysis_common_dict = analysis_common_instance.to_dict()
# create an instance of AnalysisCommon from a dict
analysis_common_from_dict = AnalysisCommon.from_dict(analysis_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


