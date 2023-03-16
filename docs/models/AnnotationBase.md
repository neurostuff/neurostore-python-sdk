# neurostore_sdk.model.annotation_base.AnnotationBase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | None, str,  | NoneClass, str,  | Descriptive name for the annotation. | [optional] 
**description** | None, str,  | NoneClass, str,  | Long form description of the annotation. | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation. | [optional] 
**[note_keys](#note_keys)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The keys (columns) in the annotation and the key&#x27;s respective data type (such as an integer or string). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation. | 

# note_keys

The keys (columns) in the annotation and the key's respective data type (such as an integer or string).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The keys (columns) in the annotation and the key&#x27;s respective data type (such as an integer or string). | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

