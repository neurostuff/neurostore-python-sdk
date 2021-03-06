# ImageReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | short UUID specifying the location of this resource | [readonly] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata about image such as software and version used and other relevant data about how the image was produced. | [optional] 
**url** | **str, none_type** | URL to image file. | [optional] 
**filename** | **str, none_type** | Name of the image file. | [optional] 
**space** | **str, none_type** | The template space the image is in (e.g., MNI  | [optional] 
**value_type** | **str, none_type** | The values the image represents. For example, T-statistic or Z-statistic, or Betas. | [optional] 
**add_date** | **datetime, none_type** | Date the image was added. | [optional] [readonly] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str, none_type** |  | [optional] [readonly] 
**user** | **str, none_type** | who owns the resource | [optional] [readonly] 
**public** | **bool** |  | [optional]  if omitted the server will use the default value of True
**analysis** | **str** |  | [optional] 
**entities** | [**[Entity]**](Entity.md) |  | [optional] 
**analysis_name** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


