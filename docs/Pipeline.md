# Pipeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**study_dependent** | **bool** |  | [optional] 
**ace_compatible** | **bool** |  | [optional] 
**pubget_compatible** | **bool** |  | [optional] 
**derived_from** | **str** |  | [optional] 

## Example

```python
from neurostore_sdk.models.pipeline import Pipeline

# TODO update the JSON string below
json = "{}"
# create an instance of Pipeline from a JSON string
pipeline_instance = Pipeline.from_json(json)
# print the JSON string representation of the object
print(Pipeline.to_json())

# convert the object into a dict
pipeline_dict = pipeline_instance.to_dict()
# create an instance of Pipeline from a dict
pipeline_form_dict = pipeline.from_dict(pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


