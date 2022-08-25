# Point

A stereotaxic 3 dimensional coordinate describing a reported coordinate from a statistical map. This coordinate could be from a center of mass cluster, a peak statistic, a sub-threshold statistic, or from some other mechanism of selection 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **[float]** | Location of the significant coordinate in three dimensional space. | [optional] 
**space** | **str, none_type** | Template space used to determine coordinate Examples include TAL or MNI. | [optional] 
**kind** | **str, none_type** | Method of how point was derived (e.g., center of mass) | [optional] 
**label_id** | **str, none_type** | If the point is associated with an image, this is the value the point takes in that image. | [optional] 
**image** | **bool, date, datetime, dict, float, int, list, str, none_type** | Statistical image the point was derived from. Either points to an image object or a string linking to an image object. | [optional] 
**values** | [**[PointValue]**](PointValue.md) | An array of values at this point since each value could represent a beta, t-statistic and/or z-statistic, etc. | [optional] 
**analysis** | **bool, date, datetime, dict, float, int, list, str, none_type** | Analysis the point is associated with. Each point is associated with one and only one analysis, but an analysis can have multiple points. Either an analysis object or a string linking to an analysis object. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


