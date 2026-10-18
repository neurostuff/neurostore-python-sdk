# ReviewImportReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loaded** | [**List[ReviewImportReportLoadedInner]**](ReviewImportReportLoadedInner.md) |  | 
**skipped** | [**List[ReviewImportReportSkippedInner]**](ReviewImportReportSkippedInner.md) |  | 
**failed** | [**List[ReviewImportReportFailedInner]**](ReviewImportReportFailedInner.md) |  | 

## Example

```python
from neurostore_sdk.models.review_import_report import ReviewImportReport

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewImportReport from a JSON string
review_import_report_instance = ReviewImportReport.from_json(json)
# print the JSON string representation of the object
print(ReviewImportReport.to_json())

# convert the object into a dict
review_import_report_dict = review_import_report_instance.to_dict()
# create an instance of ReviewImportReport from a dict
review_import_report_from_dict = ReviewImportReport.from_dict(review_import_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


