# neurostore_sdk.ConditionsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conditions_get**](ConditionsApi.md#conditions_get) | **GET** /conditions/ | GET Conditions
[**conditions_id_delete**](ConditionsApi.md#conditions_id_delete) | **DELETE** /conditions/{id} | DELETE a condition
[**conditions_id_get**](ConditionsApi.md#conditions_id_get) | **GET** /conditions/{id} | GET a condition
[**conditions_id_put**](ConditionsApi.md#conditions_id_put) | **PUT** /conditions/{id} | PUT/update a condition
[**conditions_post**](ConditionsApi.md#conditions_post) | **POST** /conditions/ | POST/Create a condition


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
    api_instance = neurostore_sdk.ConditionsApi(api_client)
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
        print("The response of ConditionsApi->conditions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConditionsApi->conditions_get: %s\n" % e)
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
    api_instance = neurostore_sdk.ConditionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE a condition
        api_instance.conditions_id_delete(id)
    except Exception as e:
        print("Exception when calling ConditionsApi->conditions_id_delete: %s\n" % e)
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
    api_instance = neurostore_sdk.ConditionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET a condition
        api_response = api_instance.conditions_id_get(id)
        print("The response of ConditionsApi->conditions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConditionsApi->conditions_id_get: %s\n" % e)
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
**404** | Example response |  -  |

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
    api_instance = neurostore_sdk.ConditionsApi(api_client)
    id = 'id_example' # str | 
    condition_request = neurostore_sdk.ConditionRequest() # ConditionRequest |  (optional)

    try:
        # PUT/update a condition
        api_response = api_instance.conditions_id_put(id, condition_request=condition_request)
        print("The response of ConditionsApi->conditions_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConditionsApi->conditions_id_put: %s\n" % e)
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
**422** | Example response |  -  |

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
    api_instance = neurostore_sdk.ConditionsApi(api_client)
    condition_request = neurostore_sdk.ConditionRequest() # ConditionRequest |  (optional)

    try:
        # POST/Create a condition
        api_response = api_instance.conditions_post(condition_request=condition_request)
        print("The response of ConditionsApi->conditions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConditionsApi->conditions_post: %s\n" % e)
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

