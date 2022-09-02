# AnalysisRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | A name of the contrast being performed. | [optional] 
**description** | **str, none_type** | A long form description of how the contrast was performed | [optional] 
**weights** | **[float]** | Weight applied to each condition, must be the same length as the conditions attribute. | [optional] 
**study** | **str** |  | [optional] 
**images** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**points** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**conditions** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


