# Analysis

A contrast of weighted conditions with associated statistical results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | A name of the contrast being performed. | [optional] 
**description** | **str, none_type** | A long form description of how the contrast was performed | [optional] 
**weights** | **[float]** | Weight applied to each condition, must be the same length as the conditions attribute. | [optional] 
**conditions** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Array of conditions (e.g., 2-back, memory, etc.) that must be the same length as the weights attribute. Either is an array of condition objects or strings that point to condition objects. | [optional] 
**images** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Statistical images (e.g., beta, t-statistic, and/or z-statistic images) where each voxel gets a value. Either represented as an array of image objects or strings linking to image objects. | [optional] 
**points** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Coordinates of significance associated with the contrast. Either an array of point objects or an array of strings linking to point objects. | [optional] 
**study** | **bool, date, datetime, dict, float, int, list, str, none_type** | The study this analysis is associated with. Each analysis can only be associated to one and only one study, but a study can have multiple analyses. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


