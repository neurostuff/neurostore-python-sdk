# ConditionReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [readonly] 
**updated_at** | **str, none_type** |  | [readonly] 
**user** | **str, none_type** | who owns the resource | [readonly] 
**id** | **str** | short UUID specifying the location of this resource | 
**name** | **str, none_type** | Name of the condition being applied in the contrast, either psychological, pharmacological, or group based. | [optional] 
**description** | **str, none_type** | Long form description of how the condition is operationalized and/or specific meaning. | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


