# neurostore_sdk.PipelineStudyResultsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_study_results_get**](PipelineStudyResultsApi.md#pipeline_study_results_get) | **GET** /pipeline-study-results/ | GET a list of pipeline run results
[**pipeline_study_results_pipeline_study_result_id_delete**](PipelineStudyResultsApi.md#pipeline_study_results_pipeline_study_result_id_delete) | **DELETE** /pipeline-study-results/{pipeline_study_result_id} | DELETE a pipeline run result by ID
[**pipeline_study_results_pipeline_study_result_id_get**](PipelineStudyResultsApi.md#pipeline_study_results_pipeline_study_result_id_get) | **GET** /pipeline-study-results/{pipeline_study_result_id} | GET a pipeline run result by ID
[**pipeline_study_results_pipeline_study_result_id_put**](PipelineStudyResultsApi.md#pipeline_study_results_pipeline_study_result_id_put) | **PUT** /pipeline-study-results/{pipeline_study_result_id} | PUT/update a pipeline run result by ID
[**pipeline_study_results_post**](PipelineStudyResultsApi.md#pipeline_study_results_post) | **POST** /pipeline-study-results/ | POST/create a pipeline run result


# **pipeline_study_results_get**
> PipelineStudyResultList pipeline_study_results_get(feature_filter=feature_filter)

GET a list of pipeline run results

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.pipeline_study_result_list import PipelineStudyResultList
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
    api_instance = neurostore_sdk.PipelineStudyResultsApi(api_client)
    feature_filter = ['feature_filter_example'] # List[str] | Filter results by feature content using jsonpath syntax (optional)

    try:
        # GET a list of pipeline run results
        api_response = api_instance.pipeline_study_results_get(feature_filter=feature_filter)
        print("The response of PipelineStudyResultsApi->pipeline_study_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineStudyResultsApi->pipeline_study_results_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_filter** | [**List[str]**](str.md)| Filter results by feature content using jsonpath syntax | [optional] 

### Return type

[**PipelineStudyResultList**](PipelineStudyResultList.md)

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

# **pipeline_study_results_pipeline_study_result_id_delete**
> pipeline_study_results_pipeline_study_result_id_delete(pipeline_study_result_id)

DELETE a pipeline run result by ID

### Example

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


# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurostore_sdk.PipelineStudyResultsApi(api_client)
    pipeline_study_result_id = 'pipeline_study_result_id_example' # str | 

    try:
        # DELETE a pipeline run result by ID
        api_instance.pipeline_study_results_pipeline_study_result_id_delete(pipeline_study_result_id)
    except Exception as e:
        print("Exception when calling PipelineStudyResultsApi->pipeline_study_results_pipeline_study_result_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_study_result_id** | **str**|  | 

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

# **pipeline_study_results_pipeline_study_result_id_get**
> PipelineStudyResult pipeline_study_results_pipeline_study_result_id_get(pipeline_study_result_id)

GET a pipeline run result by ID

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.pipeline_study_result import PipelineStudyResult
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
    api_instance = neurostore_sdk.PipelineStudyResultsApi(api_client)
    pipeline_study_result_id = 'pipeline_study_result_id_example' # str | 

    try:
        # GET a pipeline run result by ID
        api_response = api_instance.pipeline_study_results_pipeline_study_result_id_get(pipeline_study_result_id)
        print("The response of PipelineStudyResultsApi->pipeline_study_results_pipeline_study_result_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineStudyResultsApi->pipeline_study_results_pipeline_study_result_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_study_result_id** | **str**|  | 

### Return type

[**PipelineStudyResult**](PipelineStudyResult.md)

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

# **pipeline_study_results_pipeline_study_result_id_put**
> pipeline_study_results_pipeline_study_result_id_put(pipeline_study_result_id, pipeline_study_result=pipeline_study_result)

PUT/update a pipeline run result by ID

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.pipeline_study_result import PipelineStudyResult
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
    api_instance = neurostore_sdk.PipelineStudyResultsApi(api_client)
    pipeline_study_result_id = 'pipeline_study_result_id_example' # str | 
    pipeline_study_result = neurostore_sdk.PipelineStudyResult() # PipelineStudyResult |  (optional)

    try:
        # PUT/update a pipeline run result by ID
        api_instance.pipeline_study_results_pipeline_study_result_id_put(pipeline_study_result_id, pipeline_study_result=pipeline_study_result)
    except Exception as e:
        print("Exception when calling PipelineStudyResultsApi->pipeline_study_results_pipeline_study_result_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_study_result_id** | **str**|  | 
 **pipeline_study_result** | [**PipelineStudyResult**](PipelineStudyResult.md)|  | [optional] 

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

# **pipeline_study_results_post**
> pipeline_study_results_post(pipeline_study_result=pipeline_study_result)

POST/create a pipeline run result

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.pipeline_study_result import PipelineStudyResult
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
    api_instance = neurostore_sdk.PipelineStudyResultsApi(api_client)
    pipeline_study_result = neurostore_sdk.PipelineStudyResult() # PipelineStudyResult |  (optional)

    try:
        # POST/create a pipeline run result
        api_instance.pipeline_study_results_post(pipeline_study_result=pipeline_study_result)
    except Exception as e:
        print("Exception when calling PipelineStudyResultsApi->pipeline_study_results_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_study_result** | [**PipelineStudyResult**](PipelineStudyResult.md)|  | [optional] 

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

