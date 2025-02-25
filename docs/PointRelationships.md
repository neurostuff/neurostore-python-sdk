# PointRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** |  | [optional] 
**values** | [**PointRelationshipsValues**](PointRelationshipsValues.md) |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.point_relationships import PointRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PointRelationships from a JSON string
point_relationships_instance = PointRelationships.from_json(json)
# print the JSON string representation of the object
print(PointRelationships.to_json())

# convert the object into a dict
point_relationships_dict = point_relationships_instance.to_dict()
# create an instance of PointRelationships from a dict
point_relationships_from_dict = PointRelationships.from_dict(point_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


