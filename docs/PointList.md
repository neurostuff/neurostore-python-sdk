# PointList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PointReturn]**](PointReturn.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.point_list import PointList

# TODO update the JSON string below
json = "{}"
# create an instance of PointList from a JSON string
point_list_instance = PointList.from_json(json)
# print the JSON string representation of the object
print(PointList.to_json())

# convert the object into a dict
point_list_dict = point_list_instance.to_dict()
# create an instance of PointList from a dict
point_list_from_dict = PointList.from_dict(point_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


