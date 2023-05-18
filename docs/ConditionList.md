# ConditionList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ConditionReturn]**](ConditionReturn.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.condition_list import ConditionList

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionList from a JSON string
condition_list_instance = ConditionList.from_json(json)
# print the JSON string representation of the object
print ConditionList.to_json()

# convert the object into a dict
condition_list_dict = condition_list_instance.to_dict()
# create an instance of ConditionList from a dict
condition_list_form_dict = condition_list.from_dict(condition_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


