# PointCommon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | **str** |  | [optional] 
**cluster_size** | **float** | size of the cluster in cubic millimeters | [optional] 
**subpeak** | **bool** | whether the reported peak is the max-peak statistic or a sub-maxmimal peak. | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from neurostore_sdk.models.point_common import PointCommon

# TODO update the JSON string below
json = "{}"
# create an instance of PointCommon from a JSON string
point_common_instance = PointCommon.from_json(json)
# print the JSON string representation of the object
print PointCommon.to_json()

# convert the object into a dict
point_common_dict = point_common_instance.to_dict()
# create an instance of PointCommon from a dict
point_common_form_dict = point_common.from_dict(point_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


