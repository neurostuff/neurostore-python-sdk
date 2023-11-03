# neurostore_sdk.DefaultApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_options**](DefaultApi.md#annotations_options) | **OPTIONS** /annotations/ | 
[**base_studies_get**](DefaultApi.md#base_studies_get) | **GET** /base-studies/ | 
[**base_studies_id_get**](DefaultApi.md#base_studies_id_get) | **GET** /base-studies/{id} | Your GET endpoint
[**base_studies_id_put**](DefaultApi.md#base_studies_id_put) | **PUT** /base-studies/{id} | 
[**base_studies_post**](DefaultApi.md#base_studies_post) | **POST** /base-studies/ | 


# **annotations_options**
> annotations_options()



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
    api_instance = neurostore_sdk.DefaultApi(api_client)

    try:
        # 
        api_instance.annotations_options()
    except Exception as e:
        print("Exception when calling DefaultApi->annotations_options: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **base_studies_get**
> BaseStudyList base_studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, publication=publication, pmid=pmid, doi=doi, flat=flat, info=info)



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
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
    api_instance = neurostore_sdk.DefaultApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    authors = 'authors_example' # str | search authors (optional)
    level = 'group' # str | select between studies with group results or meta results (optional) (default to 'group')
    data_type = 'data_type_example' # str | whether searching for studies that contain coordinates, images, or both (optional)
    publication = 'publication_example' # str | search for papers from a particular journal (optional)
    pmid = 'pmid_example' # str | search for particular pmid (optional)
    doi = 'doi_example' # str | search for study with specific doi (optional)
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)
    info = True # bool | show additional for endpoint-object relationships without being fully nested. Incompatible with nested (optional)

    try:
        # 
        api_response = api_instance.base_studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, publication=publication, pmid=pmid, doi=doi, flat=flat, info=info)
        print("The response of DefaultApi->base_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->base_studies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional] 
 **sort** | **str**| Parameter to sort results on | [optional] [default to &#39;created_at&#39;]
 **page** | **int**| page of results | [optional] 
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional] 
 **page_size** | **int**| number of results to show on a page | [optional] 
 **name** | **str**| search the name field for a term | [optional] 
 **description** | **str**| search description field for a term | [optional] 
 **authors** | **str**| search authors | [optional] 
 **level** | **str**| select between studies with group results or meta results | [optional] [default to &#39;group&#39;]
 **data_type** | **str**| whether searching for studies that contain coordinates, images, or both | [optional] 
 **publication** | **str**| search for papers from a particular journal | [optional] 
 **pmid** | **str**| search for particular pmid | [optional] 
 **doi** | **str**| search for study with specific doi | [optional] 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 
 **info** | **bool**| show additional for endpoint-object relationships without being fully nested. Incompatible with nested | [optional] 

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
> BaseStudyReturn base_studies_id_get(id, flat=flat, info=info)

Your GET endpoint

### Example

```python
import time
import os
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
    api_instance = neurostore_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 
    flat = True # bool | do not return any embedded relationships. When set, it is incompatible with nested.  (optional)
    info = True # bool | show additional for endpoint-object relationships without being fully nested. Incompatible with nested (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.base_studies_id_get(id, flat=flat, info=info)
        print("The response of DefaultApi->base_studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->base_studies_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **flat** | **bool**| do not return any embedded relationships. When set, it is incompatible with nested.  | [optional] 
 **info** | **bool**| show additional for endpoint-object relationships without being fully nested. Incompatible with nested | [optional] 

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
import time
import os
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
    api_instance = neurostore_sdk.DefaultApi(api_client)
    id = 'id_example' # str | 
    base_study = neurostore_sdk.BaseStudy() # BaseStudy |  (optional)

    try:
        # 
        api_response = api_instance.base_studies_id_put(id, base_study=base_study)
        print("The response of DefaultApi->base_studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->base_studies_id_put: %s\n" % e)
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
import time
import os
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
    api_instance = neurostore_sdk.DefaultApi(api_client)
    base_studies_post_request = neurostore_sdk.BaseStudiesPostRequest() # BaseStudiesPostRequest |  (optional)

    try:
        # 
        api_response = api_instance.base_studies_post(base_studies_post_request=base_studies_post_request)
        print("The response of DefaultApi->base_studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->base_studies_post: %s\n" % e)
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

