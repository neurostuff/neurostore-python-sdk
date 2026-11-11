# AnalysisFeatures

Only when `detail` is `features`: what the analysis's record says, in the shape of the query, each criterion's value under its path. A normalized criterion has its mapped `ids` (and `role_ids`, `family_ids`) and the record's wording as `text`; a text criterion has the record's wording. An item the record is silent on is absent. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medical_condition** | [**AnalysisFeaturesMedicalCondition**](AnalysisFeaturesMedicalCondition.md) |  | [optional] 
**has_patients** | **bool** |  | [optional] 
**has_healthy** | **bool** |  | [optional] 
**species** | **List[str]** |  | [optional] 
**task** | [**AnalysisFeaturesTask**](AnalysisFeaturesTask.md) |  | [optional] 
**spatial_scope** | **str** |  | [optional] 
**coordinate_space** | **str** |  | [optional] 
**measure_type** | **str** |  | [optional] 
**measure_family** | **str** |  | [optional] 
**details_type** | **str** |  | [optional] 
**is_meta_analysis** | **bool** |  | [optional] 
**n** | **int** |  | [optional] 
**contrast** | [**AnalysisFeaturesContrast**](AnalysisFeaturesContrast.md) |  | [optional] 
**design** | [**AnalysisFeaturesDesign**](AnalysisFeaturesDesign.md) |  | [optional] 
**groups** | [**AnalysisFeaturesGroups**](AnalysisFeaturesGroups.md) |  | [optional] 
**inference_settings** | [**AnalysisFeaturesInferenceSettings**](AnalysisFeaturesInferenceSettings.md) |  | [optional] 
**acquisitions** | [**AnalysisFeaturesAcquisitions**](AnalysisFeaturesAcquisitions.md) |  | [optional] 
**preprocessing** | [**AnalysisFeaturesPreprocessing**](AnalysisFeaturesPreprocessing.md) |  | [optional] 
**model_estimation** | [**AnalysisFeaturesModelEstimation**](AnalysisFeaturesModelEstimation.md) |  | [optional] 
**effect** | [**AnalysisFeaturesEffect**](AnalysisFeaturesEffect.md) |  | [optional] 
**details** | [**AnalysisFeaturesDetails**](AnalysisFeaturesDetails.md) |  | [optional] 
**regions** | [**AnalysisFeaturesRegions**](AnalysisFeaturesRegions.md) |  | [optional] 
**coordinate_sets** | [**AnalysisFeaturesCoordinateSets**](AnalysisFeaturesCoordinateSets.md) |  | [optional] 
**tasks** | [**AnalysisFeaturesTasks**](AnalysisFeaturesTasks.md) |  | [optional] 

## Example

```python
from neurostore_sdk.models.analysis_features import AnalysisFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFeatures from a JSON string
analysis_features_instance = AnalysisFeatures.from_json(json)
# print the JSON string representation of the object
print(AnalysisFeatures.to_json())

# convert the object into a dict
analysis_features_dict = analysis_features_instance.to_dict()
# create an instance of AnalysisFeatures from a dict
analysis_features_from_dict = AnalysisFeatures.from_dict(analysis_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


