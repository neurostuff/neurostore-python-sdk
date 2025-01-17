# PipelineRunResultList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PipelineRunResult]**](PipelineRunResult.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_run_result_list import PipelineRunResultList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRunResultList from a JSON string
pipeline_run_result_list_instance = PipelineRunResultList.from_json(json)
# print the JSON string representation of the object
print PipelineRunResultList.to_json()

# convert the object into a dict
pipeline_run_result_list_dict = pipeline_run_result_list_instance.to_dict()
# create an instance of PipelineRunResultList from a dict
pipeline_run_result_list_form_dict = pipeline_run_result_list.from_dict(pipeline_run_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


