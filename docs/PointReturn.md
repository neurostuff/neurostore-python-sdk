# PointReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [readonly] 
**updated_at** | **str, none_type** |  | [readonly] 
**user** | **str, none_type** | who owns the resource | [readonly] 
**id** | **str** | short UUID specifying the location of this resource | 
**coordinates** | **[float]** | Location of the significant coordinate in three dimensional space. | [optional] 
**space** | **str, none_type** | Template space used to determine coordinate Examples include TAL or MNI. | [optional] 
**kind** | **str, none_type** | Method of how point was derived (e.g., center of mass) | [optional] 
**label_id** | **str, none_type** | If the point is associated with an image, this is the value the point takes in that image. | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional]  if omitted the server will use the default value of True
**image** | **str, none_type** |  | [optional] 
**value** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 
**entities** | [**[Entity]**](Entity.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


