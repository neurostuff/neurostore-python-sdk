# PointRelationshipsValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from neurostore_sdk.models.point_relationships_value import PointRelationshipsValue

# TODO update the JSON string below
json = "{}"
# create an instance of PointRelationshipsValue from a JSON string
point_relationships_value_instance = PointRelationshipsValue.from_json(json)
# print the JSON string representation of the object
print PointRelationshipsValue.to_json()

# convert the object into a dict
point_relationships_value_dict = point_relationships_value_instance.to_dict()
# create an instance of PointRelationshipsValue from a dict
point_relationships_value_form_dict = point_relationships_value.from_dict(point_relationships_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


