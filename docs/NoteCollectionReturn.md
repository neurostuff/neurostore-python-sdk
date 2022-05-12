# NoteCollectionReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The note will contain all note_keys as keys and have a value of either null or the value type specified in note_keys. | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str, none_type** |  | [optional] [readonly] 
**user** | **str, none_type** | who owns the resource | [optional] [readonly] 
**public** | **bool** |  | [optional]  if omitted the server will use the default value of True
**analysis** | **str** |  | [optional] 
**analysis_name** | **str** |  | [optional] 
**study** | **str** |  | [optional] 
**study_name** | **str** |  | [optional] 
**annotation** | **str** |  | [optional] 
**study_year** | **str** |  | [optional] 
**publication** | **str** |  | [optional] 
**authors** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


