# Study

A publishable unit of research.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doi** | **str, none_type** | Digital object identifier of the study. | [optional] 
**name** | **str, none_type** | Title of the study. | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Metadata associated with the study not covered by the other study attributes. | [optional] 
**description** | **str, none_type** | Long form description of the study, typically the abstract. | [optional] 
**publication** | **str, none_type** | The journal/place of publication for the study. | [optional] 
**pmid** | **str, none_type** | If the study was published on PubMed, place the PubMed ID here. | [optional] 
**authors** | **str, none_type** | The authors on the publication of this study. | [optional] 
**year** | **int, none_type** | The year this study was published. | [optional] 
**analyses** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | The analyses making up the study. A study can have one or more analyses, since each analysis represents a contrast of conditions, where psychological, behavioral, pharmacological, or group based. Either represented as an analysis object or a string pointing to the location of the analysis object. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


