# neurostore_sdk.PipelineEmbeddingsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_embeddings_get**](PipelineEmbeddingsApi.md#pipeline_embeddings_get) | **GET** /pipeline-embeddings/ | List pipeline embeddings
[**pipeline_embeddings_id_get**](PipelineEmbeddingsApi.md#pipeline_embeddings_id_get) | **GET** /pipeline-embeddings/{id} | Get a pipeline embedding by id


# **pipeline_embeddings_get**
> PipelineEmbeddingList pipeline_embeddings_get(paginate=paginate)

List pipeline embeddings

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_embedding_list import PipelineEmbeddingList
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
    api_instance = neurostore_sdk.PipelineEmbeddingsApi(api_client)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)

    try:
        # List pipeline embeddings
        api_response = api_instance.pipeline_embeddings_get(paginate=paginate)
        print("The response of PipelineEmbeddingsApi->pipeline_embeddings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineEmbeddingsApi->pipeline_embeddings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]

### Return type

[**PipelineEmbeddingList**](PipelineEmbeddingList.md)

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

# **pipeline_embeddings_id_get**
> PipelineEmbedding pipeline_embeddings_id_get(id)

Get a pipeline embedding by id

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_embedding import PipelineEmbedding
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
    api_instance = neurostore_sdk.PipelineEmbeddingsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a pipeline embedding by id
        api_response = api_instance.pipeline_embeddings_id_get(id)
        print("The response of PipelineEmbeddingsApi->pipeline_embeddings_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineEmbeddingsApi->pipeline_embeddings_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PipelineEmbedding**](PipelineEmbedding.md)

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

