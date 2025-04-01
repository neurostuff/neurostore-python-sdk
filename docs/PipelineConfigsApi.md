# neurostore_sdk.PipelineConfigsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_configs_get**](PipelineConfigsApi.md#pipeline_configs_get) | **GET** /pipeline-configs/ | GET a list of pipeline configs
[**pipeline_configs_id_delete**](PipelineConfigsApi.md#pipeline_configs_id_delete) | **DELETE** /pipeline-configs/{id} | DELETE a pipeline config by ID
[**pipeline_configs_id_get**](PipelineConfigsApi.md#pipeline_configs_id_get) | **GET** /pipeline-configs/{id} | GET a pipeline config by ID
[**pipeline_configs_id_put**](PipelineConfigsApi.md#pipeline_configs_id_put) | **PUT** /pipeline-configs/{id} | PUT/update a pipeline config by ID
[**pipeline_configs_post**](PipelineConfigsApi.md#pipeline_configs_post) | **POST** /pipeline-configs/ | POST/create a pipeline config


# **pipeline_configs_get**
> PipelineConfigList pipeline_configs_get(pipeline=pipeline)

GET a list of pipeline configs

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_config_list import PipelineConfigList
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
    api_instance = neurostore_sdk.PipelineConfigsApi(api_client)
    pipeline = ['pipeline_example'] # List[str] | Filter configs by pipeline name (optional)

    try:
        # GET a list of pipeline configs
        api_response = api_instance.pipeline_configs_get(pipeline=pipeline)
        print("The response of PipelineConfigsApi->pipeline_configs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineConfigsApi->pipeline_configs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**List[str]**](str.md)| Filter configs by pipeline name | [optional] 

### Return type

[**PipelineConfigList**](PipelineConfigList.md)

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

# **pipeline_configs_id_delete**
> pipeline_configs_id_delete(id)

DELETE a pipeline config by ID

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
    api_instance = neurostore_sdk.PipelineConfigsApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a pipeline config by ID
        api_instance.pipeline_configs_id_delete(id)
    except Exception as e:
        print("Exception when calling PipelineConfigsApi->pipeline_configs_id_delete: %s\n" % e)
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

# **pipeline_configs_id_get**
> PipelineConfig pipeline_configs_id_get(id)

GET a pipeline config by ID

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_config import PipelineConfig
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
    api_instance = neurostore_sdk.PipelineConfigsApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET a pipeline config by ID
        api_response = api_instance.pipeline_configs_id_get(id)
        print("The response of PipelineConfigsApi->pipeline_configs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineConfigsApi->pipeline_configs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PipelineConfig**](PipelineConfig.md)

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

# **pipeline_configs_id_put**
> pipeline_configs_id_put(id, pipeline_config=pipeline_config)

PUT/update a pipeline config by ID

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_config import PipelineConfig
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
    api_instance = neurostore_sdk.PipelineConfigsApi(api_client)
    id = 'id_example' # str | 
    pipeline_config = neurostore_sdk.PipelineConfig() # PipelineConfig |  (optional)

    try:
        # PUT/update a pipeline config by ID
        api_instance.pipeline_configs_id_put(id, pipeline_config=pipeline_config)
    except Exception as e:
        print("Exception when calling PipelineConfigsApi->pipeline_configs_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **pipeline_config** | [**PipelineConfig**](PipelineConfig.md)|  | [optional] 

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

# **pipeline_configs_post**
> pipeline_configs_post(pipeline_config=pipeline_config)

POST/create a pipeline config

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_config import PipelineConfig
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
    api_instance = neurostore_sdk.PipelineConfigsApi(api_client)
    pipeline_config = neurostore_sdk.PipelineConfig() # PipelineConfig |  (optional)

    try:
        # POST/create a pipeline config
        api_instance.pipeline_configs_post(pipeline_config=pipeline_config)
    except Exception as e:
        print("Exception when calling PipelineConfigsApi->pipeline_configs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_config** | [**PipelineConfig**](PipelineConfig.md)|  | [optional] 

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

