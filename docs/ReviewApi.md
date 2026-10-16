# neurostore_sdk.ReviewApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**review_exports_post**](ReviewApi.md#review_exports_post) | **POST** /review/exports/ | Export the reviews that match the filters as a zip of layout trees
[**review_imports_post**](ReviewApi.md#review_imports_post) | **POST** /review/imports/ | Load the papers of a study_schema layout zip for review
[**review_reviews_id_export_get**](ReviewApi.md#review_reviews_id_export_get) | **GET** /review/reviews/{id}/export | Export one review as a study_schema layout zip
[**review_reviews_id_get**](ReviewApi.md#review_reviews_id_get) | **GET** /review/reviews/{id} | One reviewer&#39;s review of a paper
[**review_reviews_id_ops_post**](ReviewApi.md#review_reviews_id_ops_post) | **POST** /review/reviews/{id}/ops | Apply a batch of the owner&#39;s ops to their review
[**review_reviews_id_patch**](ReviewApi.md#review_reviews_id_patch) | **PATCH** /review/reviews/{id} | Submit, reopen, or mark as the reference review
[**review_sources_get**](ReviewApi.md#review_sources_get) | **GET** /review/sources/ | List papers loaded for review, with each reviewer&#39;s progress
[**review_sources_id_bundle_get**](ReviewApi.md#review_sources_id_bundle_get) | **GET** /review/sources/{id}/bundle | Everything the review app needs to open one paper for the caller
[**review_sources_id_review_put**](ReviewApi.md#review_sources_id_review_put) | **PUT** /review/sources/{id}/review | Start the caller&#39;s review of a paper


# **review_exports_post**
> bytearray review_exports_post(review_exports_post_request=review_exports_post_request)

Export the reviews that match the filters as a zip of layout trees

One layout tree per reviewer, under the reviewer's id. A source with no review is included, as loaded under unreviewed/, only when include_unreviewed is true. An empty filter list means no filter. include_unreviewed cannot be combined with user_ids or states; that request is refused with 422. The whole zip is built in memory before the response is sent, so split a large export with source_ids or base_study_ids.


### Example

* Bearer Authentication (JSON-Web-Token):

```python
import neurostore_sdk
from neurostore_sdk.models.review_exports_post_request import ReviewExportsPostRequest
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
    review_exports_post_request = neurostore_sdk.ReviewExportsPostRequest() # ReviewExportsPostRequest |  (optional)

    try:
        # Export the reviews that match the filters as a zip of layout trees
        api_response = api_instance.review_exports_post(review_exports_post_request=review_exports_post_request)
        print("The response of ReviewApi->review_exports_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_exports_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_exports_post_request** | [**ReviewExportsPostRequest**](ReviewExportsPostRequest.md)|  | [optional] 

### Return type

**bytearray**

### Authorization

[JSON-Web-Token](../README.md#JSON-Web-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A zip of the layout trees |  * Content-Disposition - An attachment named review-exports.zip <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | include_unreviewed was combined with a reviewer or state filter, or a source&#39;s paper has no article_id  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_imports_post**
> ReviewImportReport review_imports_post(file)

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
        api_response = api_instance.review_imports_post(file)
        print("The response of ReviewApi->review_imports_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_imports_post: %s\n" % e)
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

# **review_reviews_id_export_get**
> bytearray review_reviews_id_export_get(id)

Export one review as a study_schema layout zip

Any reviewer may export any review. The zip holds the paper's documents and text, the review's record, its coordinate revision when it has one (each analysis's verdict taken from the review's provenance, a rejected analysis written as omit), and its ops in seq order. The record is never changed by the export; run/provenance/<id>.json beside it names the review, its state, whether it was reviewed and whether its record was edited, and the source record it derives from. The whole zip is built in memory before the response is sent.


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
        api_response = api_instance.review_reviews_id_export_get(id)
        print("The response of ReviewApi->review_reviews_id_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_reviews_id_export_get: %s\n" % e)
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
**422** | The paper of a review&#39;s source has no article_id, so it cannot be exported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_reviews_id_get**
> ReviewDetail review_reviews_id_get(id)

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
        api_response = api_instance.review_reviews_id_get(id)
        print("The response of ReviewApi->review_reviews_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_reviews_id_get: %s\n" % e)
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

# **review_reviews_id_ops_post**
> ReviewOpResult review_reviews_id_ops_post(id, review_op_batch=review_op_batch)

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
        api_response = api_instance.review_reviews_id_ops_post(id, review_op_batch=review_op_batch)
        print("The response of ReviewApi->review_reviews_id_ops_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_reviews_id_ops_post: %s\n" % e)
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
**400** | The body is not a batch: empty, more than 500 ops, or an op that is not an object. The error names the rule that failed, not the batch.  |  -  |
**404** | Not Found |  * X-Request-ID -  <br>  |
**409** | The review is not in_progress, expected_last_seq is not the review&#39;s last_seq (the body carries last_seq), or only some of the batch&#39;s client_op_ids are stored  |  -  |
**413** | The request body is over the review body limit (8 MiB) |  -  |
**422** | The batch does not validate, an op cannot be applied, or the record would fail study_schema. Each refused op is one error: field ops/&lt;index&gt;, code REJECTED, and context with op_index (an integer) and client_op_id. The message names the problem. A problem with the batch as a whole has field ops and no op index. Nothing is applied.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_reviews_id_patch**
> ReviewSummary review_reviews_id_patch(id, review_state_patch=review_state_patch)

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
        api_response = api_instance.review_reviews_id_patch(id, review_state_patch=review_state_patch)
        print("The response of ReviewApi->review_reviews_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_reviews_id_patch: %s\n" % e)
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

# **review_sources_get**
> ReviewSourceList review_sources_get(page=page, page_size=page_size, base_study_id=base_study_id, mine=mine)

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
        api_response = api_instance.review_sources_get(page=page, page_size=page_size, base_study_id=base_study_id, mine=mine)
        print("The response of ReviewApi->review_sources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_sources_get: %s\n" % e)
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

# **review_sources_id_bundle_get**
> object review_sources_id_bundle_get(id)

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
        api_response = api_instance.review_sources_id_bundle_get(id)
        print("The response of ReviewApi->review_sources_id_bundle_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_sources_id_bundle_get: %s\n" % e)
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

# **review_sources_id_review_put**
> ReviewSummary review_sources_id_review_put(id)

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
        api_response = api_instance.review_sources_id_review_put(id)
        print("The response of ReviewApi->review_sources_id_review_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewApi->review_sources_id_review_put: %s\n" % e)
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
**409** | The source&#39;s stored documents no longer validate against study_schema (for example after a schema upgrade), so no review is started. Each problem is one error with code source_invalid; re-import the source.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

