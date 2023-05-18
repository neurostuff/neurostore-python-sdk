<a name="__pageTop"></a>
# neurostore_sdk.apis.tags.annotations_api.AnnotationsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_get**](#annotations_get) | **get** /annotations/ | Your GET endpoint
[**annotations_id_delete**](#annotations_id_delete) | **delete** /annotations/{id} | DELETE an annotation
[**annotations_id_get**](#annotations_id_get) | **get** /annotations/{id} | Your GET endpoint
[**annotations_id_put**](#annotations_id_put) | **put** /annotations/{id} | Update an annotation
[**annotations_post**](#annotations_post) | **post** /annotations/ | Post Annotation

# **annotations_get**
<a name="annotations_get"></a>
> AnnotationList annotations_get()

Your GET endpoint

get annotations for an available studyset

### Example

```python
import neurostore_sdk
from neurostore_sdk.apis.tags import annotations_api
from neurostore_sdk.model.annotation_list import AnnotationList
from pprint import pprint
# Defining the host is optional and defaults to https://neurostore.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "https://neurostore.org/api"
)

# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotations_api.AnnotationsApi(api_client)

    # example passing only optional values
    query_params = {
        'studyset_id': "studyset_id_example",
    }
    try:
        # Your GET endpoint
        api_response = api_instance.annotations_get(
            query_params=query_params,
        )
        pprint(api_response)
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
studyset_id | StudysetIdSchema | | optional


# StudysetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#annotations_get.ApiResponseFor200) | OK

#### annotations_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationList**](../../models/AnnotationList.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **annotations_id_delete**
<a name="annotations_id_delete"></a>
> annotations_id_delete(id)

DELETE an annotation

delete annotation

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import neurostore_sdk
from neurostore_sdk.apis.tags import annotations_api
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotations_api.AnnotationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # DELETE an annotation
        api_response = api_instance.annotations_id_delete(
            path_params=path_params,
        )
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#annotations_id_delete.ApiResponseFor200) | OK

#### annotations_id_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JSON-Web-Token](../../../README.md#JSON-Web-Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **annotations_id_get**
<a name="annotations_id_get"></a>
> AnnotationReturn annotations_id_get(id)

Your GET endpoint

get an individual annotation

### Example

```python
import neurostore_sdk
from neurostore_sdk.apis.tags import annotations_api
from neurostore_sdk.model.annotation_return import AnnotationReturn
from pprint import pprint
# Defining the host is optional and defaults to https://neurostore.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "https://neurostore.org/api"
)

# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotations_api.AnnotationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    try:
        # Your GET endpoint
        api_response = api_instance.annotations_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'export': True,
    }
    try:
        # Your GET endpoint
        api_response = api_instance.annotations_id_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
export | ExportSchema | | optional


# ExportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#annotations_id_get.ApiResponseFor200) | OK

#### annotations_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationReturn**](../../models/AnnotationReturn.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **annotations_id_put**
<a name="annotations_id_put"></a>
> AnnotationReturn annotations_id_put(id)

Update an annotation

edit an existing annotation

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import neurostore_sdk
from neurostore_sdk.apis.tags import annotations_api
from neurostore_sdk.model.annotation_return import AnnotationReturn
from neurostore_sdk.model.annotation_request import AnnotationRequest
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotations_api.AnnotationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Update an annotation
        api_response = api_instance.annotations_id_put(
            path_params=path_params,
        )
        pprint(api_response)
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    body = AnnotationRequest(None)
    try:
        # Update an annotation
        api_response = api_instance.annotations_id_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationRequest**](../../models/AnnotationRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#annotations_id_put.ApiResponseFor200) | OK

#### annotations_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationReturn**](../../models/AnnotationReturn.md) |  | 


### Authorization

[JSON-Web-Token](../../../README.md#JSON-Web-Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **annotations_post**
<a name="annotations_post"></a>
> AnnotationReturn annotations_post()

Post Annotation

Create an annotation

### Example

* Bearer Authentication (JSON-Web-Token):
```python
import neurostore_sdk
from neurostore_sdk.apis.tags import annotations_api
from neurostore_sdk.model.annotation_return import AnnotationReturn
from neurostore_sdk.model.annotation_request import AnnotationRequest
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
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = annotations_api.AnnotationsApi(api_client)

    # example passing only optional values
    query_params = {
        'source': "neurostore",
        'source_id': "1234567890ab",
    }
    body = AnnotationRequest(None)
    try:
        # Post Annotation
        api_response = api_instance.annotations_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnnotationsApi->annotations_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationRequest**](../../models/AnnotationRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
source | SourceSchema | | optional
source_id | SourceIdSchema | | optional


# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["neurostore", "neurovault", "pubmed", "neurosynth", "neuroquery", ] if omitted the server will use the default value of "neurostore"

# SourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#annotations_post.ApiResponseFor200) | OK

#### annotations_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AnnotationReturn**](../../models/AnnotationReturn.md) |  | 


### Authorization

[JSON-Web-Token](../../../README.md#JSON-Web-Token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

