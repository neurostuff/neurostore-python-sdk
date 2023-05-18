# neurostore_sdk.ImagesApi

All URIs are relative to *http://localhost:80/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_get**](ImagesApi.md#images_get) | **GET** /images/ | GET a list of images
[**images_id_delete**](ImagesApi.md#images_id_delete) | **DELETE** /images/{id} | DELETE an image
[**images_id_get**](ImagesApi.md#images_id_get) | **GET** /images/{id} | GET an image
[**images_id_put**](ImagesApi.md#images_id_put) | **PUT** /images/{id} | PUT/update an image
[**images_post**](ImagesApi.md#images_post) | **POST** /images/ | POST/create an image


# **images_get**
> ImageList images_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, filename=filename, analysis_name=analysis_name, value_type=value_type, space=space)

GET a list of images

Retrieve and list images.

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.image_list import ImageList
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurostore_sdk.ImagesApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    filename = 'filename_example' # str | search filename field (optional)
    analysis_name = 'analysis_name_example' # str | search analysis_name field (optional)
    value_type = 'value_type_example' # str | search value_type field (optional)
    space = 'space_example' # str | search space field (optional)

    try:
        # GET a list of images
        api_response = api_instance.images_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, filename=filename, analysis_name=analysis_name, value_type=value_type, space=space)
        print("The response of ImagesApi->images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
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
import time
import os
import neurostore_sdk
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "http://localhost:80/api"
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
    api_instance = neurostore_sdk.ImagesApi(api_client)
    id = 'id_example' # str | 

    try:
        # DELETE an image
        api_instance.images_id_delete(id)
    except Exception as e:
        print("Exception when calling ImagesApi->images_id_delete: %s\n" % e)
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
import time
import os
import neurostore_sdk
from neurostore_sdk.models.image_return import ImageReturn
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurostore_sdk.ImagesApi(api_client)
    id = 'id_example' # str | 

    try:
        # GET an image
        api_response = api_instance.images_id_get(id)
        print("The response of ImagesApi->images_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_id_get: %s\n" % e)
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
**404** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_id_put**
> ImageReturn images_id_put(id, image_request=image_request)

PUT/update an image

Update a specific image.

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.image_request import ImageRequest
from neurostore_sdk.models.image_return import ImageReturn
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "http://localhost:80/api"
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
    api_instance = neurostore_sdk.ImagesApi(api_client)
    id = 'id_example' # str | 
    image_request = neurostore_sdk.ImageRequest() # ImageRequest |  (optional)

    try:
        # PUT/update an image
        api_response = api_instance.images_id_put(id, image_request=image_request)
        print("The response of ImagesApi->images_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_id_put: %s\n" % e)
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
**422** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_post**
> ImageReturn images_post(image_request=image_request)

POST/create an image

Create an image

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.image_request import ImageRequest
from neurostore_sdk.models.image_return import ImageReturn
from neurostore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "http://localhost:80/api"
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
    api_instance = neurostore_sdk.ImagesApi(api_client)
    image_request = neurostore_sdk.ImageRequest() # ImageRequest |  (optional)

    try:
        # POST/create an image
        api_response = api_instance.images_post(image_request=image_request)
        print("The response of ImagesApi->images_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_post: %s\n" % e)
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

