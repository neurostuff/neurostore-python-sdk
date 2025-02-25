# AnalysisList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**results** | [**List[AnalysisReturn]**](AnalysisReturn.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_list import AnalysisList

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisList from a JSON string
analysis_list_instance = AnalysisList.from_json(json)
# print the JSON string representation of the object
print(AnalysisList.to_json())

# convert the object into a dict
analysis_list_dict = analysis_list_instance.to_dict()
# create an instance of AnalysisList from a dict
analysis_list_from_dict = AnalysisList.from_dict(analysis_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


