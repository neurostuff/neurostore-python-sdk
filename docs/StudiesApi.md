# neurostore_sdk.StudiesApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**base_studies_get**](StudiesApi.md#base_studies_get) | **GET** /base-studies/ | 
[**base_studies_id_get**](StudiesApi.md#base_studies_id_get) | **GET** /base-studies/{id} | Your GET endpoint
[**base_studies_id_put**](StudiesApi.md#base_studies_id_put) | **PUT** /base-studies/{id} | 
[**base_studies_post**](StudiesApi.md#base_studies_post) | **POST** /base-studies/ | 
[**studies_get**](StudiesApi.md#studies_get) | **GET** /studies/ | GET a list of studies
[**studies_id_delete**](StudiesApi.md#studies_id_delete) | **DELETE** /studies/{id} | DELETE a study
[**studies_id_get**](StudiesApi.md#studies_id_get) | **GET** /studies/{id} | GET a study
[**studies_id_put**](StudiesApi.md#studies_id_put) | **PUT** /studies/{id} | PUT/update a study
[**studies_post**](StudiesApi.md#studies_post) | **POST** /studies/ | POST/create a study


# **base_studies_get**
> BaseStudyList base_studies_get(feature_filter=feature_filter, pipeline_config=pipeline_config, feature_display=feature_display, feature_flatten=feature_flatten, search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, publication=publication, pmid=pmid, doi=doi, flat=flat, info=info)



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
    feature_filter = ['feature_filter_example'] # List[str] | Filter studies by feature content. Format: \"PipelineName[:version]:field_path=value\". Examples:   - \"TestPipeline:1.0.0:predictions.age_mean>20\" (specific version)   - \"TestPipeline:groups.diagnosis=ADHD\" (any version)  Field path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    pipeline_config = ['pipeline_config_example'] # List[str] | Filter studies by pipeline config content. Format: \"PipelineName[:version]:config_path=value\". Examples:   - \"TestPipeline:1.0.0:settings.min_age=20\" (specific version)   - \"TestPipeline:model.type=linear\" (any version)  Config path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    feature_display = 'feature_display_example' # str | display features from pipelines (optional)
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
    publication = 'publication_example' # str | search for papers from a particular journal (optional)
    pmid = 'pmid_example' # str | search for particular pmid (optional)
    doi = 'doi_example' # str | search for study with specific doi (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)
    info = True # bool | show additional for endpoint-object relationships without being fully nested. Incompatible with nested (optional)

    try:
        # 
        api_response = api_instance.base_studies_get(feature_filter=feature_filter, pipeline_config=pipeline_config, feature_display=feature_display, feature_flatten=feature_flatten, search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, publication=publication, pmid=pmid, doi=doi, flat=flat, info=info)
        print("The response of StudiesApi->base_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->base_studies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_filter** | [**List[str]**](str.md)| Filter studies by feature content. Format: \&quot;PipelineName[:version]:field_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:predictions.age_mean&gt;20\&quot; (specific version)   - \&quot;TestPipeline:groups.diagnosis&#x3D;ADHD\&quot; (any version)  Field path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **pipeline_config** | [**List[str]**](str.md)| Filter studies by pipeline config content. Format: \&quot;PipelineName[:version]:config_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:settings.min_age&#x3D;20\&quot; (specific version)   - \&quot;TestPipeline:model.type&#x3D;linear\&quot; (any version)  Config path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **feature_display** | **str**| display features from pipelines | [optional] 
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
 **publication** | **str**| search for papers from a particular journal | [optional] 
 **pmid** | **str**| search for particular pmid | [optional] 
 **doi** | **str**| search for study with specific doi | [optional] 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 
 **info** | **bool**| show additional for endpoint-object relationships without being fully nested. Incompatible with nested | [optional] 

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
> BaseStudyReturn base_studies_id_get(id, flat=flat, info=info)

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

    try:
        # Your GET endpoint
        api_response = api_instance.base_studies_id_get(id, flat=flat, info=info)
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

# **studies_get**
> StudyList studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, nested=nested, name=name, description=description, source_id=source_id, unique=unique, source=source, authors=authors, user_id=user_id, data_type=data_type, studyset_owner=studyset_owner, level=level, pmid=pmid, doi=doi, flat=flat)

GET a list of studies

List studies

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.study_list import StudyList
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
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    unique = None # object | whether to list clones with originals (optional)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    authors = 'authors_example' # str | search authors (optional)
    user_id = 'user_id_example' # str | user id you want to filter by (optional)
    data_type = 'data_type_example' # str | whether searching for studies that contain coordinates, images, or both (optional)
    studyset_owner = 'studyset_owner_example' # str | for all studies filter which studysets are listed based on who owns the studyset (optional)
    level = group # str | select between studies with group results or meta results (optional) (default to group)
    pmid = 'pmid_example' # str | search for particular pmid (optional)
    doi = 'doi_example' # str | search for study with specific doi (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)

    try:
        # GET a list of studies
        api_response = api_instance.studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, nested=nested, name=name, description=description, source_id=source_id, unique=unique, source=source, authors=authors, user_id=user_id, data_type=data_type, studyset_owner=studyset_owner, level=level, pmid=pmid, doi=doi, flat=flat)
        print("The response of StudiesApi->studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->studies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **unique** | [**object**](.md)| whether to list clones with originals | [optional] 
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **authors** | **str**| search authors | [optional] 
 **user_id** | **str**| user id you want to filter by | [optional] 
 **data_type** | **str**| whether searching for studies that contain coordinates, images, or both | [optional] 
 **studyset_owner** | **str**| for all studies filter which studysets are listed based on who owns the studyset | [optional] 
 **level** | **str**| select between studies with group results or meta results | [optional] [default to group]
 **pmid** | **str**| search for particular pmid | [optional] 
 **doi** | **str**| search for study with specific doi | [optional] 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 

### Return type

[**StudyList**](StudyList.md)

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

# **studies_id_delete**
> studies_id_delete(id)

DELETE a study

delete a study

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
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

    try:
        # DELETE a study
        api_instance.studies_id_delete(id)
    except Exception as e:
        print("Exception when calling StudiesApi->studies_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_id_get**
> StudyReturn studies_id_get(id, nested=nested, studyset_owner=studyset_owner, flat=flat)

GET a study

Get a study.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.study_return import StudyReturn
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
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    studyset_owner = 'studyset_owner_example' # str | for all studies filter which studysets are listed based on who owns the studyset (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)

    try:
        # GET a study
        api_response = api_instance.studies_id_get(id, nested=nested, studyset_owner=studyset_owner, flat=flat)
        print("The response of StudiesApi->studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->studies_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **studyset_owner** | **str**| for all studies filter which studysets are listed based on who owns the studyset | [optional] 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 

### Return type

[**StudyReturn**](StudyReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study Found |  -  |
**404** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_id_put**
> StudyReturn studies_id_put(id, study_request=study_request)

PUT/update a study

Update a study.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.study_request import StudyRequest
from neurostore_sdk.models.study_return import StudyReturn
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
    study_request = neurostore_sdk.StudyRequest() # StudyRequest |  (optional)

    try:
        # PUT/update a study
        api_response = api_instance.studies_id_put(id, study_request=study_request)
        print("The response of StudiesApi->studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->studies_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **study_request** | [**StudyRequest**](StudyRequest.md)|  | [optional] 

### Return type

[**StudyReturn**](StudyReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_post**
> StudyReturn studies_post(source=source, source_id=source_id, study_request=study_request)

POST/create a study

Create a study

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.study_request import StudyRequest
from neurostore_sdk.models.study_return import StudyReturn
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
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    study_request = neurostore_sdk.StudyRequest() # StudyRequest |  (optional)

    try:
        # POST/create a study
        api_response = api_instance.studies_post(source=source, source_id=source_id, study_request=study_request)
        print("The response of StudiesApi->studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudiesApi->studies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **study_request** | [**StudyRequest**](StudyRequest.md)|  | [optional] 

### Return type

[**StudyReturn**](StudyReturn.md)

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

