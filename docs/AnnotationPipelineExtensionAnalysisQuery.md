# AnnotationPipelineExtensionAnalysisQuery

Run an analysis query over the annotation's studyset and write its result into the notes: `column` (boolean) is true for each analysis the query selects and false for every other, and each of `feature_columns` (string) carries that analysis's feature, or null where its record says nothing. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**AnalysisQuery**](AnalysisQuery.md) |  | 
**column** | **str** |  | [optional] [default to 'included']
**feature_columns** | **List[str]** |  | [optional] 

## Example

```python
from neurostore_sdk.models.annotation_pipeline_extension_analysis_query import AnnotationPipelineExtensionAnalysisQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationPipelineExtensionAnalysisQuery from a JSON string
annotation_pipeline_extension_analysis_query_instance = AnnotationPipelineExtensionAnalysisQuery.from_json(json)
# print the JSON string representation of the object
print(AnnotationPipelineExtensionAnalysisQuery.to_json())

# convert the object into a dict
annotation_pipeline_extension_analysis_query_dict = annotation_pipeline_extension_analysis_query_instance.to_dict()
# create an instance of AnnotationPipelineExtensionAnalysisQuery from a dict
annotation_pipeline_extension_analysis_query_from_dict = AnnotationPipelineExtensionAnalysisQuery.from_dict(annotation_pipeline_extension_analysis_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


