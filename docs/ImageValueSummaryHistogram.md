# ImageValueSummaryHistogram

Equal-width bins over [min, max]. Bin edges are implied by the bounds and the length of counts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**bin_width** | **float** |  | [optional] 
**counts** | **List[int]** |  | [optional] 
**underflow** | **int** | Values below min, clipped out of the binned range. | [optional] 
**overflow** | **int** | Values above max, clipped out of the binned range. | [optional] 

## Example

```python
from neurostore_sdk.models.image_value_summary_histogram import ImageValueSummaryHistogram

# TODO update the JSON string below
json = "{}"
# create an instance of ImageValueSummaryHistogram from a JSON string
image_value_summary_histogram_instance = ImageValueSummaryHistogram.from_json(json)
# print the JSON string representation of the object
print(ImageValueSummaryHistogram.to_json())

# convert the object into a dict
image_value_summary_histogram_dict = image_value_summary_histogram_instance.to_dict()
# create an instance of ImageValueSummaryHistogram from a dict
image_value_summary_histogram_from_dict = ImageValueSummaryHistogram.from_dict(image_value_summary_histogram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


