# PointValue



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from neurostore_sdk.models.point_value import PointValue

# TODO update the JSON string below
json = "{}"
# create an instance of PointValue from a JSON string
point_value_instance = PointValue.from_json(json)
# print the JSON string representation of the object
print(PointValue.to_json())

# convert the object into a dict
point_value_dict = point_value_instance.to_dict()
# create an instance of PointValue from a dict
point_value_form_dict = point_value.from_dict(point_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


