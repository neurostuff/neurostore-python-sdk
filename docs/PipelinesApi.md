# neurostore_sdk.PipelinesApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipelines_get**](PipelinesApi.md#pipelines_get) | **GET** /pipelines/ | GET a list of pipelines
[**pipelines_id_delete**](PipelinesApi.md#pipelines_id_delete) | **DELETE** /pipelines/{id} | DELETE a pipeline by ID
[**pipelines_id_get**](PipelinesApi.md#pipelines_id_get) | **GET** /pipelines/{id} | GET a pipeline by ID
[**pipelines_id_put**](PipelinesApi.md#pipelines_id_put) | **PUT** /pipelines/{id} | PUT/update a pipeline by ID
[**pipelines_post**](PipelinesApi.md#pipelines_post) | **POST** /pipelines/ | POST/create a pipeline


# **pipelines_get**
> PipelineList pipelines_get()

GET a list of pipelines

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_list import PipelineList
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
    api_instance = neurostore_sdk.PipelinesApi(api_client)

    try:
        # GET a list of pipelines
        api_response = api_instance.pipelines_get()
        print("The response of PipelinesApi->pipelines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PipelineList**](PipelineList.md)

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

# **pipelines_id_delete**
> pipelines_id_delete(id)

DELETE a pipeline by ID

### Example


```python
import neurostore_sdk
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
    api_instance = neurostore_sdk.PipelinesApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a pipeline by ID
        api_instance.pipelines_id_delete(id)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_id_get**
> Pipeline pipelines_id_get(id)

GET a pipeline by ID

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline import Pipeline
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
    api_instance = neurostore_sdk.PipelinesApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET a pipeline by ID
        api_response = api_instance.pipelines_id_get(id)
        print("The response of PipelinesApi->pipelines_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Pipeline**](Pipeline.md)

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

# **pipelines_id_put**
> pipelines_id_put(id, pipeline=pipeline)

PUT/update a pipeline by ID

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline import Pipeline
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
    api_instance = neurostore_sdk.PipelinesApi(api_client)
    id = 'id_example' # str | 
    pipeline = neurostore_sdk.Pipeline() # Pipeline |  (optional)

    try:
        # PUT/update a pipeline by ID
        api_instance.pipelines_id_put(id, pipeline=pipeline)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **pipeline** | [**Pipeline**](Pipeline.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_post**
> pipelines_post(pipeline=pipeline)

POST/create a pipeline

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline import Pipeline
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
    api_instance = neurostore_sdk.PipelinesApi(api_client)
    pipeline = neurostore_sdk.Pipeline() # Pipeline |  (optional)

    try:
        # POST/create a pipeline
        api_instance.pipelines_post(pipeline=pipeline)
    except Exception as e:
        print("Exception when calling PipelinesApi->pipelines_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**Pipeline**](Pipeline.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

