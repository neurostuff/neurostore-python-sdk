# neurostore_sdk.PipelineRunResultVotesApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipeline_run_result_votes_get**](PipelineRunResultVotesApi.md#pipeline_run_result_votes_get) | **GET** /pipeline-run-result-votes/ | GET a list of pipeline run result votes
[**pipeline_run_result_votes_pipeline_run_result_vote_id_delete**](PipelineRunResultVotesApi.md#pipeline_run_result_votes_pipeline_run_result_vote_id_delete) | **DELETE** /pipeline-run-result-votes/{pipeline_run_result_vote_id} | DELETE a pipeline run result vote by ID
[**pipeline_run_result_votes_pipeline_run_result_vote_id_get**](PipelineRunResultVotesApi.md#pipeline_run_result_votes_pipeline_run_result_vote_id_get) | **GET** /pipeline-run-result-votes/{pipeline_run_result_vote_id} | GET a pipeline run result vote by ID
[**pipeline_run_result_votes_pipeline_run_result_vote_id_put**](PipelineRunResultVotesApi.md#pipeline_run_result_votes_pipeline_run_result_vote_id_put) | **PUT** /pipeline-run-result-votes/{pipeline_run_result_vote_id} | PUT/update a pipeline run result vote by ID
[**pipeline_run_result_votes_post**](PipelineRunResultVotesApi.md#pipeline_run_result_votes_post) | **POST** /pipeline-run-result-votes/ | POST/create a pipeline run result vote


# **pipeline_run_result_votes_get**
> PipelineRunResultVoteList pipeline_run_result_votes_get()

GET a list of pipeline run result votes

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result_vote_list import PipelineRunResultVoteList
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
    api_instance = neurostore_sdk.PipelineRunResultVotesApi(api_client)

    try:
        # GET a list of pipeline run result votes
        api_response = api_instance.pipeline_run_result_votes_get()
        print("The response of PipelineRunResultVotesApi->pipeline_run_result_votes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineRunResultVotesApi->pipeline_run_result_votes_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PipelineRunResultVoteList**](PipelineRunResultVoteList.md)

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

# **pipeline_run_result_votes_pipeline_run_result_vote_id_delete**
> pipeline_run_result_votes_pipeline_run_result_vote_id_delete(pipeline_run_result_vote_id)

DELETE a pipeline run result vote by ID

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
    api_instance = neurostore_sdk.PipelineRunResultVotesApi(api_client)
    pipeline_run_result_vote_id = 'pipeline_run_result_vote_id_example' # str | 

    try:
        # DELETE a pipeline run result vote by ID
        api_instance.pipeline_run_result_votes_pipeline_run_result_vote_id_delete(pipeline_run_result_vote_id)
    except Exception as e:
        print("Exception when calling PipelineRunResultVotesApi->pipeline_run_result_votes_pipeline_run_result_vote_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_result_vote_id** | **str**|  | 

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

# **pipeline_run_result_votes_pipeline_run_result_vote_id_get**
> PipelineRunResultVote pipeline_run_result_votes_pipeline_run_result_vote_id_get(pipeline_run_result_vote_id)

GET a pipeline run result vote by ID

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result_vote import PipelineRunResultVote
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
    api_instance = neurostore_sdk.PipelineRunResultVotesApi(api_client)
    pipeline_run_result_vote_id = 'pipeline_run_result_vote_id_example' # str | 

    try:
        # GET a pipeline run result vote by ID
        api_response = api_instance.pipeline_run_result_votes_pipeline_run_result_vote_id_get(pipeline_run_result_vote_id)
        print("The response of PipelineRunResultVotesApi->pipeline_run_result_votes_pipeline_run_result_vote_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineRunResultVotesApi->pipeline_run_result_votes_pipeline_run_result_vote_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_result_vote_id** | **str**|  | 

### Return type

[**PipelineRunResultVote**](PipelineRunResultVote.md)

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

# **pipeline_run_result_votes_pipeline_run_result_vote_id_put**
> pipeline_run_result_votes_pipeline_run_result_vote_id_put(pipeline_run_result_vote_id, pipeline_run_result_vote=pipeline_run_result_vote)

PUT/update a pipeline run result vote by ID

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result_vote import PipelineRunResultVote
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
    api_instance = neurostore_sdk.PipelineRunResultVotesApi(api_client)
    pipeline_run_result_vote_id = 'pipeline_run_result_vote_id_example' # str | 
    pipeline_run_result_vote = neurostore_sdk.PipelineRunResultVote() # PipelineRunResultVote |  (optional)

    try:
        # PUT/update a pipeline run result vote by ID
        api_instance.pipeline_run_result_votes_pipeline_run_result_vote_id_put(pipeline_run_result_vote_id, pipeline_run_result_vote=pipeline_run_result_vote)
    except Exception as e:
        print("Exception when calling PipelineRunResultVotesApi->pipeline_run_result_votes_pipeline_run_result_vote_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_result_vote_id** | **str**|  | 
 **pipeline_run_result_vote** | [**PipelineRunResultVote**](PipelineRunResultVote.md)|  | [optional] 

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

# **pipeline_run_result_votes_post**
> pipeline_run_result_votes_post(pipeline_run_result_vote=pipeline_run_result_vote)

POST/create a pipeline run result vote

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.pipeline_run_result_vote import PipelineRunResultVote
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
    api_instance = neurostore_sdk.PipelineRunResultVotesApi(api_client)
    pipeline_run_result_vote = neurostore_sdk.PipelineRunResultVote() # PipelineRunResultVote |  (optional)

    try:
        # POST/create a pipeline run result vote
        api_instance.pipeline_run_result_votes_post(pipeline_run_result_vote=pipeline_run_result_vote)
    except Exception as e:
        print("Exception when calling PipelineRunResultVotesApi->pipeline_run_result_votes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_run_result_vote** | [**PipelineRunResultVote**](PipelineRunResultVote.md)|  | [optional] 

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

