# neurostore_sdk.StudiesApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**base_studies_get**](StudiesApi.md#base_studies_get) | **GET** /base-studies/ | 
[**base_studies_id_get**](StudiesApi.md#base_studies_id_get) | **GET** /base-studies/{id} | Your GET endpoint
[**base_studies_id_put**](StudiesApi.md#base_studies_id_put) | **PUT** /base-studies/{id} | 
[**base_studies_post**](StudiesApi.md#base_studies_post) | **POST** /base-studies/ | 


# **base_studies_get**
> BaseStudyList base_studies_get(nested=nested, year_min=year_min, x=x, y=y, z=z, radius=radius, year_max=year_max, feature_filter=feature_filter, pipeline_config=pipeline_config, feature_display=feature_display, semantic_search=semantic_search, pipeline_config_id=pipeline_config_id, distance_threshold=distance_threshold, overall_cap=overall_cap, feature_flatten=feature_flatten, search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, map_type=map_type, is_oa=is_oa, publication=publication, pmid=pmid, doi=doi, neurovault_id=neurovault_id, flat=flat, info=info, paginate=paginate)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.base_study_list import BaseStudyList
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://neurostore.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "https://neurostore.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurostore_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurostore_sdk.StudiesApi(api_client)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    year_min = 56 # int | Minimum publication year (inclusive) for study search (optional)
    x = 10 # float | X coordinate for spatial query (requires y, z, and radius) (optional)
    y = 20 # float | Y coordinate for spatial query (requires x, z, and radius) (optional)
    z = 30 # float | Z coordinate for spatial query (requires x, y, and radius) (optional)
    radius = 6 # float | Radius for spatial query (requires x, y, and z) (optional)
    year_max = 2020 # int | Maximum publication year (inclusive) for study search (optional)
    feature_filter = ['feature_filter_example'] # List[str] | Filter studies by feature content. Format: \"PipelineName[:version]:field_path=value\". Examples:   - \"TestPipeline:1.0.0:predictions.age_mean>20\" (specific version)   - \"TestPipeline:groups.diagnosis=ADHD\" (latest version)  Field path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    pipeline_config = ['pipeline_config_example'] # List[str] | Filter studies by pipeline config content. Format: \"PipelineName[:version]:config_path=value\". Examples:   - \"TestPipeline:1.0.0:settings.min_age=20\" (specific version)   - \"TestPipeline:model.type=linear\" (latest version)  Config path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    feature_display = 'feature_display_example' # str | display features from pipelines (optional)
    semantic_search = 'semantic_search_example' # str | Semantic search query string (optional)
    pipeline_config_id = 'pipeline_config_id_example' # str | Pipeline configuration identifier to filter studies (optional)
    distance_threshold = 0.5 # float | Distance threshold for semantic search (default 0.5) (optional)
    overall_cap = 3000 # int | Maximum number of overall results to return (default 3000) (optional)
    feature_flatten = True # bool |  (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    authors = 'authors_example' # str | search authors (optional)
    level = group # str | select between studies with group results or meta results (optional) (default to group)
    data_type = 'data_type_example' # str | whether searching for studies that contain coordinates, images, or both (optional)
    map_type = 'map_type_example' # str | filter by stored map-type flags (optional)
    is_oa = True # bool |  (optional)
    publication = 'publication_example' # str | search for papers from a particular journal (optional)
    pmid = 'pmid_example' # str | search for particular pmid (optional)
    doi = 'doi_example' # str | search for study with specific doi (optional)
    neurovault_id = 'neurovault_id_example' # str | search for study with specific neurovault id (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)
    info = True # bool | show additional for endpoint-object relationships without being fully nested. Incompatible with nested (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)

    try:
        # 
        api_response = api_instance.base_studies_get(nested=nested, year_min=year_min, x=x, y=y, z=z, radius=radius, year_max=year_max, feature_filter=feature_filter, pipeline_config=pipeline_config, feature_display=feature_display, semantic_search=semantic_search, pipeline_config_id=pipeline_config_id, distance_threshold=distance_threshold, overall_cap=overall_cap, feature_flatten=feature_flatten, search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, map_type=map_type, is_oa=is_oa, publication=publication, pmid=pmid, doi=doi, neurovault_id=neurovault_id, flat=flat, info=info, paginate=paginate)
        print("The response of StudiesApi->base_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->base_studies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **year_min** | **int**| Minimum publication year (inclusive) for study search | [optional] 
 **x** | **float**| X coordinate for spatial query (requires y, z, and radius) | [optional] 
 **y** | **float**| Y coordinate for spatial query (requires x, z, and radius) | [optional] 
 **z** | **float**| Z coordinate for spatial query (requires x, y, and radius) | [optional] 
 **radius** | **float**| Radius for spatial query (requires x, y, and z) | [optional] 
 **year_max** | **int**| Maximum publication year (inclusive) for study search | [optional] 
 **feature_filter** | [**List[str]**](str.md)| Filter studies by feature content. Format: \&quot;PipelineName[:version]:field_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:predictions.age_mean&gt;20\&quot; (specific version)   - \&quot;TestPipeline:groups.diagnosis&#x3D;ADHD\&quot; (latest version)  Field path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **pipeline_config** | [**List[str]**](str.md)| Filter studies by pipeline config content. Format: \&quot;PipelineName[:version]:config_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:settings.min_age&#x3D;20\&quot; (specific version)   - \&quot;TestPipeline:model.type&#x3D;linear\&quot; (latest version)  Config path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **feature_display** | **str**| display features from pipelines | [optional] 
 **semantic_search** | **str**| Semantic search query string | [optional] 
 **pipeline_config_id** | **str**| Pipeline configuration identifier to filter studies | [optional] 
 **distance_threshold** | **float**| Distance threshold for semantic search (default 0.5) | [optional] 
 **overall_cap** | **int**| Maximum number of overall results to return (default 3000) | [optional] 
 **feature_flatten** | **bool**|  | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **authors** | **str**| search authors | [optional] 
 **level** | **str**| select between studies with group results or meta results | [optional] [default to group]
 **data_type** | **str**| whether searching for studies that contain coordinates, images, or both | [optional] 
 **map_type** | **str**| filter by stored map-type flags | [optional] 
 **is_oa** | **bool**|  | [optional] 
 **publication** | **str**| search for papers from a particular journal | [optional] 
 **pmid** | **str**| search for particular pmid | [optional] 
 **doi** | **str**| search for study with specific doi | [optional] 
 **neurovault_id** | **str**| search for study with specific neurovault id | [optional] 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 
 **info** | **bool**| show additional for endpoint-object relationships without being fully nested. Incompatible with nested | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]

### Return type

[**BaseStudyList**](BaseStudyList.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **base_studies_id_get**
> BaseStudyReturn base_studies_id_get(id, flat=flat, info=info, nested=nested)

Your GET endpoint

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.base_study_return import BaseStudyReturn
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://neurostore.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "https://neurostore.org/api"
)


# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurostore_sdk.StudiesApi(api_client)
    id = 'id_example' # str | 
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)
    info = True # bool | show additional for endpoint-object relationships without being fully nested. Incompatible with nested (optional)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.base_studies_id_get(id, flat=flat, info=info, nested=nested)
        print("The response of StudiesApi->base_studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->base_studies_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 
 **info** | **bool**| show additional for endpoint-object relationships without being fully nested. Incompatible with nested | [optional] 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 

### Return type

[**BaseStudyReturn**](BaseStudyReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **base_studies_id_put**
> BaseStudyReturn base_studies_id_put(id, base_study=base_study)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.base_study import BaseStudy
from neurostore_sdk.models.base_study_return import BaseStudyReturn
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://neurostore.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "https://neurostore.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurostore_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurostore_sdk.StudiesApi(api_client)
    id = 'id_example' # str | 
    base_study = neurostore_sdk.BaseStudy() # BaseStudy |  (optional)

    try:
        # 
        api_response = api_instance.base_studies_id_put(id, base_study=base_study)
        print("The response of StudiesApi->base_studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->base_studies_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **base_study** | [**BaseStudy**](BaseStudy.md)|  | [optional] 

### Return type

[**BaseStudyReturn**](BaseStudyReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **base_studies_post**
> BaseStudiesPost200Response base_studies_post(base_studies_post_request=base_studies_post_request)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.base_studies_post200_response import BaseStudiesPost200Response
from neurostore_sdk.models.base_studies_post_request import BaseStudiesPostRequest
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://neurostore.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "https://neurostore.org/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JSON-Web-Token
configuration = neurostore_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurostore_sdk.StudiesApi(api_client)
    base_studies_post_request = neurostore_sdk.BaseStudiesPostRequest() # BaseStudiesPostRequest |  (optional)

    try:
        # 
        api_response = api_instance.base_studies_post(base_studies_post_request=base_studies_post_request)
        print("The response of StudiesApi->base_studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->base_studies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_studies_post_request** | [**BaseStudiesPostRequest**](BaseStudiesPostRequest.md)|  | [optional] 

### Return type

[**BaseStudiesPost200Response**](BaseStudiesPost200Response.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

