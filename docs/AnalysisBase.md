# AnalysisBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name of the contrast being performed. | [optional] 
**description** | **str** | A long form description of how the contrast was performed | [optional] 
**weights** | **List[float]** | Weight applied to each condition, must be the same length as the conditions attribute. | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_base import AnalysisBase

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisBase from a JSON string
analysis_base_instance = AnalysisBase.from_json(json)
# print the JSON string representation of the object
print(AnalysisBase.to_json())

# convert the object into a dict
analysis_base_dict = analysis_base_instance.to_dict()
# create an instance of AnalysisBase from a dict
analysis_base_form_dict = analysis_base.from_dict(analysis_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


