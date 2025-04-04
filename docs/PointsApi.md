# neurostore_sdk.PointsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**points_get**](PointsApi.md#points_get) | **GET** /points/ | Get Points
[**points_id_delete**](PointsApi.md#points_id_delete) | **DELETE** /points/{id} | DELETE a point
[**points_id_get**](PointsApi.md#points_id_get) | **GET** /points/{id} | GET a point
[**points_id_put**](PointsApi.md#points_id_put) | **PUT** /points/{id} | PUT/update a point
[**points_post**](PointsApi.md#points_post) | **POST** /points/ | POST Points


# **points_get**
> PointList points_get()

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
    api_instance = neurostore_sdk.PointsApi(api_client)

    try:
        # Get Points
        api_response = api_instance.points_get()
        print("The response of PointsApi->points_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->points_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
    api_instance = neurostore_sdk.PointsApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a point
        api_instance.points_id_delete(id)
    except Exception as e:
        print("Exception when calling PointsApi->points_id_delete: %s\n" % e)
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
    api_instance = neurostore_sdk.PointsApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET a point
        api_response = api_instance.points_id_get(id)
        print("The response of PointsApi->points_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->points_id_get: %s\n" % e)
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
    api_instance = neurostore_sdk.PointsApi(api_client)
    id = 'id_example' # str | 
    point_request = neurostore_sdk.PointRequest() # PointRequest |  (optional)

    try:
        # PUT/update a point
        api_response = api_instance.points_id_put(id, point_request=point_request)
        print("The response of PointsApi->points_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->points_id_put: %s\n" % e)
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
**422** | Example response |  -  |

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
    api_instance = neurostore_sdk.PointsApi(api_client)
    point_request = neurostore_sdk.PointRequest() # PointRequest |  (optional)

    try:
        # POST Points
        api_response = api_instance.points_post(point_request=point_request)
        print("The response of PointsApi->points_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->points_post: %s\n" % e)
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

