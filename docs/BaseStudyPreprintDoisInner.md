# BaseStudyPreprintDoisInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doi** | **str** |  | 
**server** | **str** | The preprint server that registered the DOI: one of study_schema&#39;s PreprintServer values (biorxiv, medrxiv, arxiv, researchsquare, osf_preprints, psyarxiv, ssrn and others), or any other non-empty name for a server it does not list.  | 

## Example

```python
from neurostore_sdk.models.base_study_preprint_dois_inner import BaseStudyPreprintDoisInner

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStudyPreprintDoisInner from a JSON string
base_study_preprint_dois_inner_instance = BaseStudyPreprintDoisInner.from_json(json)
# print the JSON string representation of the object
print(BaseStudyPreprintDoisInner.to_json())

# convert the object into a dict
base_study_preprint_dois_inner_dict = base_study_preprint_dois_inner_instance.to_dict()
# create an instance of BaseStudyPreprintDoisInner from a dict
base_study_preprint_dois_inner_from_dict = BaseStudyPreprintDoisInner.from_dict(base_study_preprint_dois_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


