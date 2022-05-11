# PointReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **[float]** | location of the point | [optional] 
**space** | **str, none_type** | template space used to determine coordinate (TAL or MNI or UNKNOWN) | [optional] 
**kind** | **str, none_type** | method of how point was derived (e.g., center of mass) | [optional] 
**label_id** | **str, none_type** |  | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str, none_type** |  | [optional] [readonly] 
**user** | **str, none_type** | who owns the resource | [optional] [readonly] 
**public** | **bool** |  | [optional]  if omitted the server will use the default value of True
**image** | **str** |  | [optional] 
**value** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 
**entities** | [**[Entity]**](Entity.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


