# ImageValueSummary

Distribution statistics for the image's voxel values, computed once and stored. Present only when image_value_summary=true is requested, and null when the image has never been summarized. Counts cover every voxel in the file; the distribution fields (min/max/mean/std, percentiles, histogram) cover only the finite, non-zero voxels, because neuroimaging maps store their background as zero or nan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | SUCCESS when the numbers below are populated, FAILURE when the image could not be read. | [optional] 
**error** | **str** | Why the last attempt failed, when status is not SUCCESS. | [optional] 
**summarizer_version** | **int** | Which version of the summarizer produced these numbers. | [optional] 
**computed_at** | **datetime** |  | [optional] 
**source_sha256** | **str** | SHA-256 of the file that was summarized, so a client can tell whether the numbers still describe the file at url. | [optional] 
**source_bytes** | **int** |  | [optional] 
**n_voxels** | **int** | Total voxels in the file; the denominator for fraction_nan and fraction_zero. | [optional] 
**n_values** | **int** | Finite, non-zero voxels; the n behind the distribution fields and the denominator for fraction_negative. | [optional] 
**fraction_nan** | **float** | Non-finite (nan or inf) voxels over n_voxels. | [optional] 
**fraction_zero** | **float** | Exactly-zero voxels over n_voxels. | [optional] 
**fraction_negative** | **float** | Negative voxels over n_values. A z or t map with a fraction near zero here is either one-sided or mislabelled. | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**mean** | **float** |  | [optional] 
**std** | **float** |  | [optional] 
**percentiles** | **Dict[str, Optional[float]]** | Percentile value keyed by probe, e.g. {\&quot;0.1\&quot;: -5.2, \&quot;1\&quot;: -3.1, ... \&quot;99.9\&quot;: 5.8}. | [optional] 
**histogram** | [**ImageValueSummaryHistogram**](ImageValueSummaryHistogram.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.image_value_summary import ImageValueSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ImageValueSummary from a JSON string
image_value_summary_instance = ImageValueSummary.from_json(json)
# print the JSON string representation of the object
print(ImageValueSummary.to_json())

# convert the object into a dict
image_value_summary_dict = image_value_summary_instance.to_dict()
# create an instance of ImageValueSummary from a dict
image_value_summary_from_dict = ImageValueSummary.from_dict(image_value_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


