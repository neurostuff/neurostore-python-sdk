# BaseStudy


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
**authors** | **str** | The authors in published order, separated by \&quot;; \&quot; because a name may hold \&quot;, \&quot;. When a paper&#39;s structured author list has been uploaded the server derives this from it, and a value sent in a PUT, including null, is ignored. Values written before this was fixed may still be separated by \&quot;, \&quot; or \&quot;;\&quot;. | [optional] 
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

## Example

```python
from neurostore_sdk.models.base_study import BaseStudy

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudy from a JSON string
base_study_instance = BaseStudy.from_json(json)
# print the JSON string representation of the object
print(BaseStudy.to_json())

# convert the object into a dict
base_study_dict = base_study_instance.to_dict()
# create an instance of BaseStudy from a dict
base_study_from_dict = BaseStudy.from_dict(base_study_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


