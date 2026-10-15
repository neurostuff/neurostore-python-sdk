# neurostore_sdk.ReviewApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**neurostore_resources_review_review_bundles_view_get**](ReviewApi.md#neurostore_resources_review_review_bundles_view_get) | **GET** /review/sources/{id}/bundle | Everything the review app needs to open one paper for the caller
[**neurostore_resources_review_review_export_view_get**](ReviewApi.md#neurostore_resources_review_review_export_view_get) | **GET** /review/reviews/{id}/export | Export one review as a study_schema layout zip
[**neurostore_resources_review_review_exports_view_post**](ReviewApi.md#neurostore_resources_review_review_exports_view_post) | **POST** /review/exports/ | Export the reviews that match the filters as a zip of layout trees
[**neurostore_resources_review_review_imports_view_post**](ReviewApi.md#neurostore_resources_review_review_imports_view_post) | **POST** /review/imports/ | Load the papers of a study_schema layout zip for review
[**neurostore_resources_review_review_ops_view_post**](ReviewApi.md#neurostore_resources_review_review_ops_view_post) | **POST** /review/reviews/{id}/ops | Apply a batch of the owner&#39;s ops to their review
[**neurostore_resources_review_review_sources_view_search**](ReviewApi.md#neurostore_resources_review_review_sources_view_search) | **GET** /review/sources/ | List papers loaded for review, with each reviewer&#39;s progress
[**neurostore_resources_review_reviews_view_get**](ReviewApi.md#neurostore_resources_review_reviews_view_get) | **GET** /review/reviews/{id} | One reviewer&#39;s review of a paper
[**neurostore_resources_review_reviews_view_patch**](ReviewApi.md#neurostore_resources_review_reviews_view_patch) | **PATCH** /review/reviews/{id} | Submit, reopen, or mark as the reference review
[**neurostore_resources_review_source_reviews_view_put**](ReviewApi.md#neurostore_resources_review_source_reviews_view_put) | **PUT** /review/sources/{id}/review | Start the caller&#39;s review of a paper


# **neurostore_resources_review_review_bundles_view_get**
> object neurostore_resources_review_review_bundles_view_get(id)

Everything the review app needs to open one paper for the caller

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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    id = 'id_example' # str | 

    try:
        # Everything the review app needs to open one paper for the caller
        api_response = api_instance.neurostore_resources_review_review_bundles_view_get(id)
        print("The response of ReviewApi->neurostore_resources_review_review_bundles_view_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_review_bundles_view_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_review_review_export_view_get**
> bytearray neurostore_resources_review_review_export_view_get(id)

Export one review as a study_schema layout zip

Any reviewer may export any review. The zip holds the paper's documents and text, the review's record, its coordinate revision when it has one, and its ops in seq order. The whole zip is built in memory before the response is sent.


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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    id = 'id_example' # str | 

    try:
        # Export one review as a study_schema layout zip
        api_response = api_instance.neurostore_resources_review_review_export_view_get(id)
        print("The response of ReviewApi->neurostore_resources_review_review_export_view_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_review_export_view_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A zip of the review&#39;s layout |  * Content-Disposition - An attachment named review-exports.zip <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_review_review_exports_view_post**
> bytearray neurostore_resources_review_review_exports_view_post(neurostore_resources_review_review_exports_view_post_request=neurostore_resources_review_review_exports_view_post_request)

Export the reviews that match the filters as a zip of layout trees

One layout tree per reviewer, under the reviewer's id. A source with no review is included, as loaded under _source/, only when include_unreviewed is true. An empty filter list means no filter. include_unreviewed cannot be combined with user_ids or states; that request is refused with 422. The whole zip is built in memory before the response is sent, so split a large export with source_ids or base_study_ids.


### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.neurostore_resources_review_review_exports_view_post_request import NeurostoreResourcesReviewReviewExportsViewPostRequest
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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    neurostore_resources_review_review_exports_view_post_request = neurostore_sdk.NeurostoreResourcesReviewReviewExportsViewPostRequest() # NeurostoreResourcesReviewReviewExportsViewPostRequest |  (optional)

    try:
        # Export the reviews that match the filters as a zip of layout trees
        api_response = api_instance.neurostore_resources_review_review_exports_view_post(neurostore_resources_review_review_exports_view_post_request=neurostore_resources_review_review_exports_view_post_request)
        print("The response of ReviewApi->neurostore_resources_review_review_exports_view_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_review_exports_view_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neurostore_resources_review_review_exports_view_post_request** | [**NeurostoreResourcesReviewReviewExportsViewPostRequest**](NeurostoreResourcesReviewReviewExportsViewPostRequest.md)|  | [optional] 

### Return type

**bytearray**

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A zip of the layout trees |  * Content-Disposition - An attachment named review-exports.zip <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | include_unreviewed was combined with a reviewer or state filter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_review_review_imports_view_post**
> ReviewImportReport neurostore_resources_review_review_imports_view_post(file)

Load the papers of a study_schema layout zip for review

Lead reviewers only (admin-reviewer and admin). Each paper is checked and stored on its own: the report names what loaded, what was already loaded and what failed, and why. A file that is not a layout is refused whole.


### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.review_import_report import ReviewImportReport
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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    file = None # bytearray | A zip of a study_schema layout, at most 200 MB.

    try:
        # Load the papers of a study_schema layout zip for review
        api_response = api_instance.neurostore_resources_review_review_imports_view_post(file)
        print("The response of ReviewApi->neurostore_resources_review_review_imports_view_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_review_imports_view_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| A zip of a study_schema layout, at most 200 MB. | 

### Return type

[**ReviewImportReport**](ReviewImportReport.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The report of what each paper did |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**413** | The file is over 200 MB |  * X-Request-ID -  <br>  |
**422** | Unprocessable Entity |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_review_review_ops_view_post**
> ReviewOpResult neurostore_resources_review_review_ops_view_post(id, review_op_batch=review_op_batch)

Apply a batch of the owner's ops to their review

Only the review's owner. The batch applies whole or not at all. A batch whose every client_op_id is already stored is a replay: it returns the stored ops and applies nothing.


### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.review_op_batch import ReviewOpBatch
from neurostore_sdk.models.review_op_result import ReviewOpResult
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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    id = 'id_example' # str | 
    review_op_batch = neurostore_sdk.ReviewOpBatch() # ReviewOpBatch |  (optional)

    try:
        # Apply a batch of the owner's ops to their review
        api_response = api_instance.neurostore_resources_review_review_ops_view_post(id, review_op_batch=review_op_batch)
        print("The response of ReviewApi->neurostore_resources_review_review_ops_view_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_review_ops_view_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **review_op_batch** | [**ReviewOpBatch**](ReviewOpBatch.md)|  | [optional] 

### Return type

[**ReviewOpResult**](ReviewOpResult.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ops applied, or the stored ops of a replay |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  * X-Request-ID -  <br>  |
**409** | The review is not in_progress, expected_last_seq is not the review&#39;s last_seq (the body carries last_seq), or only some of the batch&#39;s client_op_ids are stored  |  -  |
**422** | Unprocessable Entity |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_review_review_sources_view_search**
> ReviewSourceList neurostore_resources_review_review_sources_view_search(page=page, page_size=page_size, base_study_id=base_study_id, mine=mine)

List papers loaded for review, with each reviewer's progress

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.review_source_list import ReviewSourceList
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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    base_study_id = 'base_study_id_example' # str | Only the sources of this base study. (optional)
    mine = False # bool | Only the sources the caller has a review of. (optional) (default to False)

    try:
        # List papers loaded for review, with each reviewer's progress
        api_response = api_instance.neurostore_resources_review_review_sources_view_search(page=page, page_size=page_size, base_study_id=base_study_id, mine=mine)
        print("The response of ReviewApi->neurostore_resources_review_review_sources_view_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_review_sources_view_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **base_study_id** | **str**| Only the sources of this base study. | [optional] 
 **mine** | **bool**| Only the sources the caller has a review of. | [optional] [default to False]

### Return type

[**ReviewSourceList**](ReviewSourceList.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_review_reviews_view_get**
> ReviewDetail neurostore_resources_review_reviews_view_get(id)

One reviewer's review of a paper

Any reviewer may read any review.

### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.review_detail import ReviewDetail
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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    id = 'id_example' # str | 

    try:
        # One reviewer's review of a paper
        api_response = api_instance.neurostore_resources_review_reviews_view_get(id)
        print("The response of ReviewApi->neurostore_resources_review_reviews_view_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_reviews_view_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ReviewDetail**](ReviewDetail.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_review_reviews_view_patch**
> ReviewSummary neurostore_resources_review_reviews_view_patch(id, review_state_patch=review_state_patch)

Submit, reopen, or mark as the reference review

The owner moves in_progress to submitted and back. Only an admin sets reference, and a paper has at most one reference review.


### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.review_state_patch import ReviewStatePatch
from neurostore_sdk.models.review_summary import ReviewSummary
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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    id = 'id_example' # str | 
    review_state_patch = neurostore_sdk.ReviewStatePatch() # ReviewStatePatch |  (optional)

    try:
        # Submit, reopen, or mark as the reference review
        api_response = api_instance.neurostore_resources_review_reviews_view_patch(id, review_state_patch=review_state_patch)
        print("The response of ReviewApi->neurostore_resources_review_reviews_view_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_reviews_view_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **review_state_patch** | [**ReviewStatePatch**](ReviewStatePatch.md)|  | [optional] 

### Return type

[**ReviewSummary**](ReviewSummary.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  * X-Request-ID -  <br>  |
**409** | The transition is not allowed, or the paper already has a reference review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_review_source_reviews_view_put**
> ReviewSummary neurostore_resources_review_source_reviews_view_put(id)

Start the caller's review of a paper

Starts the caller's review, in_progress, from the source's extraction record. A repeat call returns the existing review.


### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.review_summary import ReviewSummary
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
    api_instance = neurostore_sdk.ReviewApi(api_client)
    id = 'id_example' # str | 

    try:
        # Start the caller's review of a paper
        api_response = api_instance.neurostore_resources_review_source_reviews_view_put(id)
        print("The response of ReviewApi->neurostore_resources_review_source_reviews_view_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->neurostore_resources_review_source_reviews_view_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ReviewSummary**](ReviewSummary.md)

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The caller&#39;s review already existed |  -  |
**201** | The caller&#39;s review was started |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

