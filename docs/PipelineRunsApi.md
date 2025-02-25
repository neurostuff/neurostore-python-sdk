# neurostore_sdk.PipelineRunsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_runs_get**](PipelineRunsApi.md#pipeline_runs_get) | **GET** /pipeline-runs/ | GET a list of pipeline runs
[**pipeline_runs_pipeline_run_id_delete**](PipelineRunsApi.md#pipeline_runs_pipeline_run_id_delete) | **DELETE** /pipeline-runs/{pipeline_run_id} | DELETE a pipeline run by ID
[**pipeline_runs_pipeline_run_id_get**](PipelineRunsApi.md#pipeline_runs_pipeline_run_id_get) | **GET** /pipeline-runs/{pipeline_run_id} | GET a pipeline run by ID
[**pipeline_runs_pipeline_run_id_put**](PipelineRunsApi.md#pipeline_runs_pipeline_run_id_put) | **PUT** /pipeline-runs/{pipeline_run_id} | PUT/update a pipeline run by ID
[**pipeline_runs_post**](PipelineRunsApi.md#pipeline_runs_post) | **POST** /pipeline-runs/ | POST/create a pipeline run


# **pipeline_runs_get**
> PipelineRunList pipeline_runs_get()

GET a list of pipeline runs

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_list import PipelineRunList
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
    api_instance = neurostore_sdk.PipelineRunsApi(api_client)

    try:
        # GET a list of pipeline runs
        api_response = api_instance.pipeline_runs_get()
        print("The response of PipelineRunsApi->pipeline_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineRunsApi->pipeline_runs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PipelineRunList**](PipelineRunList.md)

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

# **pipeline_runs_pipeline_run_id_delete**
> pipeline_runs_pipeline_run_id_delete(pipeline_run_id)

DELETE a pipeline run by ID

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
    api_instance = neurostore_sdk.PipelineRunsApi(api_client)
    pipeline_run_id = 'pipeline_run_id_example' # str | 

    try:
        # DELETE a pipeline run by ID
        api_instance.pipeline_runs_pipeline_run_id_delete(pipeline_run_id)
    except Exception as e:
        print("Exception when calling PipelineRunsApi->pipeline_runs_pipeline_run_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_id** | **str**|  | 

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

# **pipeline_runs_pipeline_run_id_get**
> PipelineRun pipeline_runs_pipeline_run_id_get(pipeline_run_id)

GET a pipeline run by ID

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_run import PipelineRun
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
    api_instance = neurostore_sdk.PipelineRunsApi(api_client)
    pipeline_run_id = 'pipeline_run_id_example' # str | 

    try:
        # GET a pipeline run by ID
        api_response = api_instance.pipeline_runs_pipeline_run_id_get(pipeline_run_id)
        print("The response of PipelineRunsApi->pipeline_runs_pipeline_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineRunsApi->pipeline_runs_pipeline_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_id** | **str**|  | 

### Return type

[**PipelineRun**](PipelineRun.md)

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

# **pipeline_runs_pipeline_run_id_put**
> pipeline_runs_pipeline_run_id_put(pipeline_run_id, pipeline_run=pipeline_run)

PUT/update a pipeline run by ID

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_run import PipelineRun
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
    api_instance = neurostore_sdk.PipelineRunsApi(api_client)
    pipeline_run_id = 'pipeline_run_id_example' # str | 
    pipeline_run = neurostore_sdk.PipelineRun() # PipelineRun |  (optional)

    try:
        # PUT/update a pipeline run by ID
        api_instance.pipeline_runs_pipeline_run_id_put(pipeline_run_id, pipeline_run=pipeline_run)
    except Exception as e:
        print("Exception when calling PipelineRunsApi->pipeline_runs_pipeline_run_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_id** | **str**|  | 
 **pipeline_run** | [**PipelineRun**](PipelineRun.md)|  | [optional] 

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

# **pipeline_runs_post**
> pipeline_runs_post(pipeline_run=pipeline_run)

POST/create a pipeline run

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_run import PipelineRun
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
    api_instance = neurostore_sdk.PipelineRunsApi(api_client)
    pipeline_run = neurostore_sdk.PipelineRun() # PipelineRun |  (optional)

    try:
        # POST/create a pipeline run
        api_instance.pipeline_runs_post(pipeline_run=pipeline_run)
    except Exception as e:
        print("Exception when calling PipelineRunsApi->pipeline_runs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run** | [**PipelineRun**](PipelineRun.md)|  | [optional] 

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

