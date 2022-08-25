# Image

A description of a brain image linking to the actual nifti file (typically on neurovault).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata about image such as software and version used and other relevant data about how the image was produced. | [optional] 
**url** | **str, none_type** | URL to image file. | [optional] 
**filename** | **str, none_type** | Name of the image file. | [optional] 
**space** | **str, none_type** | The template space the image is in (e.g., MNI  | [optional] 
**value_type** | **str, none_type** | The values the image represents. For example, T-statistic or Z-statistic, or Betas. | [optional] 
**add_date** | **datetime, none_type** | Date the image was added. | [optional] [readonly] 
**analysis** | **bool, date, datetime, dict, float, int, list, str, none_type** | Analysis the image is associated with. Each image is associated with one and only one analysis, but an analysis can have multiple images. Either an analysis object or a string linking to an analysis object. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


