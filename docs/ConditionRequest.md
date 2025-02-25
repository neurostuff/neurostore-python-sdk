# ConditionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the condition being applied in the contrast, either psychological, pharmacological, or group based. | [optional] 
**description** | **str** | Long form description of how the condition is operationalized and/or specific meaning. | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]

## Example

```python
from neurostore_sdk.models.condition_request import ConditionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionRequest from a JSON string
condition_request_instance = ConditionRequest.from_json(json)
# print the JSON string representation of the object
print(ConditionRequest.to_json())

# convert the object into a dict
condition_request_dict = condition_request_instance.to_dict()
# create an instance of ConditionRequest from a dict
condition_request_from_dict = ConditionRequest.from_dict(condition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


