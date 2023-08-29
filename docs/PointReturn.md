# PointReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** | Location of the significant coordinate in three dimensional space. | [optional] 
**space** | **str** | Template space used to determine coordinate Examples include TAL or MNI. | [optional] 
**kind** | **str** | Method of how point was derived (e.g., center of mass) | [optional] 
**label_id** | **str** | If the point is associated with an image, this is the value the point takes in that image. | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when was the resource last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 
**image** | **str** |  | [optional] 
**values** | [**PointRelationshipsValues**](PointRelationshipsValues.md) |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 
**analysis** | **str** |  | [optional] 
**cluster_size** | **float** | size of the cluster in cubic millimeters | [optional] 
**subpeak** | **bool** | whether the reported peak is the max-peak statistic or a sub-maxmimal peak. | [optional] 
**order** | **int** | determines the row to display the coordinate | [optional] 

## Example

```python
from neurostore_sdk.models.point_return import PointReturn

# TODO update the JSON string below
json = "{}"
# create an instance of PointReturn from a JSON string
point_return_instance = PointReturn.from_json(json)
# print the JSON string representation of the object
print PointReturn.to_json()

# convert the object into a dict
point_return_dict = point_return_instance.to_dict()
# create an instance of PointReturn from a dict
point_return_form_dict = point_return.from_dict(point_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


