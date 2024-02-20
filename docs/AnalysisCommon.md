# AnalysisCommon

attributes common between request and return objects

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study** | **str** |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_common import AnalysisCommon

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCommon from a JSON string
analysis_common_instance = AnalysisCommon.from_json(json)
# print the JSON string representation of the object
print AnalysisCommon.to_json()

# convert the object into a dict
analysis_common_dict = analysis_common_instance.to_dict()
# create an instance of AnalysisCommon from a dict
analysis_common_form_dict = analysis_common.from_dict(analysis_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


