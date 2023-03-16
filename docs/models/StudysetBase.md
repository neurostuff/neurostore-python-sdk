# neurostore_sdk.model.studyset_base.StudysetBase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | None, str,  | NoneClass, str,  | Descriptive and human readable name of the studyset. | [optional] 
**description** | None, str,  | NoneClass, str,  | A longform description of the studyset. | [optional] 
**publication** | None, str,  | NoneClass, str,  | The journal/source the studyset is connected to if the studyset was published. | [optional] 
**doi** | None, str,  | NoneClass, str,  | A DOI connected to the published studyset (may change to being automatically created so each studyset connected to a successful meta-analysis gets a DOI). | [optional] 
**pmid** | None, str,  | NoneClass, str,  | If the article connected to the studyset was published on PubMed, then link the ID here. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

