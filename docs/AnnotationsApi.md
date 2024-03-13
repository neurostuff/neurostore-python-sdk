# neurostore_sdk.AnnotationsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotation_analyses_get**](AnnotationsApi.md#annotation_analyses_get) | **GET** /annotation-analyses/ | Get annotation analyses
[**annotation_analyses_id_get**](AnnotationsApi.md#annotation_analyses_id_get) | **GET** /annotation-analyses/{id} | Your GET endpoint
[**annotation_analyses_id_put**](AnnotationsApi.md#annotation_analyses_id_put) | **PUT** /annotation-analyses/{id} | Your PUT endpoint
[**annotations_get**](AnnotationsApi.md#annotations_get) | **GET** /annotations/ | Your GET endpoint
[**annotations_id_delete**](AnnotationsApi.md#annotations_id_delete) | **DELETE** /annotations/{id} | DELETE an annotation
[**annotations_id_get**](AnnotationsApi.md#annotations_id_get) | **GET** /annotations/{id} | Your GET endpoint
[**annotations_id_put**](AnnotationsApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an annotation
[**annotations_post**](AnnotationsApi.md#annotations_post) | **POST** /annotations/ | Post Annotation


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
    api_instance = neurostore_sdk.AnnotationsApi(api_client)

    try:
        # Get annotation analyses
        api_response = api_instance.annotation_analyses_get()
        print("The response of AnnotationsApi->annotation_analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotation_analyses_get: %s\n" % e)
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
    api_instance = neurostore_sdk.AnnotationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.annotation_analyses_id_get(id)
        print("The response of AnnotationsApi->annotation_analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotation_analyses_id_get: %s\n" % e)
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
    api_instance = neurostore_sdk.AnnotationsApi(api_client)
    id = 'id_example' # str | 
    note_collection_request = neurostore_sdk.NoteCollectionRequest() # NoteCollectionRequest |  (optional)

    try:
        # Your PUT endpoint
        api_response = api_instance.annotation_analyses_id_put(id, note_collection_request=note_collection_request)
        print("The response of AnnotationsApi->annotation_analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotation_analyses_id_put: %s\n" % e)
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

# **annotations_get**
> AnnotationList annotations_get(studyset_id=studyset_id)

Your GET endpoint

get annotations for an available studyset

### Example

```python
import time
import os
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
    api_instance = neurostore_sdk.AnnotationsApi(api_client)
    studyset_id = 'studyset_id_example' # str | see all annotations connected to this studyset (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.annotations_get(studyset_id=studyset_id)
        print("The response of AnnotationsApi->annotations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_get: %s\n" % e)
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
    api_instance = neurostore_sdk.AnnotationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE an annotation
        api_instance.annotations_id_delete(id)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_id_delete: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnnotationsApi(api_client)
    id = 'id_example' # str | 
    export = True # bool | return endpoint data in consumable/readable format (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.annotations_id_get(id, export=export)
        print("The response of AnnotationsApi->annotations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_id_get: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnnotationsApi(api_client)
    id = 'id_example' # str | 
    annotation_request = neurostore_sdk.AnnotationRequest() # AnnotationRequest |  (optional)

    try:
        # Update an annotation
        api_response = api_instance.annotations_id_put(id, annotation_request=annotation_request)
        print("The response of AnnotationsApi->annotations_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_id_put: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.AnnotationsApi(api_client)
    source = 'neurostore' # str | the source of the resource you would like to filter/copy from (optional) (default to 'neurostore')
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    annotation_request = neurostore_sdk.AnnotationRequest() # AnnotationRequest |  (optional)

    try:
        # Post Annotation
        api_response = api_instance.annotations_post(source=source, source_id=source_id, annotation_request=annotation_request)
        print("The response of AnnotationsApi->annotations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to &#39;neurostore&#39;]
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

