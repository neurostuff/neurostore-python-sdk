# StudySchemaRun

One run behind a record, as the pipeline's runs table first stored it. A run is one combination of model and inputs; reruns of it carry the same run_id and fields. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | Required. Names one run; a run_id stored with other fields is refused (RUN_CONFLICT). | [optional] 
**kind** | **str** | model (a model made the output) or migration (an older output carried over). | [optional] 
**stage** | **str** | Required. record, evidence or normalize. | [optional] 
**source** | **str** | Required. The record source the run made or read. | [optional] 
**pipeline** | **str** | The pipeline that ran the stage. | [optional] 
**version** | **str** | The pipeline&#39;s version. | [optional] 
**model** | **str** |  | [optional] 
**adapter** | **str** | repo@revision of the adapter the model ran with. | [optional] 
**prompt_version** | **str** |  | [optional] 
**schema_version** | **str** |  | [optional] 
**code_commit** | **str** |  | [optional] 
**machine** | **str** |  | [optional] 
**fit** | **str** | For a normalize run, the fingerprint of the fitted normalization model (the task and contrast clustering) it assigned with. A refit is a new run.  | [optional] 
**created_at** | **str** | Required. When the run was made, ISO 8601. | [optional] 

## Example

```python
from neurostore_sdk.models.study_schema_run import StudySchemaRun

# TODO update the JSON string below
json = "{}"
# create an instance of StudySchemaRun from a JSON string
study_schema_run_instance = StudySchemaRun.from_json(json)
# print the JSON string representation of the object
print(StudySchemaRun.to_json())

# convert the object into a dict
study_schema_run_dict = study_schema_run_instance.to_dict()
# create an instance of StudySchemaRun from a dict
study_schema_run_from_dict = StudySchemaRun.from_dict(study_schema_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


