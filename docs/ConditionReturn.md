# ConditionReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the condition being applied in the contrast, either psychological, pharmacological, or group based. | [optional] 
**description** | **str** | Long form description of how the condition is operationalized and/or specific meaning. | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 

## Example

```python
from neurostore_sdk.models.condition_return import ConditionReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionReturn from a JSON string
condition_return_instance = ConditionReturn.from_json(json)
# print the JSON string representation of the object
print(ConditionReturn.to_json())

# convert the object into a dict
condition_return_dict = condition_return_instance.to_dict()
# create an instance of ConditionReturn from a dict
condition_return_form_dict = condition_return.from_dict(condition_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


