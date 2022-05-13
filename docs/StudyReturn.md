# StudyReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doi** | **str, none_type** | Digital object identifier of the study. | [optional] 
**name** | **str, none_type** | Title of the study. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata associated with the study not covered by the other study attributes. | [optional] 
**description** | **str, none_type** | Long form description of the study, typically the abstract. | [optional] 
**publication** | **str, none_type** | The journal/place of publication for the study. | [optional] 
**pmid** | **str, none_type** | If the study was published on PubMed, place the PubMed ID here. | [optional] 
**authors** | **str, none_type** | The authors on the publication of this study. | [optional] 
**year** | **int, none_type** | The year this study was published. | [optional] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str, none_type** |  | [optional] [readonly] 
**user** | **str, none_type** | who owns the resource | [optional] [readonly] 
**public** | **bool** |  | [optional]  if omitted the server will use the default value of True
**source** | **str, none_type** |  | [optional] 
**source_id** | **str, none_type** |  | [optional] 
**source_updated_at** | **str, none_type** |  | [optional] 
**analyses** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


