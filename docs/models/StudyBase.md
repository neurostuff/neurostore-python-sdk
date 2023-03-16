# neurostore_sdk.model.study_base.StudyBase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**doi** | None, str,  | NoneClass, str,  | Digital object identifier of the study. | [optional] 
**name** | None, str,  | NoneClass, str,  | Title of the study. | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Metadata associated with the study not covered by the other study attributes. | [optional] 
**description** | None, str,  | NoneClass, str,  | Long form description of the study, typically the abstract. | [optional] 
**publication** | None, str,  | NoneClass, str,  | The journal/place of publication for the study. | [optional] 
**pmid** | None, str,  | NoneClass, str,  | If the study was published on PubMed, place the PubMed ID here. | [optional] 
**authors** | None, str,  | NoneClass, str,  | The authors on the publication of this study. | [optional] 
**year** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The year this study was published. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

Metadata associated with the study not covered by the other study attributes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Metadata associated with the study not covered by the other study attributes. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

