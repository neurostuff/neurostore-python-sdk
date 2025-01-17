# PipelineConfigList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PipelineConfig]**](PipelineConfig.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline_config_list import PipelineConfigList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineConfigList from a JSON string
pipeline_config_list_instance = PipelineConfigList.from_json(json)
# print the JSON string representation of the object
print PipelineConfigList.to_json()

# convert the object into a dict
pipeline_config_list_dict = pipeline_config_list_instance.to_dict()
# create an instance of PipelineConfigList from a dict
pipeline_config_list_form_dict = pipeline_config_list.from_dict(pipeline_config_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


