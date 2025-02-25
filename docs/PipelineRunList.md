# PipelineRunList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PipelineRun]**](PipelineRun.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_run_list import PipelineRunList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRunList from a JSON string
pipeline_run_list_instance = PipelineRunList.from_json(json)
# print the JSON string representation of the object
print(PipelineRunList.to_json())

# convert the object into a dict
pipeline_run_list_dict = pipeline_run_list_instance.to_dict()
# create an instance of PipelineRunList from a dict
pipeline_run_list_from_dict = PipelineRunList.from_dict(pipeline_run_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


