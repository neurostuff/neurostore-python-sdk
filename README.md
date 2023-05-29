# neurostore-sdk
Create studysets for meta-analysis

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/jdkent](https://github.com/jdkent)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import neurostore_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import neurostore_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = neurostore_sdk.AnalysesApi(api_client)
    search = 'imagin' # str | search for entries that contain the substring (optional)
    sort = 'created_at' # str | Parameter to sort results on (optional) (default to 'created_at')
    page = 56 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 56 # int | number of results to show on a page (optional)
    name = 'name_example' # str | search the name field for a term (optional)
    description = 'description_example' # str | search description field for a term (optional)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET list of analyses
        api_response = api_instance.analyses_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, name=name, description=description, nested=nested)
        print("The response of AnalysesApi->analyses_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnalysesApi->analyses_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://neurostore.org/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalysesApi* | [**analyses_get**](docs/AnalysesApi.md#analyses_get) | **GET** /analyses/ | GET list of analyses
*AnalysesApi* | [**analyses_id_delete**](docs/AnalysesApi.md#analyses_id_delete) | **DELETE** /analyses/{id} | DELETE an analysis
*AnalysesApi* | [**analyses_id_get**](docs/AnalysesApi.md#analyses_id_get) | **GET** /analyses/{id} | GET an analysis
*AnalysesApi* | [**analyses_id_put**](docs/AnalysesApi.md#analyses_id_put) | **PUT** /analyses/{id} | PUT/update an analysis
*AnalysesApi* | [**analyses_post**](docs/AnalysesApi.md#analyses_post) | **POST** /analyses/ | POST/create an analysis
*AnnotationsApi* | [**annotations_get**](docs/AnnotationsApi.md#annotations_get) | **GET** /annotations/ | Your GET endpoint
*AnnotationsApi* | [**annotations_id_delete**](docs/AnnotationsApi.md#annotations_id_delete) | **DELETE** /annotations/{id} | DELETE an annotation
*AnnotationsApi* | [**annotations_id_get**](docs/AnnotationsApi.md#annotations_id_get) | **GET** /annotations/{id} | Your GET endpoint
*AnnotationsApi* | [**annotations_id_put**](docs/AnnotationsApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an annotation
*AnnotationsApi* | [**annotations_post**](docs/AnnotationsApi.md#annotations_post) | **POST** /annotations/ | Post Annotation
*ConditionsApi* | [**conditions_get**](docs/ConditionsApi.md#conditions_get) | **GET** /conditions/ | GET Conditions
*ConditionsApi* | [**conditions_id_delete**](docs/ConditionsApi.md#conditions_id_delete) | **DELETE** /conditions/{id} | DELETE a condition
*ConditionsApi* | [**conditions_id_get**](docs/ConditionsApi.md#conditions_id_get) | **GET** /conditions/{id} | GET a condition
*ConditionsApi* | [**conditions_id_put**](docs/ConditionsApi.md#conditions_id_put) | **PUT** /conditions/{id} | PUT/update a condition
*ConditionsApi* | [**conditions_post**](docs/ConditionsApi.md#conditions_post) | **POST** /conditions/ | POST/Create a condition
*ImagesApi* | [**images_get**](docs/ImagesApi.md#images_get) | **GET** /images/ | GET a list of images
*ImagesApi* | [**images_id_delete**](docs/ImagesApi.md#images_id_delete) | **DELETE** /images/{id} | DELETE an image
*ImagesApi* | [**images_id_get**](docs/ImagesApi.md#images_id_get) | **GET** /images/{id} | GET an image
*ImagesApi* | [**images_id_put**](docs/ImagesApi.md#images_id_put) | **PUT** /images/{id} | PUT/update an image
*ImagesApi* | [**images_post**](docs/ImagesApi.md#images_post) | **POST** /images/ | POST/create an image
*PointsApi* | [**points_get**](docs/PointsApi.md#points_get) | **GET** /points/ | Get Points
*PointsApi* | [**points_id_delete**](docs/PointsApi.md#points_id_delete) | **DELETE** /points/{id} | DELETE a point
*PointsApi* | [**points_id_get**](docs/PointsApi.md#points_id_get) | **GET** /points/{id} | GET a point
*PointsApi* | [**points_id_put**](docs/PointsApi.md#points_id_put) | **PUT** /points/{id} | PUT/update a point
*PointsApi* | [**points_post**](docs/PointsApi.md#points_post) | **POST** /points/ | POST Points
*StoreApi* | [**analyses_get**](docs/StoreApi.md#analyses_get) | **GET** /analyses/ | GET list of analyses
*StoreApi* | [**analyses_id_delete**](docs/StoreApi.md#analyses_id_delete) | **DELETE** /analyses/{id} | DELETE an analysis
*StoreApi* | [**analyses_id_get**](docs/StoreApi.md#analyses_id_get) | **GET** /analyses/{id} | GET an analysis
*StoreApi* | [**analyses_id_put**](docs/StoreApi.md#analyses_id_put) | **PUT** /analyses/{id} | PUT/update an analysis
*StoreApi* | [**analyses_post**](docs/StoreApi.md#analyses_post) | **POST** /analyses/ | POST/create an analysis
*StoreApi* | [**annotations_get**](docs/StoreApi.md#annotations_get) | **GET** /annotations/ | Your GET endpoint
*StoreApi* | [**annotations_id_delete**](docs/StoreApi.md#annotations_id_delete) | **DELETE** /annotations/{id} | DELETE an annotation
*StoreApi* | [**annotations_id_get**](docs/StoreApi.md#annotations_id_get) | **GET** /annotations/{id} | Your GET endpoint
*StoreApi* | [**annotations_id_put**](docs/StoreApi.md#annotations_id_put) | **PUT** /annotations/{id} | Update an annotation
*StoreApi* | [**annotations_post**](docs/StoreApi.md#annotations_post) | **POST** /annotations/ | Post Annotation
*StoreApi* | [**conditions_get**](docs/StoreApi.md#conditions_get) | **GET** /conditions/ | GET Conditions
*StoreApi* | [**conditions_id_delete**](docs/StoreApi.md#conditions_id_delete) | **DELETE** /conditions/{id} | DELETE a condition
*StoreApi* | [**conditions_id_get**](docs/StoreApi.md#conditions_id_get) | **GET** /conditions/{id} | GET a condition
*StoreApi* | [**conditions_id_put**](docs/StoreApi.md#conditions_id_put) | **PUT** /conditions/{id} | PUT/update a condition
*StoreApi* | [**conditions_post**](docs/StoreApi.md#conditions_post) | **POST** /conditions/ | POST/Create a condition
*StoreApi* | [**images_get**](docs/StoreApi.md#images_get) | **GET** /images/ | GET a list of images
*StoreApi* | [**images_id_delete**](docs/StoreApi.md#images_id_delete) | **DELETE** /images/{id} | DELETE an image
*StoreApi* | [**images_id_get**](docs/StoreApi.md#images_id_get) | **GET** /images/{id} | GET an image
*StoreApi* | [**images_id_put**](docs/StoreApi.md#images_id_put) | **PUT** /images/{id} | PUT/update an image
*StoreApi* | [**images_post**](docs/StoreApi.md#images_post) | **POST** /images/ | POST/create an image
*StoreApi* | [**points_get**](docs/StoreApi.md#points_get) | **GET** /points/ | Get Points
*StoreApi* | [**points_id_delete**](docs/StoreApi.md#points_id_delete) | **DELETE** /points/{id} | DELETE a point
*StoreApi* | [**points_id_get**](docs/StoreApi.md#points_id_get) | **GET** /points/{id} | GET a point
*StoreApi* | [**points_id_put**](docs/StoreApi.md#points_id_put) | **PUT** /points/{id} | PUT/update a point
*StoreApi* | [**points_post**](docs/StoreApi.md#points_post) | **POST** /points/ | POST Points
*StoreApi* | [**studies_get**](docs/StoreApi.md#studies_get) | **GET** /studies/ | GET a list of studies
*StoreApi* | [**studies_id_delete**](docs/StoreApi.md#studies_id_delete) | **DELETE** /studies/{id} | DELETE a study
*StoreApi* | [**studies_id_get**](docs/StoreApi.md#studies_id_get) | **GET** /studies/{id} | GET a study
*StoreApi* | [**studies_id_put**](docs/StoreApi.md#studies_id_put) | **PUT** /studies/{id} | PUT/update a study
*StoreApi* | [**studies_post**](docs/StoreApi.md#studies_post) | **POST** /studies/ | POST/create a study
*StoreApi* | [**studysets_id_delete**](docs/StoreApi.md#studysets_id_delete) | **DELETE** /studysets/{id} | DELETE a studyset
*StoreApi* | [**studysets_id_get**](docs/StoreApi.md#studysets_id_get) | **GET** /studysets/{id} | GET a studyset
*StoreApi* | [**studysets_id_put**](docs/StoreApi.md#studysets_id_put) | **PUT** /studysets/{id} | PUT/update a studyset
*StoreApi* | [**studysets_post**](docs/StoreApi.md#studysets_post) | **POST** /studysets/ | POST/create a studyset
*StudiesApi* | [**studies_get**](docs/StudiesApi.md#studies_get) | **GET** /studies/ | GET a list of studies
*StudiesApi* | [**studies_id_delete**](docs/StudiesApi.md#studies_id_delete) | **DELETE** /studies/{id} | DELETE a study
*StudiesApi* | [**studies_id_get**](docs/StudiesApi.md#studies_id_get) | **GET** /studies/{id} | GET a study
*StudiesApi* | [**studies_id_put**](docs/StudiesApi.md#studies_id_put) | **PUT** /studies/{id} | PUT/update a study
*StudiesApi* | [**studies_post**](docs/StudiesApi.md#studies_post) | **POST** /studies/ | POST/create a study
*StudysetsApi* | [**studysets_get**](docs/StudysetsApi.md#studysets_get) | **GET** /studysets/ | GET a list of studysets
*StudysetsApi* | [**studysets_id_delete**](docs/StudysetsApi.md#studysets_id_delete) | **DELETE** /studysets/{id} | DELETE a studyset
*StudysetsApi* | [**studysets_id_get**](docs/StudysetsApi.md#studysets_id_get) | **GET** /studysets/{id} | GET a studyset
*StudysetsApi* | [**studysets_id_put**](docs/StudysetsApi.md#studysets_id_put) | **PUT** /studysets/{id} | PUT/update a studyset
*StudysetsApi* | [**studysets_post**](docs/StudysetsApi.md#studysets_post) | **POST** /studysets/ | POST/create a studyset
*UserApi* | [**users_get**](docs/UserApi.md#users_get) | **GET** /users/ | Your GET endpoint
*UserApi* | [**users_id_get**](docs/UserApi.md#users_id_get) | **GET** /users/{id} | Individual User Profile
*UserApi* | [**users_id_put**](docs/UserApi.md#users_id_put) | **PUT** /users/{id} | Update Individual Profile
*UserApi* | [**users_post**](docs/UserApi.md#users_post) | **POST** /users/ | 


## Documentation For Models

 - [AnalysisBase](docs/AnalysisBase.md)
 - [AnalysisCommon](docs/AnalysisCommon.md)
 - [AnalysisList](docs/AnalysisList.md)
 - [AnalysisRequest](docs/AnalysisRequest.md)
 - [AnalysisRequestRelationships](docs/AnalysisRequestRelationships.md)
 - [AnalysisRequestRelationshipsConditions](docs/AnalysisRequestRelationshipsConditions.md)
 - [AnalysisRequestRelationshipsImages](docs/AnalysisRequestRelationshipsImages.md)
 - [AnalysisRequestRelationshipsPoints](docs/AnalysisRequestRelationshipsPoints.md)
 - [AnalysisReturn](docs/AnalysisReturn.md)
 - [AnalysisReturnRelationships](docs/AnalysisReturnRelationships.md)
 - [AnalysisReturnRelationshipsConditions](docs/AnalysisReturnRelationshipsConditions.md)
 - [AnalysisReturnRelationshipsImages](docs/AnalysisReturnRelationshipsImages.md)
 - [AnalysisReturnRelationshipsPoints](docs/AnalysisReturnRelationshipsPoints.md)
 - [AnnotationBase](docs/AnnotationBase.md)
 - [AnnotationCommon](docs/AnnotationCommon.md)
 - [AnnotationExport](docs/AnnotationExport.md)
 - [AnnotationList](docs/AnnotationList.md)
 - [AnnotationRequest](docs/AnnotationRequest.md)
 - [AnnotationRequestRelationships](docs/AnnotationRequestRelationships.md)
 - [AnnotationRequestRelationshipsNotes](docs/AnnotationRequestRelationshipsNotes.md)
 - [AnnotationReturn](docs/AnnotationReturn.md)
 - [AnnotationReturnRelationships](docs/AnnotationReturnRelationships.md)
 - [AnnotationReturnRelationshipsNotes](docs/AnnotationReturnRelationshipsNotes.md)
 - [Clone](docs/Clone.md)
 - [ConditionBase](docs/ConditionBase.md)
 - [ConditionList](docs/ConditionList.md)
 - [ConditionRequest](docs/ConditionRequest.md)
 - [ConditionReturn](docs/ConditionReturn.md)
 - [Entity](docs/Entity.md)
 - [ImageBase](docs/ImageBase.md)
 - [ImageCommon](docs/ImageCommon.md)
 - [ImageList](docs/ImageList.md)
 - [ImageRelationships](docs/ImageRelationships.md)
 - [ImageRequest](docs/ImageRequest.md)
 - [ImageReturn](docs/ImageReturn.md)
 - [JsonLd](docs/JsonLd.md)
 - [JsonLdContext](docs/JsonLdContext.md)
 - [Metadata](docs/Metadata.md)
 - [NestedPutAttributes](docs/NestedPutAttributes.md)
 - [NoteCollectionBase](docs/NoteCollectionBase.md)
 - [NoteCollectionRequest](docs/NoteCollectionRequest.md)
 - [NoteCollectionReturn](docs/NoteCollectionReturn.md)
 - [NoteCollectionReturnAllOf](docs/NoteCollectionReturnAllOf.md)
 - [PointBase](docs/PointBase.md)
 - [PointCommon](docs/PointCommon.md)
 - [PointList](docs/PointList.md)
 - [PointRelationships](docs/PointRelationships.md)
 - [PointRelationshipsValues](docs/PointRelationshipsValues.md)
 - [PointRequest](docs/PointRequest.md)
 - [PointReturn](docs/PointReturn.md)
 - [PointValue](docs/PointValue.md)
 - [ReadableResourceAttributes](docs/ReadableResourceAttributes.md)
 - [ResourceAttributes](docs/ResourceAttributes.md)
 - [StudyBase](docs/StudyBase.md)
 - [StudyCommon](docs/StudyCommon.md)
 - [StudyList](docs/StudyList.md)
 - [StudyRequest](docs/StudyRequest.md)
 - [StudyRequestRelationships](docs/StudyRequestRelationships.md)
 - [StudyRequestRelationshipsAnalyses](docs/StudyRequestRelationshipsAnalyses.md)
 - [StudyReturn](docs/StudyReturn.md)
 - [StudyReturnAllOf](docs/StudyReturnAllOf.md)
 - [StudyReturnAllOfStudysets](docs/StudyReturnAllOfStudysets.md)
 - [StudyReturnRelationships](docs/StudyReturnRelationships.md)
 - [StudyReturnRelationshipsAnalyses](docs/StudyReturnRelationshipsAnalyses.md)
 - [StudysetBase](docs/StudysetBase.md)
 - [StudysetList](docs/StudysetList.md)
 - [StudysetRequest](docs/StudysetRequest.md)
 - [StudysetRequestRelationships](docs/StudysetRequestRelationships.md)
 - [StudysetRequestRelationshipsStudies](docs/StudysetRequestRelationshipsStudies.md)
 - [StudysetReturn](docs/StudysetReturn.md)
 - [StudysetReturnRelationships](docs/StudysetReturnRelationships.md)
 - [StudysetReturnRelationshipsStudies](docs/StudysetReturnRelationshipsStudies.md)
 - [StudysetsIdGet404Response](docs/StudysetsIdGet404Response.md)
 - [StudysetsIdPut422Response](docs/StudysetsIdPut422Response.md)
 - [User](docs/User.md)
 - [UserList](docs/UserList.md)
 - [UserResourceAttributes](docs/UserResourceAttributes.md)
 - [UserlessResourceAttributes](docs/UserlessResourceAttributes.md)
 - [WriteableResourceAttributes](docs/WriteableResourceAttributes.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="JSON-Web-Token"></a>
### JSON-Web-Token

- **Type**: Bearer authentication


## Author

jamesdkent21@gmail.com


