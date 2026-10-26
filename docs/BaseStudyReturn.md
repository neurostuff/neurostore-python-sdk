# BaseStudyReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**versions** | [**List[BaseStudyVersionsInner]**](BaseStudyVersionsInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**publication** | **str** |  | [optional] 
**doi** | **str** |  | [optional] 
**pmid** | **str** |  | [optional] 
**authors** | **str** | The authors in published order, separated by \&quot;; \&quot;. When a paper&#39;s structured author list has been uploaded the server derives this from it, and a value sent in a PUT is ignored. | [optional] 
**year** | **int** |  | [optional] 
**level** | **str** |  | [optional] 
**is_oa** | **bool** |  | [optional] 
**pmcid** | **str** |  | [optional] 
**publication_status** | **str** | study_schema&#39;s publication_status: &#x60;preprint&#x60; while only a preprint&#39;s identifiers are known, &#x60;published&#x60; once a version of record&#39;s are.  | [optional] 
**preprint_dois** | [**List[BaseStudyPreprintDoisInner]**](BaseStudyPreprintDoisInner.md) | DOIs a preprint server registered for the paper, with the server. An identifier is held by one active base study: one another base study holds is not taken (see POST /base-studies). Returned normalized: DOIs in lower case.  | [optional] 
**preprint_pmids** | **List[str]** | PubMed&#39;s records of the paper&#39;s preprint. | [optional] 
**preprint_pmcids** | **List[str]** | PubMed Central&#39;s copies of the paper&#39;s preprint. | [optional] 
**alternative_dois** | **List[str]** | Any other DOI of the paper that is neither the version of record&#39;s &#x60;doi&#x60; nor a preprint&#39;s.  | [optional] 
**alternative_pmids** | **List[str]** | Any other PMID of the paper that is neither &#x60;pmid&#x60; nor a preprint&#39;s. | [optional] 
**alternative_pmcids** | **List[str]** | Any other PMCID of the paper that is neither &#x60;pmcid&#x60; nor a preprint&#39;s. | [optional] 
**created_at** | **datetime** | time the resource was created on the database | [optional] [readonly] 
**updated_at** | **str** | when the resource was last modified/updated. | [optional] [readonly] 
**id** | **str** | short UUID specifying the location of this resource | [optional] 
**public** | **bool** | whether the resource is listed in public searches or not | [optional] [default to True]
**user** | **str** | who owns the resource | [optional] [readonly] 
**username** | **str** | human readable username | [optional] 
**has_coordinates** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**has_z_maps** | **bool** |  | [optional] 
**has_t_maps** | **bool** |  | [optional] 
**has_beta_and_variance_maps** | **bool** |  | [optional] 
**features** | **object** |  | [optional] 

## Example

```python
from neurostore_sdk.models.base_study_return import BaseStudyReturn

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudyReturn from a JSON string
base_study_return_instance = BaseStudyReturn.from_json(json)
# print the JSON string representation of the object
print(BaseStudyReturn.to_json())

# convert the object into a dict
base_study_return_dict = base_study_return_instance.to_dict()
# create an instance of BaseStudyReturn from a dict
base_study_return_from_dict = BaseStudyReturn.from_dict(base_study_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


