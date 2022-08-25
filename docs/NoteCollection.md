# NoteCollection

The storage object for all notes within an annotation for a single analysis.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The note will contain all note_keys as keys and have a value of either null or the value type specified in note_keys. | [optional] 
**analysis** | **bool, date, datetime, dict, float, int, list, str, none_type** | The analysis the note collection is associated with. Either represented as an analysis object or a string pointing to the location of the analysis object. | [optional] 
**annotation** | **bool, date, datetime, dict, float, int, list, str, none_type** | The annotation this collection of notes is associated with. Either represented as an annotation object or a string pointing to the location of the annotation object. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


