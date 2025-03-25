# neurostore_sdk.StoreApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyses_get**](StoreApi.md#analyses_get) | **GET** /analyses/ | GET list of analyses
[**analyses_id_delete**](StoreApi.md#analyses_id_delete) | **DELETE** /analyses/{id} | DELETE an analysis
[**analyses_id_get**](StoreApi.md#analyses_id_get) | **GET** /analyses/{id} | GET an analysis
[**analyses_id_put**](StoreApi.md#analyses_id_put) | **PUT** /analyses/{id} | PUT/update an analysis
[**analyses_post**](StoreApi.md#analyses_post) | **POST** /analyses/ | POST/create an analysis
[**annotation_analyses_get**](StoreApi.md#annotation_analyses_get) | **GET** /annotation-analyses/ | Get annotation analyses
[**annotation_analyses_id_get**](StoreApi.md#annotation_analyses_id_get) | **GET** /annotation-analyses/{id} | Your GET endpoint
[**annotation_analyses_id_put**](StoreApi.md#annotation_analyses_id_put) | **PUT** /annotation-analyses/{id} | Your PUT endpoint
[**annotation_analyses_post**](StoreApi.md#annotation_analyses_post) | **POST** /annotation-analyses/ | Your POST endpoint
[**annotations_get**](StoreApi.md#annotations_get) | **GET** /annotations/ | Your GET endpoint
[**annotations_id_delete**](StoreApi.md#annotations_id_delete) | **DELETE** /annotations/{id} | DELETE an annotation
[**annotations_id_get**](StoreApi.md#annotations_id_get) | **GET** /annotations/{id} | Your GET endpoint
[**annotations_id_put**](StoreApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an annotation
[**annotations_post**](StoreApi.md#annotations_post) | **POST** /annotations/ | Post Annotation
[**base_studies_get**](StoreApi.md#base_studies_get) | **GET** /base-studies/ | 
[**base_studies_id_get**](StoreApi.md#base_studies_id_get) | **GET** /base-studies/{id} | Your GET endpoint
[**base_studies_id_put**](StoreApi.md#base_studies_id_put) | **PUT** /base-studies/{id} | 
[**base_studies_post**](StoreApi.md#base_studies_post) | **POST** /base-studies/ | 
[**conditions_get**](StoreApi.md#conditions_get) | **GET** /conditions/ | GET Conditions
[**conditions_id_delete**](StoreApi.md#conditions_id_delete) | **DELETE** /conditions/{id} | DELETE a condition
[**conditions_id_get**](StoreApi.md#conditions_id_get) | **GET** /conditions/{id} | GET a condition
[**conditions_id_put**](StoreApi.md#conditions_id_put) | **PUT** /conditions/{id} | PUT/update a condition
[**conditions_post**](StoreApi.md#conditions_post) | **POST** /conditions/ | POST/Create a condition
[**images_get**](StoreApi.md#images_get) | **GET** /images/ | GET a list of images
[**images_id_delete**](StoreApi.md#images_id_delete) | **DELETE** /images/{id} | DELETE an image
[**images_id_get**](StoreApi.md#images_id_get) | **GET** /images/{id} | GET an image
[**images_id_put**](StoreApi.md#images_id_put) | **PUT** /images/{id} | PUT/update an image
[**images_post**](StoreApi.md#images_post) | **POST** /images/ | POST/create an image
[**points_get**](StoreApi.md#points_get) | **GET** /points/ | Get Points
[**points_id_delete**](StoreApi.md#points_id_delete) | **DELETE** /points/{id} | DELETE a point
[**points_id_get**](StoreApi.md#points_id_get) | **GET** /points/{id} | GET a point
[**points_id_put**](StoreApi.md#points_id_put) | **PUT** /points/{id} | PUT/update a point
[**points_post**](StoreApi.md#points_post) | **POST** /points/ | POST Points
[**studies_get**](StoreApi.md#studies_get) | **GET** /studies/ | GET a list of studies
[**studies_id_delete**](StoreApi.md#studies_id_delete) | **DELETE** /studies/{id} | DELETE a study
[**studies_id_get**](StoreApi.md#studies_id_get) | **GET** /studies/{id} | GET a study
[**studies_id_put**](StoreApi.md#studies_id_put) | **PUT** /studies/{id} | PUT/update a study
[**studies_post**](StoreApi.md#studies_post) | **POST** /studies/ | POST/create a study
[**studysets_id_delete**](StoreApi.md#studysets_id_delete) | **DELETE** /studysets/{id} | DELETE a studyset
[**studysets_id_get**](StoreApi.md#studysets_id_get) | **GET** /studysets/{id} | GET a studyset
[**studysets_id_put**](StoreApi.md#studysets_id_put) | **PUT** /studysets/{id} | PUT/update a studyset
[**studysets_post**](StoreApi.md#studysets_post) | **POST** /studysets/ | POST/create a studyset


# **analyses_get**
> AnalysisList analyses_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, nested=nested)

GET list of analyses

List all analyses performed across studies.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.analysis_list import AnalysisList
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
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET list of analyses
        api_response = api_instance.analyses_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, nested=nested)
        print("The response of StoreApi->analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 

### Return type

[**AnalysisList**](AnalysisList.md)

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

# **analyses_id_delete**
> analyses_id_delete(id)

DELETE an analysis

delete an analysis

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
        # DELETE an analysis
        api_instance.analyses_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_id_delete: %s\n" % e)
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

# **analyses_id_get**
> AnalysisReturn analyses_id_get(id, nested=nested)

GET an analysis

Information pertaining to a particular analysis within a study.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.analysis_return import AnalysisReturn
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

    try:
        # GET an analysis
        api_response = api_instance.analyses_id_get(id, nested=nested)
        print("The response of StoreApi->analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 

### Return type

[**AnalysisReturn**](AnalysisReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_id_put**
> AnalysisReturn analyses_id_put(id, analysis_request=analysis_request)

PUT/update an analysis

Update an existing analysis.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.analysis_request import AnalysisRequest
from neurostore_sdk.models.analysis_return import AnalysisReturn
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
    analysis_request = neurostore_sdk.AnalysisRequest() # AnalysisRequest |  (optional)

    try:
        # PUT/update an analysis
        api_response = api_instance.analyses_id_put(id, analysis_request=analysis_request)
        print("The response of StoreApi->analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **analysis_request** | [**AnalysisRequest**](AnalysisRequest.md)|  | [optional] 

### Return type

[**AnalysisReturn**](AnalysisReturn.md)

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

# **analyses_post**
> AnalysisReturn analyses_post(analysis_request=analysis_request)

POST/create an analysis

create an analysis

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.analysis_request import AnalysisRequest
from neurostore_sdk.models.analysis_return import AnalysisReturn
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
    analysis_request = neurostore_sdk.AnalysisRequest() # AnalysisRequest |  (optional)

    try:
        # POST/create an analysis
        api_response = api_instance.analyses_post(analysis_request=analysis_request)
        print("The response of StoreApi->analyses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_request** | [**AnalysisRequest**](AnalysisRequest.md)|  | [optional] 

### Return type

[**AnalysisReturn**](AnalysisReturn.md)

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

# **annotation_analyses_get**
> NoteCollectionList annotation_analyses_get()

Get annotation analyses

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.note_collection_list import NoteCollectionList
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

    try:
        # Get annotation analyses
        api_response = api_instance.annotation_analyses_get()
        print("The response of StoreApi->annotation_analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotation_analyses_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NoteCollectionList**](NoteCollectionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annotation_analyses_id_get**
> NoteCollectionReturn annotation_analyses_id_get(id)

Your GET endpoint

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.note_collection_return import NoteCollectionReturn
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
        # Your GET endpoint
        api_response = api_instance.annotation_analyses_id_get(id)
        print("The response of StoreApi->annotation_analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotation_analyses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NoteCollectionReturn**](NoteCollectionReturn.md)

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

# **annotation_analyses_id_put**
> NoteCollectionReturn annotation_analyses_id_put(id, note_collection_request=note_collection_request)

Your PUT endpoint

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.note_collection_request import NoteCollectionRequest
from neurostore_sdk.models.note_collection_return import NoteCollectionReturn
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
    note_collection_request = neurostore_sdk.NoteCollectionRequest() # NoteCollectionRequest |  (optional)

    try:
        # Your PUT endpoint
        api_response = api_instance.annotation_analyses_id_put(id, note_collection_request=note_collection_request)
        print("The response of StoreApi->annotation_analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotation_analyses_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **note_collection_request** | [**NoteCollectionRequest**](NoteCollectionRequest.md)|  | [optional] 

### Return type

[**NoteCollectionReturn**](NoteCollectionReturn.md)

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

# **annotation_analyses_post**
> List[NoteCollectionReturn] annotation_analyses_post(note_collection_request=note_collection_request)

Your POST endpoint

This endpoint does not allow for creation, only modification of existing annotation-analyses. If you wish to create an annotation-analysis, post to the annotations endpoint and/or add the analysis to the appropriate study in the studyset, and the annotation-analysis will be created automatically. 

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.note_collection_request import NoteCollectionRequest
from neurostore_sdk.models.note_collection_return import NoteCollectionReturn
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
    note_collection_request = [neurostore_sdk.NoteCollectionRequest()] # List[NoteCollectionRequest] |  (optional)

    try:
        # Your POST endpoint
        api_response = api_instance.annotation_analyses_post(note_collection_request=note_collection_request)
        print("The response of StoreApi->annotation_analyses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotation_analyses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_collection_request** | [**List[NoteCollectionRequest]**](NoteCollectionRequest.md)|  | [optional] 

### Return type

[**List[NoteCollectionReturn]**](NoteCollectionReturn.md)

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

# **annotations_get**
> AnnotationList annotations_get(studyset_id=studyset_id)

Your GET endpoint

get annotations for an available studyset

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.annotation_list import AnnotationList
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
    studyset_id = 'studyset_id_example' # str | see all annotations connected to this studyset (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.annotations_get(studyset_id=studyset_id)
        print("The response of StoreApi->annotations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studyset_id** | **str**| see all annotations connected to this studyset | [optional] 

### Return type

[**AnnotationList**](AnnotationList.md)

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

# **annotations_id_delete**
> annotations_id_delete(id)

DELETE an annotation

delete annotation

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
        # DELETE an annotation
        api_instance.annotations_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_id_delete: %s\n" % e)
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

# **annotations_id_get**
> AnnotationReturn annotations_id_get(id, export=export)

Your GET endpoint

get an individual annotation

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.annotation_return import AnnotationReturn
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
    export = True # bool | return endpoint data in consumable/readable format (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.annotations_id_get(id, export=export)
        print("The response of StoreApi->annotations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **export** | **bool**| return endpoint data in consumable/readable format | [optional] 

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

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

# **annotations_id_put**
> AnnotationReturn annotations_id_put(id, annotation_request=annotation_request)

Update an annotation

edit an existing annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.annotation_request import AnnotationRequest
from neurostore_sdk.models.annotation_return import AnnotationReturn
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
    annotation_request = neurostore_sdk.AnnotationRequest() # AnnotationRequest |  (optional)

    try:
        # Update an annotation
        api_response = api_instance.annotations_id_put(id, annotation_request=annotation_request)
        print("The response of StoreApi->annotations_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **annotation_request** | [**AnnotationRequest**](AnnotationRequest.md)|  | [optional] 

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

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

# **annotations_post**
> AnnotationReturn annotations_post(source=source, source_id=source_id, annotation_request=annotation_request)

Post Annotation

Create an annotation

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.annotation_request import AnnotationRequest
from neurostore_sdk.models.annotation_return import AnnotationReturn
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
    annotation_request = neurostore_sdk.AnnotationRequest() # AnnotationRequest |  (optional)

    try:
        # Post Annotation
        api_response = api_instance.annotations_post(source=source, source_id=source_id, annotation_request=annotation_request)
        print("The response of StoreApi->annotations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **annotation_request** | [**AnnotationRequest**](AnnotationRequest.md)|  | [optional] 

### Return type

[**AnnotationReturn**](AnnotationReturn.md)

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

# **base_studies_get**
> BaseStudyList base_studies_get(feature_filter=feature_filter, feature_display=feature_display, search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, publication=publication, pmid=pmid, doi=doi, flat=flat, info=info)



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
    api_instance = neurostore_sdk.StoreApi(api_client)
    feature_filter = 'feature_filter_example' # str | Filter studies by features (optional)
    feature_display = 'feature_display_example' # str | display features from pipelines (optional)
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
        api_response = api_instance.base_studies_get(feature_filter=feature_filter, feature_display=feature_display, search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, publication=publication, pmid=pmid, doi=doi, flat=flat, info=info)
        print("The response of StoreApi->base_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->base_studies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_filter** | **str**| Filter studies by features | [optional] 
 **feature_display** | **str**| display features from pipelines | [optional] 
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)
    info = True # bool | show additional for endpoint-object relationships without being fully nested. Incompatible with nested (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.base_studies_id_get(id, flat=flat, info=info)
        print("The response of StoreApi->base_studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->base_studies_id_get: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    base_study = neurostore_sdk.BaseStudy() # BaseStudy |  (optional)

    try:
        # 
        api_response = api_instance.base_studies_id_put(id, base_study=base_study)
        print("The response of StoreApi->base_studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->base_studies_id_put: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    base_studies_post_request = neurostore_sdk.BaseStudiesPostRequest() # BaseStudiesPostRequest |  (optional)

    try:
        # 
        api_response = api_instance.base_studies_post(base_studies_post_request=base_studies_post_request)
        print("The response of StoreApi->base_studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->base_studies_post: %s\n" % e)
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

# **conditions_get**
> ConditionList conditions_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description)

GET Conditions

Get all conditions

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.condition_list import ConditionList
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
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)

    try:
        # GET Conditions
        api_response = api_instance.conditions_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description)
        print("The response of StoreApi->conditions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 

### Return type

[**ConditionList**](ConditionList.md)

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

# **conditions_id_delete**
> conditions_id_delete(id)

DELETE a condition

delete a condition

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
        # DELETE a condition
        api_instance.conditions_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_id_delete: %s\n" % e)
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

# **conditions_id_get**
> ConditionReturn conditions_id_get(id)

GET a condition

Retrieve a condition (e.g., 2-back) that can be used in contrasts (e.g., 2-back - 1-back)

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.condition_return import ConditionReturn
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

    try:
        # GET a condition
        api_response = api_instance.conditions_id_get(id)
        print("The response of StoreApi->conditions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConditionReturn**](ConditionReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conditions_id_put**
> ConditionReturn conditions_id_put(id, condition_request=condition_request)

PUT/update a condition

update a condition

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.condition_request import ConditionRequest
from neurostore_sdk.models.condition_return import ConditionReturn
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
    condition_request = neurostore_sdk.ConditionRequest() # ConditionRequest |  (optional)

    try:
        # PUT/update a condition
        api_response = api_instance.conditions_id_put(id, condition_request=condition_request)
        print("The response of StoreApi->conditions_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **condition_request** | [**ConditionRequest**](ConditionRequest.md)|  | [optional] 

### Return type

[**ConditionReturn**](ConditionReturn.md)

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

# **conditions_post**
> ConditionReturn conditions_post(condition_request=condition_request)

POST/Create a condition

Create a condition

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.condition_request import ConditionRequest
from neurostore_sdk.models.condition_return import ConditionReturn
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
    condition_request = neurostore_sdk.ConditionRequest() # ConditionRequest |  (optional)

    try:
        # POST/Create a condition
        api_response = api_instance.conditions_post(condition_request=condition_request)
        print("The response of StoreApi->conditions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **condition_request** | [**ConditionRequest**](ConditionRequest.md)|  | [optional] 

### Return type

[**ConditionReturn**](ConditionReturn.md)

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

# **images_get**
> ImageList images_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, filename=filename, analysis_name=analysis_name, value_type=value_type, space=space)

GET a list of images

Retrieve and list images.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.image_list import ImageList
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
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    filename = 'filename_example' # str | search filename field (optional)
    analysis_name = 'analysis_name_example' # str | search analysis_name field (optional)
    value_type = 'value_type_example' # str | search value_type field (optional)
    space = 'space_example' # str | search space field (optional)

    try:
        # GET a list of images
        api_response = api_instance.images_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, filename=filename, analysis_name=analysis_name, value_type=value_type, space=space)
        print("The response of StoreApi->images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **filename** | **str**| search filename field | [optional] 
 **analysis_name** | **str**| search analysis_name field | [optional] 
 **value_type** | **str**| search value_type field | [optional] 
 **space** | **str**| search space field | [optional] 

### Return type

[**ImageList**](ImageList.md)

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

# **images_id_delete**
> images_id_delete(id)

DELETE an image

delete an image

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
        # DELETE an image
        api_instance.images_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->images_id_delete: %s\n" % e)
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

# **images_id_get**
> ImageReturn images_id_get(id)

GET an image

Retrieve information about a particular image from an analysis.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.image_return import ImageReturn
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

    try:
        # GET an image
        api_response = api_instance.images_id_get(id)
        print("The response of StoreApi->images_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->images_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ImageReturn**](ImageReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_id_put**
> ImageReturn images_id_put(id, image_request=image_request)

PUT/update an image

Update a specific image.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.image_request import ImageRequest
from neurostore_sdk.models.image_return import ImageReturn
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
    image_request = neurostore_sdk.ImageRequest() # ImageRequest |  (optional)

    try:
        # PUT/update an image
        api_response = api_instance.images_id_put(id, image_request=image_request)
        print("The response of StoreApi->images_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->images_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **image_request** | [**ImageRequest**](ImageRequest.md)|  | [optional] 

### Return type

[**ImageReturn**](ImageReturn.md)

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

# **images_post**
> ImageReturn images_post(image_request=image_request)

POST/create an image

Create an image

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.image_request import ImageRequest
from neurostore_sdk.models.image_return import ImageReturn
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
    image_request = neurostore_sdk.ImageRequest() # ImageRequest |  (optional)

    try:
        # POST/create an image
        api_response = api_instance.images_post(image_request=image_request)
        print("The response of StoreApi->images_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->images_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_request** | [**ImageRequest**](ImageRequest.md)|  | [optional] 

### Return type

[**ImageReturn**](ImageReturn.md)

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

# **points_get**
> PointList points_get()

Get Points

list points in database

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.point_list import PointList
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

    try:
        # Get Points
        api_response = api_instance.points_get()
        print("The response of StoreApi->points_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->points_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PointList**](PointList.md)

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

# **points_id_delete**
> points_id_delete(id)

DELETE a point

delete a point

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
        # DELETE a point
        api_instance.points_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->points_id_delete: %s\n" % e)
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

# **points_id_get**
> PointReturn points_id_get(id)

GET a point

Information about a particular MRI coordinate

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.point_return import PointReturn
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

    try:
        # GET a point
        api_response = api_instance.points_id_get(id)
        print("The response of StoreApi->points_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->points_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PointReturn**](PointReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_id_put**
> PointReturn points_id_put(id, point_request=point_request)

PUT/update a point

Update a particular MRI coordinate.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.point_request import PointRequest
from neurostore_sdk.models.point_return import PointReturn
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
    point_request = neurostore_sdk.PointRequest() # PointRequest |  (optional)

    try:
        # PUT/update a point
        api_response = api_instance.points_id_put(id, point_request=point_request)
        print("The response of StoreApi->points_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->points_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **point_request** | [**PointRequest**](PointRequest.md)|  | [optional] 

### Return type

[**PointReturn**](PointReturn.md)

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

# **points_post**
> PointReturn points_post(point_request=point_request)

POST Points

add a point to an analysis

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.point_request import PointRequest
from neurostore_sdk.models.point_return import PointReturn
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
    point_request = neurostore_sdk.PointRequest() # PointRequest |  (optional)

    try:
        # POST Points
        api_response = api_instance.points_post(point_request=point_request)
        print("The response of StoreApi->points_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->points_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_request** | [**PointRequest**](PointRequest.md)|  | [optional] 

### Return type

[**PointReturn**](PointReturn.md)

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
    api_instance = neurostore_sdk.StoreApi(api_client)
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
> StudysetReturn studysets_id_get(id, nested=nested, gzip=gzip)

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
    gzip = True # bool | return the content as gzipped content (optional)

    try:
        # GET a studyset
        api_response = api_instance.studysets_id_get(id, nested=nested, gzip=gzip)
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
**404** | Example response |  -  |

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
**422** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_post**
> StudysetReturn studysets_post(studyset_request=studyset_request)

POST/create a studyset

Create a studyset.

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
    studyset_request = neurostore_sdk.StudysetRequest() # StudysetRequest |  (optional)

    try:
        # POST/create a studyset
        api_response = api_instance.studysets_post(studyset_request=studyset_request)
        print("The response of StoreApi->studysets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

