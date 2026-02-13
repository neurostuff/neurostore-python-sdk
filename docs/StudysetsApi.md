# neurostore_sdk.StudysetsApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studysets_get**](StudysetsApi.md#studysets_get) | **GET** /studysets/ | GET a list of studysets


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
    api_instance = neurostore_sdk.StudysetsApi(api_client)
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
        print("The response of StudysetsApi->studysets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudysetsApi->studysets_get: %s\n" % e)
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

