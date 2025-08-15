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
> PipelineStudyResultList pipeline_study_results_get(paginate=paginate, feature_filter=feature_filter, feature_flatten=feature_flatten, pipeline_config=pipeline_config, feature_display=feature_display, study_id=study_id, version=version)

GET a list of pipeline run results

### Example


```python
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
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    feature_filter = ['feature_filter_example'] # List[str] | Filter results by feature content. Format: \"PipelineName[:version]:field_path=value\". Examples:   - \"TestPipeline:1.0.0:groups.diagnosis=ADHD\" (specific version)   - \"TestPipeline:groups.diagnosis=ADHD\" (latest version)  Field path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    feature_flatten = True # bool |  (optional)
    pipeline_config = ['pipeline_config_example'] # List[str] | Filter results by pipeline config content. Format: \"PipelineName[:version]:config_path=value\". Examples:   - \"TestPipeline:1.0.0:preprocessing.smoothing=8\" (specific version)   - \"TestPipeline:model.type=linear\" (latest version)  Config path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    feature_display = ['feature_display_example'] # List[str] | Filter results by pipeline name and optionally version. Format: \"pipeline_name[:version]\". Examples:   - \"TestPipeline\" (all results from pipeline)   - \"TestPipeline:1.0.0\" (results from specific version) Multiple values can be provided to get results from multiple pipelines/versions.  (optional)
    study_id = ['study_id_example'] # List[str] | Filter results by base study ID (optional)
    version = 'version_example' # str | Filter results by pipeline config version (optional)

    try:
        # GET a list of pipeline run results
        api_response = api_instance.pipeline_study_results_get(paginate=paginate, feature_filter=feature_filter, feature_flatten=feature_flatten, pipeline_config=pipeline_config, feature_display=feature_display, study_id=study_id, version=version)
        print("The response of PipelineStudyResultsApi->pipeline_study_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineStudyResultsApi->pipeline_study_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **feature_filter** | [**List[str]**](str.md)| Filter results by feature content. Format: \&quot;PipelineName[:version]:field_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:groups.diagnosis&#x3D;ADHD\&quot; (specific version)   - \&quot;TestPipeline:groups.diagnosis&#x3D;ADHD\&quot; (latest version)  Field path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **feature_flatten** | **bool**|  | [optional] 
 **pipeline_config** | [**List[str]**](str.md)| Filter results by pipeline config content. Format: \&quot;PipelineName[:version]:config_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:preprocessing.smoothing&#x3D;8\&quot; (specific version)   - \&quot;TestPipeline:model.type&#x3D;linear\&quot; (latest version)  Config path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **feature_display** | [**List[str]**](str.md)| Filter results by pipeline name and optionally version. Format: \&quot;pipeline_name[:version]\&quot;. Examples:   - \&quot;TestPipeline\&quot; (all results from pipeline)   - \&quot;TestPipeline:1.0.0\&quot; (results from specific version) Multiple values can be provided to get results from multiple pipelines/versions.  | [optional] 
 **study_id** | [**List[str]**](str.md)| Filter results by base study ID | [optional] 
 **version** | **str**| Filter results by pipeline config version | [optional] 

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
> PipelineStudyResultList pipeline_study_results_post(paginate=paginate, feature_filter=feature_filter, feature_flatten=feature_flatten, pipeline_config=pipeline_config, feature_display=feature_display, study_id=study_id, version=version, pipeline_study_result_post=pipeline_study_result_post)

POST/create a pipeline run result

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.pipeline_study_result_list import PipelineStudyResultList
from neurostore_sdk.models.pipeline_study_result_post import PipelineStudyResultPost
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
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    feature_filter = ['feature_filter_example'] # List[str] | Filter results by feature content. Format: \"PipelineName[:version]:field_path=value\". Examples:   - \"TestPipeline:1.0.0:groups.diagnosis=ADHD\" (specific version)   - \"TestPipeline:groups.diagnosis=ADHD\" (latest version)  Field path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    feature_flatten = True # bool |  (optional)
    pipeline_config = ['pipeline_config_example'] # List[str] | Filter results by pipeline config content. Format: \"PipelineName[:version]:config_path=value\". Examples:   - \"TestPipeline:1.0.0:preprocessing.smoothing=8\" (specific version)   - \"TestPipeline:model.type=linear\" (latest version)  Config path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    feature_display = ['feature_display_example'] # List[str] | Filter results by pipeline name and optionally version. Format: \"pipeline_name[:version]\". Examples:   - \"TestPipeline\" (all results from pipeline)   - \"TestPipeline:1.0.0\" (results from specific version) Multiple values can be provided to get results from multiple pipelines/versions.  (optional)
    study_id = ['study_id_example'] # List[str] | Filter results by base study ID (optional)
    version = 'version_example' # str | Filter results by pipeline config version (optional)
    pipeline_study_result_post = neurostore_sdk.PipelineStudyResultPost() # PipelineStudyResultPost |  (optional)

    try:
        # POST/create a pipeline run result
        api_response = api_instance.pipeline_study_results_post(paginate=paginate, feature_filter=feature_filter, feature_flatten=feature_flatten, pipeline_config=pipeline_config, feature_display=feature_display, study_id=study_id, version=version, pipeline_study_result_post=pipeline_study_result_post)
        print("The response of PipelineStudyResultsApi->pipeline_study_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineStudyResultsApi->pipeline_study_results_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **feature_filter** | [**List[str]**](str.md)| Filter results by feature content. Format: \&quot;PipelineName[:version]:field_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:groups.diagnosis&#x3D;ADHD\&quot; (specific version)   - \&quot;TestPipeline:groups.diagnosis&#x3D;ADHD\&quot; (latest version)  Field path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **feature_flatten** | **bool**|  | [optional] 
 **pipeline_config** | [**List[str]**](str.md)| Filter results by pipeline config content. Format: \&quot;PipelineName[:version]:config_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:preprocessing.smoothing&#x3D;8\&quot; (specific version)   - \&quot;TestPipeline:model.type&#x3D;linear\&quot; (latest version)  Config path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **feature_display** | [**List[str]**](str.md)| Filter results by pipeline name and optionally version. Format: \&quot;pipeline_name[:version]\&quot;. Examples:   - \&quot;TestPipeline\&quot; (all results from pipeline)   - \&quot;TestPipeline:1.0.0\&quot; (results from specific version) Multiple values can be provided to get results from multiple pipelines/versions.  | [optional] 
 **study_id** | [**List[str]**](str.md)| Filter results by base study ID | [optional] 
 **version** | **str**| Filter results by pipeline config version | [optional] 
 **pipeline_study_result_post** | [**PipelineStudyResultPost**](PipelineStudyResultPost.md)|  | [optional] 

### Return type

[**PipelineStudyResultList**](PipelineStudyResultList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**200** | OK (search results) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

