# StudysetReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | time the resource was created on the database | [readonly] 
**updated_at** | **str, none_type** |  | [readonly] 
**user** | **str, none_type** | who owns the resource | [readonly] 
**id** | **str** | short UUID specifying the location of this resource | 
**name** | **str, none_type** | Descriptive and human readable name of the studyset. | [optional] 
**description** | **str, none_type** | A longform description of the studyset. | [optional] 
**publication** | **str, none_type** | The journal/source the studyset is connected to if the studyset was published. | [optional] 
**doi** | **str, none_type** | A DOI connected to the published studyset (may change to being automatically created so each studyset connected to a successful meta-analysis gets a DOI). | [optional] 
**pmid** | **str, none_type** | If the article connected to the studyset was published on PubMed, then link the ID here. | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional]  if omitted the server will use the default value of True
**source** | **str, none_type** |  | [optional] 
**source_id** | **str, none_type** |  | [optional] 
**source_updated_at** | **str, none_type** |  | [optional] [readonly] 
**studies** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


