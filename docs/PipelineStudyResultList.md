# PipelineStudyResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PipelineStudyResult]**](PipelineStudyResult.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_study_result_list import PipelineStudyResultList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineStudyResultList from a JSON string
pipeline_study_result_list_instance = PipelineStudyResultList.from_json(json)
# print the JSON string representation of the object
print(PipelineStudyResultList.to_json())

# convert the object into a dict
pipeline_study_result_list_dict = pipeline_study_result_list_instance.to_dict()
# create an instance of PipelineStudyResultList from a dict
pipeline_study_result_list_from_dict = PipelineStudyResultList.from_dict(pipeline_study_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


