# neurostore_sdk.model.image_base.ImageBase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[metadata](#metadata)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Metadata about image such as software and version used and other relevant data about how the image was produced. | [optional] 
**url** | None, str,  | NoneClass, str,  | URL to image file. | [optional] 
**filename** | None, str,  | NoneClass, str,  | Name of the image file. | [optional] 
**space** | None, str,  | NoneClass, str,  | The template space the image is in (e.g., MNI  | [optional] 
**value_type** | None, str,  | NoneClass, str,  | The values the image represents. For example, T-statistic or Z-statistic, or Betas. | [optional] 
**add_date** | None, str, datetime,  | NoneClass, str,  | Date the image was added. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

Metadata about image such as software and version used and other relevant data about how the image was produced.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Metadata about image such as software and version used and other relevant data about how the image was produced. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

