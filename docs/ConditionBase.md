# ConditionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the condition being applied in the contrast, either psychological, pharmacological, or group based. | [optional] 
**description** | **str** | Long form description of how the condition is operationalized and/or specific meaning. | [optional] 

## Example

```python
from neurostore_sdk.models.condition_base import ConditionBase

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionBase from a JSON string
condition_base_instance = ConditionBase.from_json(json)
# print the JSON string representation of the object
print(ConditionBase.to_json())

# convert the object into a dict
condition_base_dict = condition_base_instance.to_dict()
# create an instance of ConditionBase from a dict
condition_base_from_dict = ConditionBase.from_dict(condition_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


