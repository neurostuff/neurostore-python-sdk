# ReviewSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**base_study_id** | **str** |  | 
**label** | **str** |  | 
**origin** | **str** | pipeline_run when the source names a pipeline config and a run, else upload. | 
**created_at** | **datetime** |  | 
**total** | **int** | Targets a reviewer can judge in the source&#39;s record, its extracted values and its coordinate parse&#39;s analyses. | 
**reviews** | [**List[ReviewProgress]**](ReviewProgress.md) |  | 
**assignees** | [**List[ReviewAssignee]**](ReviewAssignee.md) | The users the paper (base study) is assigned to. | 

## Example

```python
from neurostore_sdk.models.review_source import ReviewSource

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewSource from a JSON string
review_source_instance = ReviewSource.from_json(json)
# print the JSON string representation of the object
print(ReviewSource.to_json())

# convert the object into a dict
review_source_dict = review_source_instance.to_dict()
# create an instance of ReviewSource from a dict
review_source_from_dict = ReviewSource.from_dict(review_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


