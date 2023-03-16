# neurostore_sdk.model.note_collection_return.NoteCollectionReturn

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NoteCollectionBase](NoteCollectionBase.md) | [**NoteCollectionBase**](NoteCollectionBase.md) | [**NoteCollectionBase**](NoteCollectionBase.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**analysis** | str,  | str,  |  | [optional] 
**analysis_name** | None, str,  | NoneClass, str,  |  | [optional] 
**study** | str,  | str,  |  | [optional] 
**study_name** | None, str,  | NoneClass, str,  |  | [optional] 
**annotation** | str,  | str,  |  | [optional] 
**study_year** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**publication** | None, str,  | NoneClass, str,  |  | [optional] 
**authors** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

