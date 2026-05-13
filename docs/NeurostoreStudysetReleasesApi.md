# neurostore_sdk.NeurostoreStudysetReleasesApi

All URIs are relative to *https://neurostore.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**neurostore_resources_neurostore_studyset_releases_download**](NeurostoreStudysetReleasesApi.md#neurostore_resources_neurostore_studyset_releases_download) | **GET** /neurostore-studyset-releases/{version}/download | Download NeuroStore studyset release tarball
[**neurostore_resources_neurostore_studyset_releases_get**](NeurostoreStudysetReleasesApi.md#neurostore_resources_neurostore_studyset_releases_get) | **GET** /neurostore-studyset-releases/{version} | GET NeuroStore studyset release manifest
[**neurostore_resources_neurostore_studyset_releases_search**](NeurostoreStudysetReleasesApi.md#neurostore_resources_neurostore_studyset_releases_search) | **GET** /neurostore-studyset-releases/ | GET NeuroStore studyset release list


# **neurostore_resources_neurostore_studyset_releases_download**
> bytearray neurostore_resources_neurostore_studyset_releases_download(version)

Download NeuroStore studyset release tarball

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
    api_instance = neurostore_sdk.NeurostoreStudysetReleasesApi(api_client)
    version = 'version_example' # str | nightly, latest, or a monthly release in YYYY-MM format.

    try:
        # Download NeuroStore studyset release tarball
        api_response = api_instance.neurostore_resources_neurostore_studyset_releases_download(version)
        print("The response of NeurostoreStudysetReleasesApi->neurostore_resources_neurostore_studyset_releases_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeurostoreStudysetReleasesApi->neurostore_resources_neurostore_studyset_releases_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| nightly, latest, or a monthly release in YYYY-MM format. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **neurostore_resources_neurostore_studyset_releases_get**
> object neurostore_resources_neurostore_studyset_releases_get(version)

GET NeuroStore studyset release manifest

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
    api_instance = neurostore_sdk.NeurostoreStudysetReleasesApi(api_client)
    version = 'version_example' # str | nightly, latest, or a monthly release in YYYY-MM format.

    try:
        # GET NeuroStore studyset release manifest
        api_response = api_instance.neurostore_resources_neurostore_studyset_releases_get(version)
        print("The response of NeurostoreStudysetReleasesApi->neurostore_resources_neurostore_studyset_releases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeurostoreStudysetReleasesApi->neurostore_resources_neurostore_studyset_releases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| nightly, latest, or a monthly release in YYYY-MM format. | 

### Return type

**object**

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

# **neurostore_resources_neurostore_studyset_releases_search**
> NeurostoreResourcesNeurostoreStudysetReleasesSearch200Response neurostore_resources_neurostore_studyset_releases_search()

GET NeuroStore studyset release list

### Example


```python
import neurostore_sdk
from neurostore_sdk.models.neurostore_resources_neurostore_studyset_releases_search200_response import NeurostoreResourcesNeurostoreStudysetReleasesSearch200Response
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
    api_instance = neurostore_sdk.NeurostoreStudysetReleasesApi(api_client)

    try:
        # GET NeuroStore studyset release list
        api_response = api_instance.neurostore_resources_neurostore_studyset_releases_search()
        print("The response of NeurostoreStudysetReleasesApi->neurostore_resources_neurostore_studyset_releases_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeurostoreStudysetReleasesApi->neurostore_resources_neurostore_studyset_releases_search: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NeurostoreResourcesNeurostoreStudysetReleasesSearch200Response**](NeurostoreResourcesNeurostoreStudysetReleasesSearch200Response.md)

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

