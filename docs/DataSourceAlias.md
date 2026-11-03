# DataSourceAlias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**alias** | **str** |  | 
**tier** | **str** | What a match on the alias needs: &#x60;name&#x60;, a full name matched case-insensitively; &#x60;safe&#x60;, an acronym that stands alone; &#x60;context&#x60;, an acronym needing a dataset or imaging word nearby; &#x60;defined&#x60;, an acronym needing one of the data source&#39;s names in the same paper; &#x60;qualified&#x60;, a common word needing a qualifier such as \&quot;dataset\&quot; or an accession. | 

## Example

```python
from neurostore_sdk.models.data_source_alias import DataSourceAlias

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceAlias from a JSON string
data_source_alias_instance = DataSourceAlias.from_json(json)
# print the JSON string representation of the object
print(DataSourceAlias.to_json())

# convert the object into a dict
data_source_alias_dict = data_source_alias_instance.to_dict()
# create an instance of DataSourceAlias from a dict
data_source_alias_from_dict = DataSourceAlias.from_dict(data_source_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


