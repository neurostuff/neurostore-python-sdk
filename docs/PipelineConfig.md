# PipelineConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_config import PipelineConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineConfig from a JSON string
pipeline_config_instance = PipelineConfig.from_json(json)
# print the JSON string representation of the object
print(PipelineConfig.to_json())

# convert the object into a dict
pipeline_config_dict = pipeline_config_instance.to_dict()
# create an instance of PipelineConfig from a dict
pipeline_config_form_dict = pipeline_config.from_dict(pipeline_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


