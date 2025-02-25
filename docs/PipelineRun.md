# PipelineRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**finished_at** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_run import PipelineRun

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRun from a JSON string
pipeline_run_instance = PipelineRun.from_json(json)
# print the JSON string representation of the object
print(PipelineRun.to_json())

# convert the object into a dict
pipeline_run_dict = pipeline_run_instance.to_dict()
# create an instance of PipelineRun from a dict
pipeline_run_form_dict = pipeline_run.from_dict(pipeline_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


