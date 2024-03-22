# neurostore_sdk.AnalysesApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyses_get**](AnalysesApi.md#analyses_get) | **GET** /analyses/ | GET list of analyses
[**analyses_id_delete**](AnalysesApi.md#analyses_id_delete) | **DELETE** /analyses/{id} | DELETE an analysis
[**analyses_id_get**](AnalysesApi.md#analyses_id_get) | **GET** /analyses/{id} | GET an analysis
[**analyses_id_put**](AnalysesApi.md#analyses_id_put) | **PUT** /analyses/{id} | PUT/update an analysis
[**analyses_post**](AnalysesApi.md#analyses_post) | **POST** /analyses/ | POST/create an analysis
[**annotation_analyses_get**](AnalysesApi.md#annotation_analyses_get) | **GET** /annotation-analyses/ | Get annotation analyses
[**annotation_analyses_id_get**](AnalysesApi.md#annotation_analyses_id_get) | **GET** /annotation-analyses/{id} | Your GET endpoint
[**annotation_analyses_id_put**](AnalysesApi.md#annotation_analyses_id_put) | **PUT** /annotation-analyses/{id} | Your PUT endpoint
[**annotation_analyses_post**](AnalysesApi.md#annotation_analyses_post) | **POST** /annotation-analyses/ | Your POST endpoint


# **analyses_get**
> AnalysisList analyses_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, nested=nested)

GET list of analyses

List all analyses performed across studies.

### Example

```python
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
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
        print("The response of AnalysesApi->analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->analyses_get: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE an analysis
        api_instance.analyses_id_delete(id)
    except Exception as e:
        print("Exception when calling AnalysesApi->analyses_id_delete: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET an analysis
        api_response = api_instance.analyses_id_get(id, nested=nested)
        print("The response of AnalysesApi->analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->analyses_id_get: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
    id = 'id_example' # str | 
    analysis_request = neurostore_sdk.AnalysisRequest() # AnalysisRequest |  (optional)

    try:
        # PUT/update an analysis
        api_response = api_instance.analyses_id_put(id, analysis_request=analysis_request)
        print("The response of AnalysesApi->analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->analyses_id_put: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
    analysis_request = neurostore_sdk.AnalysisRequest() # AnalysisRequest |  (optional)

    try:
        # POST/create an analysis
        api_response = api_instance.analyses_post(analysis_request=analysis_request)
        print("The response of AnalysesApi->analyses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->analyses_post: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)

    try:
        # Get annotation analyses
        api_response = api_instance.annotation_analyses_get()
        print("The response of AnalysesApi->annotation_analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->annotation_analyses_get: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.annotation_analyses_id_get(id)
        print("The response of AnalysesApi->annotation_analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->annotation_analyses_id_get: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
    id = 'id_example' # str | 
    note_collection_request = neurostore_sdk.NoteCollectionRequest() # NoteCollectionRequest |  (optional)

    try:
        # Your PUT endpoint
        api_response = api_instance.annotation_analyses_id_put(id, note_collection_request=note_collection_request)
        print("The response of AnalysesApi->annotation_analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->annotation_analyses_id_put: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
    note_collection_request = [neurostore_sdk.NoteCollectionRequest()] # List[NoteCollectionRequest] |  (optional)

    try:
        # Your POST endpoint
        api_response = api_instance.annotation_analyses_post(note_collection_request=note_collection_request)
        print("The response of AnalysesApi->annotation_analyses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->annotation_analyses_post: %s\n" % e)
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

