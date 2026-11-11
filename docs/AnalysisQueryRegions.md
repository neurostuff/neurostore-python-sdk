# AnalysisQueryRegions

The regions the analysis names, its seeds and targets, and its coordinate sets' regions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**atlas** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**region_type** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 
**definition_method** | [**AnalysisQueryValue**](AnalysisQueryValue.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query_regions import AnalysisQueryRegions

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQueryRegions from a JSON string
analysis_query_regions_instance = AnalysisQueryRegions.from_json(json)
# print the JSON string representation of the object
print(AnalysisQueryRegions.to_json())

# convert the object into a dict
analysis_query_regions_dict = analysis_query_regions_instance.to_dict()
# create an instance of AnalysisQueryRegions from a dict
analysis_query_regions_from_dict = AnalysisQueryRegions.from_dict(analysis_query_regions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


