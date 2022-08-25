# Annotation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Descriptive name for the annotation. | [optional] 
**description** | **str, none_type** | Long form description of the annotation. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation. | [optional] 
**note_keys** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The keys (columns) in the annotation and the key&#39;s respective type. | [optional] 
**studyset** | **bool, date, datetime, dict, float, int, list, str, none_type** | The studyset the annotation is associated with. Each annotation is associated with one and only one studyset, but a studyset can have multiple annotations. The representation can either be a studyset object or a string indicating the location to find the studyset object. | [optional] 
**notes** | [**[NoteCollection]**](NoteCollection.md) | The collection of notes for each analysis within the studyset. Each analysis will have all note_keys with the appropriately typed values. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


