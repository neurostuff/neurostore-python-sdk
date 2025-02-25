# neurostore_sdk.PipelineRunResultsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_run_results_get**](PipelineRunResultsApi.md#pipeline_run_results_get) | **GET** /pipeline-run-results/ | GET a list of pipeline run results
[**pipeline_run_results_pipeline_run_result_id_delete**](PipelineRunResultsApi.md#pipeline_run_results_pipeline_run_result_id_delete) | **DELETE** /pipeline-run-results/{pipeline_run_result_id} | DELETE a pipeline run result by ID
[**pipeline_run_results_pipeline_run_result_id_get**](PipelineRunResultsApi.md#pipeline_run_results_pipeline_run_result_id_get) | **GET** /pipeline-run-results/{pipeline_run_result_id} | GET a pipeline run result by ID
[**pipeline_run_results_pipeline_run_result_id_put**](PipelineRunResultsApi.md#pipeline_run_results_pipeline_run_result_id_put) | **PUT** /pipeline-run-results/{pipeline_run_result_id} | PUT/update a pipeline run result by ID
[**pipeline_run_results_post**](PipelineRunResultsApi.md#pipeline_run_results_post) | **POST** /pipeline-run-results/ | POST/create a pipeline run result


# **pipeline_run_results_get**
> PipelineRunResultList pipeline_run_results_get()

GET a list of pipeline run results

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result_list import PipelineRunResultList
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
    api_instance = neurostore_sdk.PipelineRunResultsApi(api_client)

    try:
        # GET a list of pipeline run results
        api_response = api_instance.pipeline_run_results_get()
        print("The response of PipelineRunResultsApi->pipeline_run_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineRunResultsApi->pipeline_run_results_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PipelineRunResultList**](PipelineRunResultList.md)

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

# **pipeline_run_results_pipeline_run_result_id_delete**
> pipeline_run_results_pipeline_run_result_id_delete(pipeline_run_result_id)

DELETE a pipeline run result by ID

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
    api_instance = neurostore_sdk.PipelineRunResultsApi(api_client)
    pipeline_run_result_id = 'pipeline_run_result_id_example' # str | 

    try:
        # DELETE a pipeline run result by ID
        api_instance.pipeline_run_results_pipeline_run_result_id_delete(pipeline_run_result_id)
    except Exception as e:
        print("Exception when calling PipelineRunResultsApi->pipeline_run_results_pipeline_run_result_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_result_id** | **str**|  | 

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

# **pipeline_run_results_pipeline_run_result_id_get**
> PipelineRunResult pipeline_run_results_pipeline_run_result_id_get(pipeline_run_result_id)

GET a pipeline run result by ID

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result import PipelineRunResult
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
    api_instance = neurostore_sdk.PipelineRunResultsApi(api_client)
    pipeline_run_result_id = 'pipeline_run_result_id_example' # str | 

    try:
        # GET a pipeline run result by ID
        api_response = api_instance.pipeline_run_results_pipeline_run_result_id_get(pipeline_run_result_id)
        print("The response of PipelineRunResultsApi->pipeline_run_results_pipeline_run_result_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineRunResultsApi->pipeline_run_results_pipeline_run_result_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_result_id** | **str**|  | 

### Return type

[**PipelineRunResult**](PipelineRunResult.md)

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

# **pipeline_run_results_pipeline_run_result_id_put**
> pipeline_run_results_pipeline_run_result_id_put(pipeline_run_result_id, pipeline_run_result=pipeline_run_result)

PUT/update a pipeline run result by ID

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result import PipelineRunResult
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
    api_instance = neurostore_sdk.PipelineRunResultsApi(api_client)
    pipeline_run_result_id = 'pipeline_run_result_id_example' # str | 
    pipeline_run_result = neurostore_sdk.PipelineRunResult() # PipelineRunResult |  (optional)

    try:
        # PUT/update a pipeline run result by ID
        api_instance.pipeline_run_results_pipeline_run_result_id_put(pipeline_run_result_id, pipeline_run_result=pipeline_run_result)
    except Exception as e:
        print("Exception when calling PipelineRunResultsApi->pipeline_run_results_pipeline_run_result_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_result_id** | **str**|  | 
 **pipeline_run_result** | [**PipelineRunResult**](PipelineRunResult.md)|  | [optional] 

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

# **pipeline_run_results_post**
> pipeline_run_results_post(pipeline_run_result=pipeline_run_result)

POST/create a pipeline run result

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result import PipelineRunResult
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
    api_instance = neurostore_sdk.PipelineRunResultsApi(api_client)
    pipeline_run_result = neurostore_sdk.PipelineRunResult() # PipelineRunResult |  (optional)

    try:
        # POST/create a pipeline run result
        api_instance.pipeline_run_results_post(pipeline_run_result=pipeline_run_result)
    except Exception as e:
        print("Exception when calling PipelineRunResultsApi->pipeline_run_results_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_result** | [**PipelineRunResult**](PipelineRunResult.md)|  | [optional] 

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

