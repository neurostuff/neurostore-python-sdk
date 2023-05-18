# PointBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** | Location of the significant coordinate in three dimensional space. | [optional] 
**space** | **str** | Template space used to determine coordinate Examples include TAL or MNI. | [optional] 
**kind** | **str** | Method of how point was derived (e.g., center of mass) | [optional] 
**label_id** | **str** | If the point is associated with an image, this is the value the point takes in that image. | [optional] 

## Example

```python
from neurostore_sdk.models.point_base import PointBase

# TODO update the JSON string below
json = "{}"
# create an instance of PointBase from a JSON string
point_base_instance = PointBase.from_json(json)
# print the JSON string representation of the object
print PointBase.to_json()

# convert the object into a dict
point_base_dict = point_base_instance.to_dict()
# create an instance of PointBase from a dict
point_base_form_dict = point_base.from_dict(point_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


