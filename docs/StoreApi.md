# neurostore_sdk.StoreApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyses_get**](StoreApi.md#analyses_get) | **GET** /analyses/ | GET list of analyses
[**analyses_id_delete**](StoreApi.md#analyses_id_delete) | **DELETE** /analyses/{id} | DELETE an analysis
[**analyses_id_get**](StoreApi.md#analyses_id_get) | **GET** /analyses/{id} | GET an analysis
[**analyses_id_put**](StoreApi.md#analyses_id_put) | **PUT** /analyses/{id} | PUT/update an analysis
[**analyses_post**](StoreApi.md#analyses_post) | **POST** /analyses/ | POST/create an analysis
[**annotation_analyses_get**](StoreApi.md#annotation_analyses_get) | **GET** /annotation-analyses/ | Get annotation analyses
[**annotation_analyses_id_get**](StoreApi.md#annotation_analyses_id_get) | **GET** /annotation-analyses/{id} | Your GET endpoint
[**annotation_analyses_id_put**](StoreApi.md#annotation_analyses_id_put) | **PUT** /annotation-analyses/{id} | Your PUT endpoint
[**annotation_analyses_post**](StoreApi.md#annotation_analyses_post) | **POST** /annotation-analyses/ | Your POST endpoint
[**annotations_get**](StoreApi.md#annotations_get) | **GET** /annotations/ | Your GET endpoint
[**annotations_id_delete**](StoreApi.md#annotations_id_delete) | **DELETE** /annotations/{id} | DELETE an annotation
[**annotations_id_get**](StoreApi.md#annotations_id_get) | **GET** /annotations/{id} | Your GET endpoint
[**annotations_id_put**](StoreApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an annotation
[**annotations_post**](StoreApi.md#annotations_post) | **POST** /annotations/ | Post Annotation
[**base_studies_get**](StoreApi.md#base_studies_get) | **GET** /base-studies/ | 
[**base_studies_id_get**](StoreApi.md#base_studies_id_get) | **GET** /base-studies/{id} | Your GET endpoint
[**base_studies_id_put**](StoreApi.md#base_studies_id_put) | **PUT** /base-studies/{id} | 
[**base_studies_post**](StoreApi.md#base_studies_post) | **POST** /base-studies/ | 
[**conditions_get**](StoreApi.md#conditions_get) | **GET** /conditions/ | GET Conditions
[**conditions_id_delete**](StoreApi.md#conditions_id_delete) | **DELETE** /conditions/{id} | DELETE a condition
[**conditions_id_get**](StoreApi.md#conditions_id_get) | **GET** /conditions/{id} | GET a condition
[**conditions_id_put**](StoreApi.md#conditions_id_put) | **PUT** /conditions/{id} | PUT/update a condition
[**conditions_post**](StoreApi.md#conditions_post) | **POST** /conditions/ | POST/Create a condition
[**images_get**](StoreApi.md#images_get) | **GET** /images/ | GET a list of images
[**images_id_delete**](StoreApi.md#images_id_delete) | **DELETE** /images/{id} | DELETE an image
[**images_id_get**](StoreApi.md#images_id_get) | **GET** /images/{id} | GET an image
[**images_id_put**](StoreApi.md#images_id_put) | **PUT** /images/{id} | PUT/update an image
[**images_post**](StoreApi.md#images_post) | **POST** /images/ | POST/create an image
[**pipeline_configs_get**](StoreApi.md#pipeline_configs_get) | **GET** /pipeline-configs/ | GET a list of pipeline configs
[**pipeline_configs_id_delete**](StoreApi.md#pipeline_configs_id_delete) | **DELETE** /pipeline-configs/{id} | DELETE a pipeline config by ID
[**pipeline_configs_id_get**](StoreApi.md#pipeline_configs_id_get) | **GET** /pipeline-configs/{id} | GET a pipeline config by ID
[**pipeline_configs_id_put**](StoreApi.md#pipeline_configs_id_put) | **PUT** /pipeline-configs/{id} | PUT/update a pipeline config by ID
[**pipeline_configs_post**](StoreApi.md#pipeline_configs_post) | **POST** /pipeline-configs/ | POST/create a pipeline config
[**pipeline_embeddings_get**](StoreApi.md#pipeline_embeddings_get) | **GET** /pipeline-embeddings/ | List pipeline embeddings
[**pipeline_embeddings_id_get**](StoreApi.md#pipeline_embeddings_id_get) | **GET** /pipeline-embeddings/{id} | Get a pipeline embedding by id
[**pipeline_study_results_get**](StoreApi.md#pipeline_study_results_get) | **GET** /pipeline-study-results/ | GET a list of pipeline run results
[**pipeline_study_results_pipeline_study_result_id_delete**](StoreApi.md#pipeline_study_results_pipeline_study_result_id_delete) | **DELETE** /pipeline-study-results/{pipeline_study_result_id} | DELETE a pipeline run result by ID
[**pipeline_study_results_pipeline_study_result_id_get**](StoreApi.md#pipeline_study_results_pipeline_study_result_id_get) | **GET** /pipeline-study-results/{pipeline_study_result_id} | GET a pipeline run result by ID
[**pipeline_study_results_pipeline_study_result_id_put**](StoreApi.md#pipeline_study_results_pipeline_study_result_id_put) | **PUT** /pipeline-study-results/{pipeline_study_result_id} | PUT/update a pipeline run result by ID
[**pipeline_study_results_post**](StoreApi.md#pipeline_study_results_post) | **POST** /pipeline-study-results/ | POST/create a pipeline run result
[**pipelines_get**](StoreApi.md#pipelines_get) | **GET** /pipelines/ | GET a list of pipelines
[**pipelines_id_delete**](StoreApi.md#pipelines_id_delete) | **DELETE** /pipelines/{id} | DELETE a pipeline by ID
[**pipelines_id_get**](StoreApi.md#pipelines_id_get) | **GET** /pipelines/{id} | GET a pipeline by ID
[**pipelines_id_put**](StoreApi.md#pipelines_id_put) | **PUT** /pipelines/{id} | PUT/update a pipeline by ID
[**pipelines_post**](StoreApi.md#pipelines_post) | **POST** /pipelines/ | POST/create a pipeline
[**points_get**](StoreApi.md#points_get) | **GET** /points/ | Get Points
[**points_id_delete**](StoreApi.md#points_id_delete) | **DELETE** /points/{id} | DELETE a point
[**points_id_get**](StoreApi.md#points_id_get) | **GET** /points/{id} | GET a point
[**points_id_put**](StoreApi.md#points_id_put) | **PUT** /points/{id} | PUT/update a point
[**points_post**](StoreApi.md#points_post) | **POST** /points/ | POST Points
[**studies_get**](StoreApi.md#studies_get) | **GET** /studies/ | GET a list of studies
[**studies_id_delete**](StoreApi.md#studies_id_delete) | **DELETE** /studies/{id} | DELETE a study
[**studies_id_get**](StoreApi.md#studies_id_get) | **GET** /studies/{id} | GET a study
[**studies_id_put**](StoreApi.md#studies_id_put) | **PUT** /studies/{id} | PUT/update a study
[**studies_post**](StoreApi.md#studies_post) | **POST** /studies/ | POST/create a study
[**studysets_get**](StoreApi.md#studysets_get) | **GET** /studysets/ | GET a list of studysets
[**studysets_id_delete**](StoreApi.md#studysets_id_delete) | **DELETE** /studysets/{id} | DELETE a studyset
[**studysets_id_get**](StoreApi.md#studysets_id_get) | **GET** /studysets/{id} | GET a studyset
[**studysets_id_put**](StoreApi.md#studysets_id_put) | **PUT** /studysets/{id} | PUT/update a studyset
[**studysets_post**](StoreApi.md#studysets_post) | **POST** /studysets/ | POST/create a studyset
[**tables_get**](StoreApi.md#tables_get) | **GET** /tables/ | GET list of tables
[**tables_id_delete**](StoreApi.md#tables_id_delete) | **DELETE** /tables/{id} | DELETE a table
[**tables_id_get**](StoreApi.md#tables_id_get) | **GET** /tables/{id} | GET a table
[**tables_id_put**](StoreApi.md#tables_id_put) | **PUT** /tables/{id} | PUT/update a table
[**tables_post**](StoreApi.md#tables_post) | **POST** /tables/ | POST/create a table
[**users_get**](StoreApi.md#users_get) | **GET** /users/ | Your GET endpoint
[**users_id_get**](StoreApi.md#users_id_get) | **GET** /users/{id} | Individual User Profile
[**users_id_put**](StoreApi.md#users_id_put) | **PUT** /users/{id} | Update Individual Profile
[**users_post**](StoreApi.md#users_post) | **POST** /users/ | 


# **analyses_get**
> AnalysisList analyses_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, study=study, name=name, nested=nested)

GET list of analyses

List all analyses performed across studies.

### Example


```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    study = 'study_example' # str | Filter tables by study id (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET list of analyses
        api_response = api_instance.analyses_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, study=study, name=name, nested=nested)
        print("The response of StoreApi->analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **study** | **str**| Filter tables by study id | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE an analysis
        api_instance.analyses_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_id_delete: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET an analysis
        api_response = api_instance.analyses_id_get(id, nested=nested)
        print("The response of StoreApi->analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_id_get: %s\n" % e)
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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_id_put**
> AnalysisReturn analyses_id_put(id, analysis_request=analysis_request)

PUT/update an analysis

Update an existing analysis.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    analysis_request = neurostore_sdk.AnalysisRequest() # AnalysisRequest |  (optional)

    try:
        # PUT/update an analysis
        api_response = api_instance.analyses_id_put(id, analysis_request=analysis_request)
        print("The response of StoreApi->analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_id_put: %s\n" % e)
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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyses_post**
> AnalysisReturn analyses_post(analysis_request=analysis_request)

POST/create an analysis

create an analysis

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    analysis_request = neurostore_sdk.AnalysisRequest() # AnalysisRequest |  (optional)

    try:
        # POST/create an analysis
        api_response = api_instance.analyses_post(analysis_request=analysis_request)
        print("The response of StoreApi->analyses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->analyses_post: %s\n" % e)
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
> NoteCollectionList annotation_analyses_get(paginate=paginate)

Get annotation analyses

### Example


```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)

    try:
        # Get annotation analyses
        api_response = api_instance.annotation_analyses_get(paginate=paginate)
        print("The response of StoreApi->annotation_analyses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotation_analyses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # Your GET endpoint
        api_response = api_instance.annotation_analyses_id_get(id)
        print("The response of StoreApi->annotation_analyses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotation_analyses_id_get: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    note_collection_request = neurostore_sdk.NoteCollectionRequest() # NoteCollectionRequest |  (optional)

    try:
        # Your PUT endpoint
        api_response = api_instance.annotation_analyses_id_put(id, note_collection_request=note_collection_request)
        print("The response of StoreApi->annotation_analyses_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotation_analyses_id_put: %s\n" % e)
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

This endpoint does not allow for creation, only modification of existing annotation-analyses.
If you wish to create an annotation-analysis, post to the annotations endpoint and/or add the analysis
to the appropriate study in the studyset, and the annotation-analysis will be created automatically. 

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    note_collection_request = [neurostore_sdk.NoteCollectionRequest()] # List[NoteCollectionRequest] |  (optional)

    try:
        # Your POST endpoint
        api_response = api_instance.annotation_analyses_post(note_collection_request=note_collection_request)
        print("The response of StoreApi->annotation_analyses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotation_analyses_post: %s\n" % e)
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

# **annotations_get**
> AnnotationList annotations_get(studyset_id=studyset_id, paginate=paginate)

Your GET endpoint

get annotations for an available studyset

### Example


```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    studyset_id = 'studyset_id_example' # str | see all annotations connected to this studyset (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)

    try:
        # Your GET endpoint
        api_response = api_instance.annotations_get(studyset_id=studyset_id, paginate=paginate)
        print("The response of StoreApi->annotations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studyset_id** | **str**| see all annotations connected to this studyset | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE an annotation
        api_instance.annotations_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_id_delete: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    export = True # bool | return endpoint data in consumable/readable format (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.annotations_id_get(id, export=export)
        print("The response of StoreApi->annotations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_id_get: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    annotation_request = neurostore_sdk.AnnotationRequest() # AnnotationRequest |  (optional)

    try:
        # Update an annotation
        api_response = api_instance.annotations_id_put(id, annotation_request=annotation_request)
        print("The response of StoreApi->annotations_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_id_put: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    annotation_request = neurostore_sdk.AnnotationRequest() # AnnotationRequest |  (optional)

    try:
        # Post Annotation
        api_response = api_instance.annotations_post(source=source, source_id=source_id, annotation_request=annotation_request)
        print("The response of StoreApi->annotations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->annotations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
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

# **base_studies_get**
> BaseStudyList base_studies_get(nested=nested, year_min=year_min, x=x, y=y, z=z, radius=radius, year_max=year_max, feature_filter=feature_filter, pipeline_config=pipeline_config, feature_display=feature_display, semantic_search=semantic_search, pipeline_config_id=pipeline_config_id, distance_threshold=distance_threshold, overall_cap=overall_cap, feature_flatten=feature_flatten, search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, map_type=map_type, is_oa=is_oa, publication=publication, pmid=pmid, doi=doi, neurovault_id=neurovault_id, flat=flat, info=info, paginate=paginate)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.base_study_list import BaseStudyList
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    year_min = 56 # int | Minimum publication year (inclusive) for study search (optional)
    x = 10 # float | X coordinate for spatial query (requires y, z, and radius) (optional)
    y = 20 # float | Y coordinate for spatial query (requires x, z, and radius) (optional)
    z = 30 # float | Z coordinate for spatial query (requires x, y, and radius) (optional)
    radius = 6 # float | Radius for spatial query (requires x, y, and z) (optional)
    year_max = 2020 # int | Maximum publication year (inclusive) for study search (optional)
    feature_filter = ['feature_filter_example'] # List[str] | Filter studies by feature content. Format: \"PipelineName[:version]:field_path=value\". Examples:   - \"TestPipeline:1.0.0:predictions.age_mean>20\" (specific version)   - \"TestPipeline:groups.diagnosis=ADHD\" (latest version)  Field path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    pipeline_config = ['pipeline_config_example'] # List[str] | Filter studies by pipeline config content. Format: \"PipelineName[:version]:config_path=value\". Examples:   - \"TestPipeline:1.0.0:settings.min_age=20\" (specific version)   - \"TestPipeline:model.type=linear\" (latest version)  Config path supports array notation with [], regex search with ~, and comparisons with =, >, <, >=, <=.  (optional)
    feature_display = 'feature_display_example' # str | display features from pipelines (optional)
    semantic_search = 'semantic_search_example' # str | Semantic search query string (optional)
    pipeline_config_id = 'pipeline_config_id_example' # str | Pipeline configuration identifier to filter studies (optional)
    distance_threshold = 0.5 # float | Distance threshold for semantic search (default 0.5) (optional)
    overall_cap = 3000 # int | Maximum number of overall results to return (default 3000) (optional)
    feature_flatten = True # bool |  (optional)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    authors = 'authors_example' # str | search authors (optional)
    level = group # str | select between studies with group results or meta results (optional) (default to group)
    data_type = 'data_type_example' # str | whether searching for studies that contain coordinates, images, or both (optional)
    map_type = 'map_type_example' # str | filter by stored map-type flags (optional)
    is_oa = True # bool |  (optional)
    publication = 'publication_example' # str | search for papers from a particular journal (optional)
    pmid = 'pmid_example' # str | search for particular pmid (optional)
    doi = 'doi_example' # str | search for study with specific doi (optional)
    neurovault_id = 'neurovault_id_example' # str | search for study with specific neurovault id (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)
    info = True # bool | show additional for endpoint-object relationships without being fully nested. Incompatible with nested (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)

    try:
        # 
        api_response = api_instance.base_studies_get(nested=nested, year_min=year_min, x=x, y=y, z=z, radius=radius, year_max=year_max, feature_filter=feature_filter, pipeline_config=pipeline_config, feature_display=feature_display, semantic_search=semantic_search, pipeline_config_id=pipeline_config_id, distance_threshold=distance_threshold, overall_cap=overall_cap, feature_flatten=feature_flatten, search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, map_type=map_type, is_oa=is_oa, publication=publication, pmid=pmid, doi=doi, neurovault_id=neurovault_id, flat=flat, info=info, paginate=paginate)
        print("The response of StoreApi->base_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->base_studies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **year_min** | **int**| Minimum publication year (inclusive) for study search | [optional] 
 **x** | **float**| X coordinate for spatial query (requires y, z, and radius) | [optional] 
 **y** | **float**| Y coordinate for spatial query (requires x, z, and radius) | [optional] 
 **z** | **float**| Z coordinate for spatial query (requires x, y, and radius) | [optional] 
 **radius** | **float**| Radius for spatial query (requires x, y, and z) | [optional] 
 **year_max** | **int**| Maximum publication year (inclusive) for study search | [optional] 
 **feature_filter** | [**List[str]**](str.md)| Filter studies by feature content. Format: \&quot;PipelineName[:version]:field_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:predictions.age_mean&gt;20\&quot; (specific version)   - \&quot;TestPipeline:groups.diagnosis&#x3D;ADHD\&quot; (latest version)  Field path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **pipeline_config** | [**List[str]**](str.md)| Filter studies by pipeline config content. Format: \&quot;PipelineName[:version]:config_path&#x3D;value\&quot;. Examples:   - \&quot;TestPipeline:1.0.0:settings.min_age&#x3D;20\&quot; (specific version)   - \&quot;TestPipeline:model.type&#x3D;linear\&quot; (latest version)  Config path supports array notation with [], regex search with ~, and comparisons with &#x3D;, &gt;, &lt;, &gt;&#x3D;, &lt;&#x3D;.  | [optional] 
 **feature_display** | **str**| display features from pipelines | [optional] 
 **semantic_search** | **str**| Semantic search query string | [optional] 
 **pipeline_config_id** | **str**| Pipeline configuration identifier to filter studies | [optional] 
 **distance_threshold** | **float**| Distance threshold for semantic search (default 0.5) | [optional] 
 **overall_cap** | **int**| Maximum number of overall results to return (default 3000) | [optional] 
 **feature_flatten** | **bool**|  | [optional] 
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **authors** | **str**| search authors | [optional] 
 **level** | **str**| select between studies with group results or meta results | [optional] [default to group]
 **data_type** | **str**| whether searching for studies that contain coordinates, images, or both | [optional] 
 **map_type** | **str**| filter by stored map-type flags | [optional] 
 **is_oa** | **bool**|  | [optional] 
 **publication** | **str**| search for papers from a particular journal | [optional] 
 **pmid** | **str**| search for particular pmid | [optional] 
 **doi** | **str**| search for study with specific doi | [optional] 
 **neurovault_id** | **str**| search for study with specific neurovault id | [optional] 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 
 **info** | **bool**| show additional for endpoint-object relationships without being fully nested. Incompatible with nested | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]

### Return type

[**BaseStudyList**](BaseStudyList.md)

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

# **base_studies_id_get**
> BaseStudyReturn base_studies_id_get(id, flat=flat, info=info, nested=nested)

Your GET endpoint

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.base_study_return import BaseStudyReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)
    info = True # bool | show additional for endpoint-object relationships without being fully nested. Incompatible with nested (optional)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.base_studies_id_get(id, flat=flat, info=info, nested=nested)
        print("The response of StoreApi->base_studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->base_studies_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 
 **info** | **bool**| show additional for endpoint-object relationships without being fully nested. Incompatible with nested | [optional] 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 

### Return type

[**BaseStudyReturn**](BaseStudyReturn.md)

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

# **base_studies_id_put**
> BaseStudyReturn base_studies_id_put(id, base_study=base_study)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.base_study import BaseStudy
from neurostore_sdk.models.base_study_return import BaseStudyReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    base_study = neurostore_sdk.BaseStudy() # BaseStudy |  (optional)

    try:
        # 
        api_response = api_instance.base_studies_id_put(id, base_study=base_study)
        print("The response of StoreApi->base_studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->base_studies_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **base_study** | [**BaseStudy**](BaseStudy.md)|  | [optional] 

### Return type

[**BaseStudyReturn**](BaseStudyReturn.md)

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

# **base_studies_post**
> BaseStudiesPost200Response base_studies_post(base_studies_post_request=base_studies_post_request)



### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.base_studies_post200_response import BaseStudiesPost200Response
from neurostore_sdk.models.base_studies_post_request import BaseStudiesPostRequest
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    base_studies_post_request = neurostore_sdk.BaseStudiesPostRequest() # BaseStudiesPostRequest |  (optional)

    try:
        # 
        api_response = api_instance.base_studies_post(base_studies_post_request=base_studies_post_request)
        print("The response of StoreApi->base_studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->base_studies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_studies_post_request** | [**BaseStudiesPostRequest**](BaseStudiesPostRequest.md)|  | [optional] 

### Return type

[**BaseStudiesPost200Response**](BaseStudiesPost200Response.md)

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

# **conditions_get**
> ConditionList conditions_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, name=name, description=description)

GET Conditions

Get all conditions

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.condition_list import ConditionList
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)

    try:
        # GET Conditions
        api_response = api_instance.conditions_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, name=name, description=description)
        print("The response of StoreApi->conditions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 

### Return type

[**ConditionList**](ConditionList.md)

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

# **conditions_id_delete**
> conditions_id_delete(id)

DELETE a condition

delete a condition

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a condition
        api_instance.conditions_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_id_delete: %s\n" % e)
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

# **conditions_id_get**
> ConditionReturn conditions_id_get(id)

GET a condition

Retrieve a condition (e.g., 2-back) that can be used in contrasts (e.g., 2-back - 1-back)

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.condition_return import ConditionReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET a condition
        api_response = api_instance.conditions_id_get(id)
        print("The response of StoreApi->conditions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConditionReturn**](ConditionReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conditions_id_put**
> ConditionReturn conditions_id_put(id, condition_request=condition_request)

PUT/update a condition

update a condition

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.condition_request import ConditionRequest
from neurostore_sdk.models.condition_return import ConditionReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    condition_request = neurostore_sdk.ConditionRequest() # ConditionRequest |  (optional)

    try:
        # PUT/update a condition
        api_response = api_instance.conditions_id_put(id, condition_request=condition_request)
        print("The response of StoreApi->conditions_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **condition_request** | [**ConditionRequest**](ConditionRequest.md)|  | [optional] 

### Return type

[**ConditionReturn**](ConditionReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conditions_post**
> ConditionReturn conditions_post(condition_request=condition_request)

POST/Create a condition

Create a condition

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.condition_request import ConditionRequest
from neurostore_sdk.models.condition_return import ConditionReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    condition_request = neurostore_sdk.ConditionRequest() # ConditionRequest |  (optional)

    try:
        # POST/Create a condition
        api_response = api_instance.conditions_post(condition_request=condition_request)
        print("The response of StoreApi->conditions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->conditions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **condition_request** | [**ConditionRequest**](ConditionRequest.md)|  | [optional] 

### Return type

[**ConditionReturn**](ConditionReturn.md)

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

# **images_get**
> ImageList images_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, filename=filename, analysis_name=analysis_name, value_type=value_type, space=space)

GET a list of images

Retrieve and list images.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.image_list import ImageList
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    filename = 'filename_example' # str | search filename field (optional)
    analysis_name = 'analysis_name_example' # str | search analysis_name field (optional)
    value_type = 'value_type_example' # str | search value_type field (optional)
    space = 'space_example' # str | search space field (optional)

    try:
        # GET a list of images
        api_response = api_instance.images_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, filename=filename, analysis_name=analysis_name, value_type=value_type, space=space)
        print("The response of StoreApi->images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **filename** | **str**| search filename field | [optional] 
 **analysis_name** | **str**| search analysis_name field | [optional] 
 **value_type** | **str**| search value_type field | [optional] 
 **space** | **str**| search space field | [optional] 

### Return type

[**ImageList**](ImageList.md)

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

# **images_id_delete**
> images_id_delete(id)

DELETE an image

delete an image

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE an image
        api_instance.images_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->images_id_delete: %s\n" % e)
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

# **images_id_get**
> ImageReturn images_id_get(id)

GET an image

Retrieve information about a particular image from an analysis.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.image_return import ImageReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET an image
        api_response = api_instance.images_id_get(id)
        print("The response of StoreApi->images_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->images_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ImageReturn**](ImageReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_id_put**
> ImageReturn images_id_put(id, image_request=image_request)

PUT/update an image

Update a specific image.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.image_request import ImageRequest
from neurostore_sdk.models.image_return import ImageReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    image_request = neurostore_sdk.ImageRequest() # ImageRequest |  (optional)

    try:
        # PUT/update an image
        api_response = api_instance.images_id_put(id, image_request=image_request)
        print("The response of StoreApi->images_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->images_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **image_request** | [**ImageRequest**](ImageRequest.md)|  | [optional] 

### Return type

[**ImageReturn**](ImageReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_post**
> ImageReturn images_post(image_request=image_request)

POST/create an image

Create an image

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.image_request import ImageRequest
from neurostore_sdk.models.image_return import ImageReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    image_request = neurostore_sdk.ImageRequest() # ImageRequest |  (optional)

    try:
        # POST/create an image
        api_response = api_instance.images_post(image_request=image_request)
        print("The response of StoreApi->images_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->images_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_request** | [**ImageRequest**](ImageRequest.md)|  | [optional] 

### Return type

[**ImageReturn**](ImageReturn.md)

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

# **pipeline_configs_get**
> PipelineConfigList pipeline_configs_get(pipeline=pipeline, paginate=paginate, has_embeddings=has_embeddings, embedding_dimensions=embedding_dimensions)

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    pipeline = ['pipeline_example'] # List[str] | Filter configs by pipeline name (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    has_embeddings = True # bool | Filter configs as whether they have embeddings saved. (optional)
    embedding_dimensions = 56 # int | Filter configs by number of dimensions in the embeddings. (optional)

    try:
        # GET a list of pipeline configs
        api_response = api_instance.pipeline_configs_get(pipeline=pipeline, paginate=paginate, has_embeddings=has_embeddings, embedding_dimensions=embedding_dimensions)
        print("The response of StoreApi->pipeline_configs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_configs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**List[str]**](str.md)| Filter configs by pipeline name | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **has_embeddings** | **bool**| Filter configs as whether they have embeddings saved. | [optional] 
 **embedding_dimensions** | **int**| Filter configs by number of dimensions in the embeddings. | [optional] 

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a pipeline config by ID
        api_instance.pipeline_configs_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_configs_id_delete: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET a pipeline config by ID
        api_response = api_instance.pipeline_configs_id_get(id)
        print("The response of StoreApi->pipeline_configs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_configs_id_get: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    pipeline_config = neurostore_sdk.PipelineConfig() # PipelineConfig |  (optional)

    try:
        # PUT/update a pipeline config by ID
        api_instance.pipeline_configs_id_put(id, pipeline_config=pipeline_config)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_configs_id_put: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    pipeline_config = neurostore_sdk.PipelineConfig() # PipelineConfig |  (optional)

    try:
        # POST/create a pipeline config
        api_instance.pipeline_configs_post(pipeline_config=pipeline_config)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_configs_post: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)

    try:
        # List pipeline embeddings
        api_response = api_instance.pipeline_embeddings_get(paginate=paginate)
        print("The response of StoreApi->pipeline_embeddings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_embeddings_get: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a pipeline embedding by id
        api_response = api_instance.pipeline_embeddings_id_get(id)
        print("The response of StoreApi->pipeline_embeddings_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_embeddings_id_get: %s\n" % e)
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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = neurostore_sdk.StoreApi(api_client)
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
        print("The response of StoreApi->pipeline_study_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_study_results_get: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    pipeline_study_result_id = 'pipeline_study_result_id_example' # str | 

    try:
        # DELETE a pipeline run result by ID
        api_instance.pipeline_study_results_pipeline_study_result_id_delete(pipeline_study_result_id)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_study_results_pipeline_study_result_id_delete: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    pipeline_study_result_id = 'pipeline_study_result_id_example' # str | 

    try:
        # GET a pipeline run result by ID
        api_response = api_instance.pipeline_study_results_pipeline_study_result_id_get(pipeline_study_result_id)
        print("The response of StoreApi->pipeline_study_results_pipeline_study_result_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_study_results_pipeline_study_result_id_get: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    pipeline_study_result_id = 'pipeline_study_result_id_example' # str | 
    pipeline_study_result = neurostore_sdk.PipelineStudyResult() # PipelineStudyResult |  (optional)

    try:
        # PUT/update a pipeline run result by ID
        api_instance.pipeline_study_results_pipeline_study_result_id_put(pipeline_study_result_id, pipeline_study_result=pipeline_study_result)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_study_results_pipeline_study_result_id_put: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
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
        print("The response of StoreApi->pipeline_study_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipeline_study_results_post: %s\n" % e)
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

# **pipelines_get**
> PipelineList pipelines_get(paginate=paginate)

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)

    try:
        # GET a list of pipelines
        api_response = api_instance.pipelines_get(paginate=paginate)
        print("The response of StoreApi->pipelines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipelines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a pipeline by ID
        api_instance.pipelines_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->pipelines_id_delete: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET a pipeline by ID
        api_response = api_instance.pipelines_id_get(id)
        print("The response of StoreApi->pipelines_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->pipelines_id_get: %s\n" % e)
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    pipeline = neurostore_sdk.Pipeline() # Pipeline |  (optional)

    try:
        # PUT/update a pipeline by ID
        api_instance.pipelines_id_put(id, pipeline=pipeline)
    except Exception as e:
        print("Exception when calling StoreApi->pipelines_id_put: %s\n" % e)
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

* Bearer Authentication (JSON-Web-Token):

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
    api_instance = neurostore_sdk.StoreApi(api_client)
    pipeline = neurostore_sdk.Pipeline() # Pipeline |  (optional)

    try:
        # POST/create a pipeline
        api_instance.pipelines_post(pipeline=pipeline)
    except Exception as e:
        print("Exception when calling StoreApi->pipelines_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**Pipeline**](Pipeline.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized - Authentication required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_get**
> PointList points_get(paginate=paginate)

Get Points

list points in database

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.point_list import PointList
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)

    try:
        # Get Points
        api_response = api_instance.points_get(paginate=paginate)
        print("The response of StoreApi->points_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->points_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]

### Return type

[**PointList**](PointList.md)

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

# **points_id_delete**
> points_id_delete(id)

DELETE a point

delete a point

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a point
        api_instance.points_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->points_id_delete: %s\n" % e)
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

# **points_id_get**
> PointReturn points_id_get(id)

GET a point

Information about a particular MRI coordinate

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.point_return import PointReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET a point
        api_response = api_instance.points_id_get(id)
        print("The response of StoreApi->points_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->points_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PointReturn**](PointReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_id_put**
> PointReturn points_id_put(id, point_request=point_request)

PUT/update a point

Update a particular MRI coordinate.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.point_request import PointRequest
from neurostore_sdk.models.point_return import PointReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    point_request = neurostore_sdk.PointRequest() # PointRequest |  (optional)

    try:
        # PUT/update a point
        api_response = api_instance.points_id_put(id, point_request=point_request)
        print("The response of StoreApi->points_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->points_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **point_request** | [**PointRequest**](PointRequest.md)|  | [optional] 

### Return type

[**PointReturn**](PointReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_post**
> PointReturn points_post(point_request=point_request)

POST Points

add a point to an analysis

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.point_request import PointRequest
from neurostore_sdk.models.point_return import PointReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    point_request = neurostore_sdk.PointRequest() # PointRequest |  (optional)

    try:
        # POST Points
        api_response = api_instance.points_post(point_request=point_request)
        print("The response of StoreApi->points_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->points_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_request** | [**PointRequest**](PointRequest.md)|  | [optional] 

### Return type

[**PointReturn**](PointReturn.md)

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

# **studies_get**
> StudyList studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, nested=nested, name=name, description=description, source_id=source_id, unique=unique, source=source, authors=authors, user_id=user_id, data_type=data_type, map_type=map_type, studyset_owner=studyset_owner, level=level, pmid=pmid, doi=doi, flat=flat)

GET a list of studies

List studies

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.study_list import StudyList
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    unique = None # object | whether to list clones with originals (optional)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    authors = 'authors_example' # str | search authors (optional)
    user_id = 'user_id_example' # str | user id you want to filter by (optional)
    data_type = 'data_type_example' # str | whether searching for studies that contain coordinates, images, or both (optional)
    map_type = 'map_type_example' # str | filter by stored map-type flags (optional)
    studyset_owner = 'studyset_owner_example' # str | for all studies filter which studysets are listed based on who owns the studyset (optional)
    level = group # str | select between studies with group results or meta results (optional) (default to group)
    pmid = 'pmid_example' # str | search for particular pmid (optional)
    doi = 'doi_example' # str | search for study with specific doi (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)

    try:
        # GET a list of studies
        api_response = api_instance.studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, nested=nested, name=name, description=description, source_id=source_id, unique=unique, source=source, authors=authors, user_id=user_id, data_type=data_type, map_type=map_type, studyset_owner=studyset_owner, level=level, pmid=pmid, doi=doi, flat=flat)
        print("The response of StoreApi->studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **unique** | [**object**](.md)| whether to list clones with originals | [optional] 
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **authors** | **str**| search authors | [optional] 
 **user_id** | **str**| user id you want to filter by | [optional] 
 **data_type** | **str**| whether searching for studies that contain coordinates, images, or both | [optional] 
 **map_type** | **str**| filter by stored map-type flags | [optional] 
 **studyset_owner** | **str**| for all studies filter which studysets are listed based on who owns the studyset | [optional] 
 **level** | **str**| select between studies with group results or meta results | [optional] [default to group]
 **pmid** | **str**| search for particular pmid | [optional] 
 **doi** | **str**| search for study with specific doi | [optional] 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 

### Return type

[**StudyList**](StudyList.md)

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

# **studies_id_delete**
> studies_id_delete(id)

DELETE a study

delete a study

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a study
        api_instance.studies_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->studies_id_delete: %s\n" % e)
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

# **studies_id_get**
> StudyReturn studies_id_get(id, nested=nested, studyset_owner=studyset_owner, flat=flat)

GET a study

Get a study.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.study_return import StudyReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    studyset_owner = 'studyset_owner_example' # str | for all studies filter which studysets are listed based on who owns the studyset (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)

    try:
        # GET a study
        api_response = api_instance.studies_id_get(id, nested=nested, studyset_owner=studyset_owner, flat=flat)
        print("The response of StoreApi->studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studies_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **studyset_owner** | **str**| for all studies filter which studysets are listed based on who owns the studyset | [optional] 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 

### Return type

[**StudyReturn**](StudyReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Study Found |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_id_put**
> StudyReturn studies_id_put(id, study_request=study_request)

PUT/update a study

Update a study.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.study_request import StudyRequest
from neurostore_sdk.models.study_return import StudyReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    study_request = neurostore_sdk.StudyRequest() # StudyRequest |  (optional)

    try:
        # PUT/update a study
        api_response = api_instance.studies_id_put(id, study_request=study_request)
        print("The response of StoreApi->studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studies_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **study_request** | [**StudyRequest**](StudyRequest.md)|  | [optional] 

### Return type

[**StudyReturn**](StudyReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_post**
> StudyReturn studies_post(source=source, source_id=source_id, study_request=study_request)

POST/create a study

Create a study

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.study_request import StudyRequest
from neurostore_sdk.models.study_return import StudyReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    study_request = neurostore_sdk.StudyRequest() # StudyRequest |  (optional)

    try:
        # POST/create a study
        api_response = api_instance.studies_post(source=source, source_id=source_id, study_request=study_request)
        print("The response of StoreApi->studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **study_request** | [**StudyRequest**](StudyRequest.md)|  | [optional] 

### Return type

[**StudyReturn**](StudyReturn.md)

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

# **studysets_get**
> StudysetList studysets_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, nested=nested, name=name, description=description, source_id=source_id, unique=unique, source=source, authors=authors, user_id=user_id)

GET a list of studysets

Get a list of studysets.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.studyset_list import StudysetList
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    unique = None # object | whether to list clones with originals (optional)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    authors = 'authors_example' # str | search authors (optional)
    user_id = 'user_id_example' # str | user id you want to filter by (optional)

    try:
        # GET a list of studysets
        api_response = api_instance.studysets_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, nested=nested, name=name, description=description, source_id=source_id, unique=unique, source=source, authors=authors, user_id=user_id)
        print("The response of StoreApi->studysets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **unique** | [**object**](.md)| whether to list clones with originals | [optional] 
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **authors** | **str**| search authors | [optional] 
 **user_id** | **str**| user id you want to filter by | [optional] 

### Return type

[**StudysetList**](StudysetList.md)

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

# **studysets_id_delete**
> studysets_id_delete(id)

DELETE a studyset

delete a studyset

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a studyset
        api_instance.studysets_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_id_delete: %s\n" % e)
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

# **studysets_id_get**
> StudysetReturn studysets_id_get(id, nested=nested, summary=summary, gzip=gzip)

GET a studyset

Retrieve the information of a studyset with the matching studyset ID.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)
    summary = True # bool | return a lightweight summary payload with study metadata and per-analysis coordinate counts; incompatible with nested (optional)
    gzip = True # bool | return the content as gzipped content (optional)

    try:
        # GET a studyset
        api_response = api_instance.studysets_id_get(id, nested=nested, summary=summary, gzip=gzip)
        print("The response of StoreApi->studysets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 
 **summary** | **bool**| return a lightweight summary payload with study metadata and per-analysis coordinate counts; incompatible with nested | [optional] 
 **gzip** | **bool**| return the content as gzipped content | [optional] 

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/gzip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | studyset found |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_id_put**
> StudysetReturn studysets_id_put(id, studyset_request=studyset_request)

PUT/update a studyset

Update a studyset.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.studyset_request import StudysetRequest
from neurostore_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    studyset_request = neurostore_sdk.StudysetRequest() # StudysetRequest |  (optional)

    try:
        # PUT/update a studyset
        api_response = api_instance.studysets_id_put(id, studyset_request=studyset_request)
        print("The response of StoreApi->studysets_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **studyset_request** | [**StudysetRequest**](StudysetRequest.md)|  | [optional] 

### Return type

[**StudysetReturn**](StudysetReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studysets_post**
> StudysetReturn studysets_post(source_id=source_id, source=source, copy_annotations=copy_annotations, studyset_request=studyset_request)

POST/create a studyset

Create a studyset. When `source_id` is provided, Neurostore clones an existing studyset owned by any user into a new studyset owned by the caller, copying studies and (by default) annotations.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.studyset_request import StudysetRequest
from neurostore_sdk.models.studyset_return import StudysetReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    source_id = '1234567890ab' # str | id of the resource you are either filtering/copying on (optional)
    source = neurostore # str | the source of the resource you would like to filter/copy from (optional) (default to neurostore)
    copy_annotations = True # bool | When cloning a studyset, copy annotations and their notes when true (default). (optional) (default to True)
    studyset_request = neurostore_sdk.StudysetRequest() # StudysetRequest |  (optional)

    try:
        # POST/create a studyset
        api_response = api_instance.studysets_post(source_id=source_id, source=source, copy_annotations=copy_annotations, studyset_request=studyset_request)
        print("The response of StoreApi->studysets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->studysets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| id of the resource you are either filtering/copying on | [optional] 
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to neurostore]
 **copy_annotations** | **bool**| When cloning a studyset, copy annotations and their notes when true (default). | [optional] [default to True]
 **studyset_request** | [**StudysetRequest**](StudysetRequest.md)|  | [optional] 

### Return type

[**StudysetReturn**](StudysetReturn.md)

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

# **tables_get**
> TableList tables_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, name=name, description=description, nested=nested)

GET list of tables

List all tables across studies.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.table_list import TableList
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    paginate = True # bool | whether to paginate results (true) or return all results at once (false) (optional) (default to True)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET list of tables
        api_response = api_instance.tables_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, paginate=paginate, name=name, description=description, nested=nested)
        print("The response of StoreApi->tables_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->tables_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **paginate** | **bool**| whether to paginate results (true) or return all results at once (false) | [optional] [default to True]
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 

### Return type

[**TableList**](TableList.md)

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

# **tables_id_delete**
> tables_id_delete(id)

DELETE a table

delete a table

### Example

* Bearer Authentication (JSON-Web-Token):

```python
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a table
        api_instance.tables_id_delete(id)
    except Exception as e:
        print("Exception when calling StoreApi->tables_id_delete: %s\n" % e)
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

# **tables_id_get**
> TableReturn tables_id_get(id, nested=nested)

GET a table

Information about a specific table.

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.table_return import TableReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET a table
        api_response = api_instance.tables_id_get(id, nested=nested)
        print("The response of StoreApi->tables_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->tables_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional] 

### Return type

[**TableReturn**](TableReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tables_id_put**
> TableReturn tables_id_put(id, table_request=table_request)

PUT/update a table

update a table

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.table_request import TableRequest
from neurostore_sdk.models.table_return import TableReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    table_request = neurostore_sdk.TableRequest() # TableRequest |  (optional)

    try:
        # PUT/update a table
        api_response = api_instance.tables_id_put(id, table_request=table_request)
        print("The response of StoreApi->tables_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->tables_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **table_request** | [**TableRequest**](TableRequest.md)|  | [optional] 

### Return type

[**TableReturn**](TableReturn.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tables_post**
> TableReturn tables_post(table_request=table_request)

POST/create a table

create a table

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.table_request import TableRequest
from neurostore_sdk.models.table_return import TableReturn
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    table_request = neurostore_sdk.TableRequest() # TableRequest |  (optional)

    try:
        # POST/create a table
        api_response = api_instance.tables_post(table_request=table_request)
        print("The response of StoreApi->tables_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->tables_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_request** | [**TableRequest**](TableRequest.md)|  | [optional] 

### Return type

[**TableReturn**](TableReturn.md)

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

# **users_get**
> UserList users_get()

Your GET endpoint

get list of users

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.user_list import UserList
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
    api_instance = neurostore_sdk.StoreApi(api_client)

    try:
        # Your GET endpoint
        api_response = api_instance.users_get()
        print("The response of StoreApi->users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserList**](UserList.md)

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

# **users_id_get**
> User users_id_get(id)

Individual User Profile

get an individual user

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.user import User
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 

    try:
        # Individual User Profile
        api_response = api_instance.users_id_get(id)
        print("The response of StoreApi->users_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->users_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**User**](User.md)

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

# **users_id_put**
> User users_id_put(id, user=user)

Update Individual Profile

update an individual user

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.user import User
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    id = 'id_example' # str | 
    user = neurostore_sdk.User() # User |  (optional)

    try:
        # Update Individual Profile
        api_response = api_instance.users_id_put(id, user=user)
        print("The response of StoreApi->users_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->users_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

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

# **users_post**
> User users_post(user=user)



create a user

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.user import User
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
    api_instance = neurostore_sdk.StoreApi(api_client)
    user = neurostore_sdk.User() # User |  (optional)

    try:
        # 
        api_response = api_instance.users_post(user=user)
        print("The response of StoreApi->users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoreApi->users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

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

