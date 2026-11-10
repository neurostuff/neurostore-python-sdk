# AnalysisQueryRegion

The regions the analysis names, its seeds and targets, and its coordinate sets' regions. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**atlas** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**definition** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_region import AnalysisQueryRegion

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryRegion from a JSON string
analysis_query_region_instance = AnalysisQueryRegion.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryRegion.to_json())

# convert the object into a dict
analysis_query_region_dict = analysis_query_region_instance.to_dict()
# create an instance of AnalysisQueryRegion from a dict
analysis_query_region_from_dict = AnalysisQueryRegion.from_dict(analysis_query_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


