# PipelineRunResultVote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**pipeline_run_result_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**vote** | **int** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_run_result_vote import PipelineRunResultVote

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRunResultVote from a JSON string
pipeline_run_result_vote_instance = PipelineRunResultVote.from_json(json)
# print the JSON string representation of the object
print(PipelineRunResultVote.to_json())

# convert the object into a dict
pipeline_run_result_vote_dict = pipeline_run_result_vote_instance.to_dict()
# create an instance of PipelineRunResultVote from a dict
pipeline_run_result_vote_from_dict = PipelineRunResultVote.from_dict(pipeline_run_result_vote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


