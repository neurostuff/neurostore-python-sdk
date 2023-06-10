# neurostore_sdk.DefaultApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abstract_studies_get**](DefaultApi.md#abstract_studies_get) | **GET** /abstract-studies/ | 
[**abstract_studies_id_get**](DefaultApi.md#abstract_studies_id_get) | **GET** /abstract-studies/{id} | Your GET endpoint
[**abstract_studies_id_put**](DefaultApi.md#abstract_studies_id_put) | **PUT** /abstract-studies/{id} | 
[**abstract_studies_post**](DefaultApi.md#abstract_studies_post) | **POST** /abstract-studies/ | 


# **abstract_studies_get**
> AbstractStudyReturn abstract_studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, source=source, publication=publication, pmid=pmid, doi=doi)



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.abstract_study_return import AbstractStudyReturn
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
    source = 'neurostore' # str | the source of the resource you would like to filter/copy from (optional) (default to 'neurostore')
    publication = 'publication_example' # str | search for papers from a particular journal (optional)
    pmid = 'pmid_example' # str | search for particular pmid (optional)
    doi = 'doi_example' # str | search for study with specific doi (optional)

    try:
        # 
        api_response = api_instance.abstract_studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, authors=authors, level=level, data_type=data_type, source=source, publication=publication, pmid=pmid, doi=doi)
        print("The response of DefaultApi->abstract_studies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->abstract_studies_get: %s\n" % e)
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
 **source** | **str**| the source of the resource you would like to filter/copy from | [optional] [default to &#39;neurostore&#39;]
 **publication** | **str**| search for papers from a particular journal | [optional] 
 **pmid** | **str**| search for particular pmid | [optional] 
 **doi** | **str**| search for study with specific doi | [optional] 

### Return type

[**AbstractStudyReturn**](AbstractStudyReturn.md)

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

# **abstract_studies_id_get**
> AbstractStudyReturn abstract_studies_id_get(id)

Your GET endpoint

### Example

```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.abstract_study_return import AbstractStudyReturn
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

    try:
        # Your GET endpoint
        api_response = api_instance.abstract_studies_id_get(id)
        print("The response of DefaultApi->abstract_studies_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->abstract_studies_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AbstractStudyReturn**](AbstractStudyReturn.md)

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

# **abstract_studies_id_put**
> AbstractStudyReturn abstract_studies_id_put(id, abstract_study=abstract_study)



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.abstract_study import AbstractStudy
from neurostore_sdk.models.abstract_study_return import AbstractStudyReturn
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
    abstract_study = neurostore_sdk.AbstractStudy() # AbstractStudy |  (optional)

    try:
        # 
        api_response = api_instance.abstract_studies_id_put(id, abstract_study=abstract_study)
        print("The response of DefaultApi->abstract_studies_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->abstract_studies_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **abstract_study** | [**AbstractStudy**](AbstractStudy.md)|  | [optional] 

### Return type

[**AbstractStudyReturn**](AbstractStudyReturn.md)

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

# **abstract_studies_post**
> AbstractStudyList abstract_studies_post(abstract_study=abstract_study)



### Example

* Bearer Authentication (JSON-Web-Token):
```python
import time
import os
import neurostore_sdk
from neurostore_sdk.models.abstract_study import AbstractStudy
from neurostore_sdk.models.abstract_study_list import AbstractStudyList
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
    abstract_study = neurostore_sdk.AbstractStudy() # AbstractStudy |  (optional)

    try:
        # 
        api_response = api_instance.abstract_studies_post(abstract_study=abstract_study)
        print("The response of DefaultApi->abstract_studies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->abstract_studies_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abstract_study** | [**AbstractStudy**](AbstractStudy.md)|  | [optional] 

### Return type

[**AbstractStudyList**](AbstractStudyList.md)

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

