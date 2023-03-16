# neurostore_sdk.model.point_base.PointBase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[coordinates](#coordinates)** | list, tuple,  | tuple,  | Location of the significant coordinate in three dimensional space. | [optional] 
**space** | None, str,  | NoneClass, str,  | Template space used to determine coordinate Examples include TAL or MNI. | [optional] 
**kind** | None, str,  | NoneClass, str,  | Method of how point was derived (e.g., center of mass) | [optional] 
**label_id** | None, str,  | NoneClass, str,  | If the point is associated with an image, this is the value the point takes in that image. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# coordinates

Location of the significant coordinate in three dimensional space.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Location of the significant coordinate in three dimensional space. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 32 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

