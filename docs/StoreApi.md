# neurostore_sdk.StoreApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studies_get**](StoreApi.md#studies_get) | **GET** /studies/ | GET a list of studies
[**studies_id_delete**](StoreApi.md#studies_id_delete) | **DELETE** /studies/{id} | DELETE a study
[**studies_id_get**](StoreApi.md#studies_id_get) | **GET** /studies/{id} | GET a study
[**studies_id_put**](StoreApi.md#studies_id_put) | **PUT** /studies/{id} | PUT/update a study
[**studies_post**](StoreApi.md#studies_post) | **POST** /studies/ | POST/create a study
[**studysets_id_delete**](StoreApi.md#studysets_id_delete) | **DELETE** /studysets/{id} | DELETE a studyset
[**studysets_id_get**](StoreApi.md#studysets_id_get) | **GET** /studysets/{id} | GET a studyset
[**studysets_id_put**](StoreApi.md#studysets_id_put) | **PUT** /studysets/{id} | PUT/update a studyset
[**studysets_post**](StoreApi.md#studysets_post) | **POST** /studysets/ | POST/create a studyset


# **studies_get**
> StudyList studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, nested=nested, name=name, description=description, source_id=source_id, unique=unique, source=source, authors=authors, user_id=user_id, data_type=data_type, map_type=map_type, studyset_owner=studyset_owner, level=level, pmid=pmid, doi=doi, flat=flat)

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    unique = None # object | whether to list clones with originals (optional)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    authors = 'authors_example' # str | search authors (optional)
    user_id = 'user_id_example' # str | user id you want to filter by (optional)
    data_type = 'data_type_example' # str | whether searching for studies that contain coordinates, images, or both (optional)
    map_type = 'map_type_example' # str | filter by stored map-type flags (optional)
    studyset_owner = 'studyset_owner_example' # str | for all studies filter which studysets are listed based on who owns the studyset (optional)
    level = group # str | select between studies with group results or meta results (optional) (default to group)
    pmid = 'pmid_example' # str | search for particular pmid (optional)
    doi = 'doi_example' # str | search for study with specific doi (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)

    try:
        # GET a list of studies
        api_response = api_instance.studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, nested=nested, name=name, description=description, source_id=source_id, unique=unique, source=source, authors=authors, user_id=user_id, data_type=data_type, map_type=map_type, studyset_owner=studyset_owner, level=level, pmid=pmid, doi=doi, flat=flat)
        print("The response of StoreApi->studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **unique** | [**object**](.md)| whether to list clones with originals | [optional] 
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **authors** | **str**| search authors | [optional] 
 **user_id** | **str**| user id you want to filter by | [optional] 
 **data_type** | **str**| whether searching for studies that contain coordinates, images, or both | [optional] 
 **map_type** | **str**| filter by stored map-type flags | [optional] 
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a study
        api_instance.studies_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->studies_id_delete: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    studyset_owner = 'studyset_owner_example' # str | for all studies filter which studysets are listed based on who owns the studyset (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)

    try:
        # GET a study
        api_response = api_instance.studies_id_get(id, nested=nested, studyset_owner=studyset_owner, flat=flat)
        print("The response of StoreApi->studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studies_id_get: %s\n" % e)
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
**404** | Not Found |  -  |

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    study_request = neurostore_sdk.StudyRequest() # StudyRequest |  (optional)

    try:
        # PUT/update a study
        api_response = api_instance.studies_id_put(id, study_request=study_request)
        print("The response of StoreApi->studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studies_id_put: %s\n" % e)
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
**422** | Unprocessable Entity |  -  |

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    study_request = neurostore_sdk.StudyRequest() # StudyRequest |  (optional)

    try:
        # POST/create a study
        api_response = api_instance.studies_post(source=source, source_id=source_id, study_request=study_request)
        print("The response of StoreApi->studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studies_post: %s\n" % e)
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

# **studysets_id_delete**
> studysets_id_delete(id)

DELETE a studyset

delete a studyset

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a studyset
        api_instance.studysets_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_id_delete: %s\n" % e)
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

# **studysets_id_get**
> StudysetReturn studysets_id_get(id, nested=nested, summary=summary, gzip=gzip)

GET a studyset

Retrieve the information of a studyset with the matching studyset ID.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    summary = True # bool | return a lightweight summary payload with study metadata and per-analysis coordinate counts; incompatible with nested (optional)
    gzip = True # bool | return the content as gzipped content (optional)

    try:
        # GET a studyset
        api_response = api_instance.studysets_id_get(id, nested=nested, summary=summary, gzip=gzip)
        print("The response of StoreApi->studysets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **summary** | **bool**| return a lightweight summary payload with study metadata and per-analysis coordinate counts; incompatible with nested | [optional] 
 **gzip** | **bool**| return the content as gzipped content | [optional] 

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/gzip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | studyset found |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_id_put**
> StudysetReturn studysets_id_put(id, studyset_request=studyset_request)

PUT/update a studyset

Update a studyset.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.studyset_request import StudysetRequest
from neurostore_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    studyset_request = neurostore_sdk.StudysetRequest() # StudysetRequest |  (optional)

    try:
        # PUT/update a studyset
        api_response = api_instance.studysets_id_put(id, studyset_request=studyset_request)
        print("The response of StoreApi->studysets_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **studyset_request** | [**StudysetRequest**](StudysetRequest.md)|  | [optional] 

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_post**
> StudysetReturn studysets_post(source_id=source_id, source=source, copy_annotations=copy_annotations, studyset_request=studyset_request)

POST/create a studyset

Create a studyset. When `source_id` is provided, Neurostore clones an existing studyset owned by any user into a new studyset owned by the caller, copying studies and (by default) annotations.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.studyset_request import StudysetRequest
from neurostore_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    copy_annotations = True # bool | When cloning a studyset, copy annotations and their notes when true (default). (optional) (default to True)
    studyset_request = neurostore_sdk.StudysetRequest() # StudysetRequest |  (optional)

    try:
        # POST/create a studyset
        api_response = api_instance.studysets_post(source_id=source_id, source=source, copy_annotations=copy_annotations, studyset_request=studyset_request)
        print("The response of StoreApi->studysets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **copy_annotations** | **bool**| When cloning a studyset, copy annotations and their notes when true (default). | [optional] [default to True]
 **studyset_request** | [**StudysetRequest**](StudysetRequest.md)|  | [optional] 

### Return type

[**StudysetReturn**](StudysetReturn.md)

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

