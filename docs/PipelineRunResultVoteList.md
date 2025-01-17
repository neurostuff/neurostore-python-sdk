# PipelineRunResultVoteList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PipelineRunResultVote]**](PipelineRunResultVote.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_run_result_vote_list import PipelineRunResultVoteList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRunResultVoteList from a JSON string
pipeline_run_result_vote_list_instance = PipelineRunResultVoteList.from_json(json)
# print the JSON string representation of the object
print PipelineRunResultVoteList.to_json()

# convert the object into a dict
pipeline_run_result_vote_list_dict = pipeline_run_result_vote_list_instance.to_dict()
# create an instance of PipelineRunResultVoteList from a dict
pipeline_run_result_vote_list_form_dict = pipeline_run_result_vote_list.from_dict(pipeline_run_result_vote_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


