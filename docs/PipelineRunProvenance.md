# PipelineRunProvenance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_id** | **str** | The pipeline-study-result that stores the document. | [optional] 
**config_id** | **str** |  | [optional] 
**run_id** | **str** | The caller&#39;s run id the result was uploaded with. | [optional] 
**pipeline** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**commit** | **str** |  | [optional] 
**var_schema** | [**PipelineRunProvenanceSchema**](PipelineRunProvenanceSchema.md) |  | [optional] 
**parse_version** | **Dict[str, object]** | The parse&#39;s producer (name, version, stage, model, prompt_version). | [optional] 
**date_executed** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_run_provenance import PipelineRunProvenance

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRunProvenance from a JSON string
pipeline_run_provenance_instance = PipelineRunProvenance.from_json(json)
# print the JSON string representation of the object
print(PipelineRunProvenance.to_json())

# convert the object into a dict
pipeline_run_provenance_dict = pipeline_run_provenance_instance.to_dict()
# create an instance of PipelineRunProvenance from a dict
pipeline_run_provenance_from_dict = PipelineRunProvenance.from_dict(pipeline_run_provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


