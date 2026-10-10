# PipelineRunProvenanceSchema

The study_schema schema the document follows (name, version).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_run_provenance_schema import PipelineRunProvenanceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRunProvenanceSchema from a JSON string
pipeline_run_provenance_schema_instance = PipelineRunProvenanceSchema.from_json(json)
# print the JSON string representation of the object
print(PipelineRunProvenanceSchema.to_json())

# convert the object into a dict
pipeline_run_provenance_schema_dict = pipeline_run_provenance_schema_instance.to_dict()
# create an instance of PipelineRunProvenanceSchema from a dict
pipeline_run_provenance_schema_from_dict = PipelineRunProvenanceSchema.from_dict(pipeline_run_provenance_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


