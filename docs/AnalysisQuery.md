# AnalysisQuery

Criteria on a pipeline analysis. Group criteria (medical_condition, species, has_patients, has_healthy) match when any group the analysis ran on matches. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**medical_condition** | [**AnalysisQueryMedicalCondition**](AnalysisQueryMedicalCondition.md) |  | [optional] 
**has_patients** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**has_healthy** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**species** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**task** | [**AnalysisQueryNormalized**](AnalysisQueryNormalized.md) |  | [optional] 
**spatial_scope** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**coordinate_space** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**measure_type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**measure_family** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**details_type** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**is_meta_analysis** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**n** | [**AnalysisQueryRange**](AnalysisQueryRange.md) |  | [optional] 
**has_coordinates** | [**AnalysisQueryBoolean**](AnalysisQueryBoolean.md) |  | [optional] 
**role** | [**AnalysisQueryText**](AnalysisQueryText.md) |  | [optional] 
**contrast** | [**AnalysisQueryContrast**](AnalysisQueryContrast.md) |  | [optional] 
**design** | [**AnalysisQueryDesign**](AnalysisQueryDesign.md) |  | [optional] 
**sample** | [**AnalysisQuerySample**](AnalysisQuerySample.md) |  | [optional] 
**inference** | [**AnalysisQueryInference**](AnalysisQueryInference.md) |  | [optional] 
**acquisition** | [**AnalysisQueryAcquisition**](AnalysisQueryAcquisition.md) |  | [optional] 
**preprocessing** | [**AnalysisQueryPreprocessing**](AnalysisQueryPreprocessing.md) |  | [optional] 
**model** | [**AnalysisQueryModel**](AnalysisQueryModel.md) |  | [optional] 
**statistic** | [**AnalysisQueryStatistic**](AnalysisQueryStatistic.md) |  | [optional] 
**connectivity** | [**AnalysisQueryConnectivity**](AnalysisQueryConnectivity.md) |  | [optional] 
**region** | [**AnalysisQueryRegion**](AnalysisQueryRegion.md) |  | [optional] 
**coordinates** | [**AnalysisQueryCoordinates**](AnalysisQueryCoordinates.md) |  | [optional] 
**task_details** | [**AnalysisQueryTaskDetails**](AnalysisQueryTaskDetails.md) |  | [optional] 
**var_or** | **List[Dict[str, object]]** | Sub-queries, any of which may match; each takes this object&#39;s criteria. (Not a $ref to this schema, which resolvers that inline references cannot expand.)  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_query import AnalysisQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisQuery from a JSON string
analysis_query_instance = AnalysisQuery.from_json(json)
# print the JSON string representation of the object
print(AnalysisQuery.to_json())

# convert the object into a dict
analysis_query_dict = analysis_query_instance.to_dict()
# create an instance of AnalysisQuery from a dict
analysis_query_from_dict = AnalysisQuery.from_dict(analysis_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


