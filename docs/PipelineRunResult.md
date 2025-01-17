# PipelineRunResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**pipeline_run_id** | **str** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_run_result import PipelineRunResult

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRunResult from a JSON string
pipeline_run_result_instance = PipelineRunResult.from_json(json)
# print the JSON string representation of the object
print PipelineRunResult.to_json()

# convert the object into a dict
pipeline_run_result_dict = pipeline_run_result_instance.to_dict()
# create an instance of PipelineRunResult from a dict
pipeline_run_result_form_dict = pipeline_run_result.from_dict(pipeline_run_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


