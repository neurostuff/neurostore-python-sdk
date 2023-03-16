# neurostore-sdk
Create studysets for meta-analysis

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/jdkent](https://github.com/jdkent)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import neurostore_sdk
from pprint import pprint
from neurostore_sdk.apis.tags import analyses_api
from neurostore_sdk.model.analysis_list import AnalysisList
from neurostore_sdk.model.analysis_request import AnalysisRequest
from neurostore_sdk.model.analysis_return import AnalysisReturn
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_sdk.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analyses_api.AnalysesApi(api_client)
    search = "imagin" # str | search for entries that contain the substring (optional)
sort = "created_at" # str | Parameter to sort results on (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=true, isPathParam=false, isHeaderParam=false, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=true, baseName='sort', paramName='sort', dataType='str', datatypeWithEnum='null', dataFormat='null', collectionFormat='null', description='Parameter to sort results on', unescapedDescription='Parameter to sort results on', baseType='null', defaultValue='"created_at"', enumDefaultValue='null', enumName='null', style='FORM', deepObject='false', allowEmptyValue='false', example='"created_at"', jsonSchema='{
  "name" : "sort",
  "in" : "query",
  "description" : "Parameter to sort results on",
  "required" : false,
  "style" : "form",
  "explode" : true,
  "schema" : {
    "type" : "string",
    "default" : "created_at"
  }
}', isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=false, _enum=null, allowableValues=null, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='string', baseName='SortSchema', complexType='null', getter='getSort', setter='setSort', description='null', dataType='str', datatypeWithEnum='str', dataFormat='null', name='sort', min='null', max='null', defaultValue='"created_at"', defaultValueWithParam=' = data.sort;', baseType='str', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='"created_at"', jsonSchema='{
  "type" : "string",
  "default" : "created_at"
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=false, isInnerEnum=false, isEnumRef=false, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, isNew=false, _enum=null, allowableValues=null, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='Sort', nameInSnakeCase='null', enumName='null', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})
page = 0 # int | page of results (optional)
desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
page_size = 1 # int | number of results to show on a page (optional)
name = "name_example" # str | search the name field for a term (optional)
description = "description_example" # str | search description field for a term (optional)
nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    try:
        # GET list of analyses
        api_response = api_instance.analyses_get(search=searchsort=sortpage=pagedesc=descpage_size=page_sizename=namedescription=descriptionnested=nested)
        pprint(api_response)
    except neurostore_sdk.ApiException as e:
        print("Exception when calling AnalysesApi->analyses_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:80/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalysesApi* | [**analyses_get**](docs/apis/tags/AnalysesApi.md#analyses_get) | **get** /analyses/ | GET list of analyses
*AnalysesApi* | [**analyses_id_delete**](docs/apis/tags/AnalysesApi.md#analyses_id_delete) | **delete** /analyses/{id} | DELETE an analysis
*AnalysesApi* | [**analyses_id_get**](docs/apis/tags/AnalysesApi.md#analyses_id_get) | **get** /analyses/{id} | GET an analysis
*AnalysesApi* | [**analyses_id_put**](docs/apis/tags/AnalysesApi.md#analyses_id_put) | **put** /analyses/{id} | PUT/update an analysis
*AnalysesApi* | [**analyses_post**](docs/apis/tags/AnalysesApi.md#analyses_post) | **post** /analyses/ | POST/create an analysis
*AnnotationsApi* | [**annotations_get**](docs/apis/tags/AnnotationsApi.md#annotations_get) | **get** /annotations/ | Your GET endpoint
*AnnotationsApi* | [**annotations_id_delete**](docs/apis/tags/AnnotationsApi.md#annotations_id_delete) | **delete** /annotations/{id} | DELETE an annotation
*AnnotationsApi* | [**annotations_id_get**](docs/apis/tags/AnnotationsApi.md#annotations_id_get) | **get** /annotations/{id} | Your GET endpoint
*AnnotationsApi* | [**annotations_id_put**](docs/apis/tags/AnnotationsApi.md#annotations_id_put) | **put** /annotations/{id} | Update an annotation
*AnnotationsApi* | [**annotations_post**](docs/apis/tags/AnnotationsApi.md#annotations_post) | **post** /annotations/ | Post Annotation
*ConditionsApi* | [**conditions_get**](docs/apis/tags/ConditionsApi.md#conditions_get) | **get** /conditions/ | GET Conditions
*ConditionsApi* | [**conditions_id_delete**](docs/apis/tags/ConditionsApi.md#conditions_id_delete) | **delete** /conditions/{id} | DELETE a condition
*ConditionsApi* | [**conditions_id_get**](docs/apis/tags/ConditionsApi.md#conditions_id_get) | **get** /conditions/{id} | GET a condition
*ConditionsApi* | [**conditions_id_put**](docs/apis/tags/ConditionsApi.md#conditions_id_put) | **put** /conditions/{id} | PUT/update a condition
*ConditionsApi* | [**conditions_post**](docs/apis/tags/ConditionsApi.md#conditions_post) | **post** /conditions/ | POST/Create a condition
*ImagesApi* | [**images_get**](docs/apis/tags/ImagesApi.md#images_get) | **get** /images/ | GET a list of images
*ImagesApi* | [**images_id_delete**](docs/apis/tags/ImagesApi.md#images_id_delete) | **delete** /images/{id} | DELETE an image
*ImagesApi* | [**images_id_get**](docs/apis/tags/ImagesApi.md#images_id_get) | **get** /images/{id} | GET an image
*ImagesApi* | [**images_id_put**](docs/apis/tags/ImagesApi.md#images_id_put) | **put** /images/{id} | PUT/update an image
*ImagesApi* | [**images_post**](docs/apis/tags/ImagesApi.md#images_post) | **post** /images/ | POST/create an image
*PointsApi* | [**points_get**](docs/apis/tags/PointsApi.md#points_get) | **get** /points/ | Get Points
*PointsApi* | [**points_id_delete**](docs/apis/tags/PointsApi.md#points_id_delete) | **delete** /points/{id} | DELETE a point
*PointsApi* | [**points_id_get**](docs/apis/tags/PointsApi.md#points_id_get) | **get** /points/{id} | GET a point
*PointsApi* | [**points_id_put**](docs/apis/tags/PointsApi.md#points_id_put) | **put** /points/{id} | PUT/update a point
*PointsApi* | [**points_post**](docs/apis/tags/PointsApi.md#points_post) | **post** /points/ | POST Points
*StoreApi* | [**analyses_get**](docs/apis/tags/StoreApi.md#analyses_get) | **get** /analyses/ | GET list of analyses
*StoreApi* | [**analyses_id_delete**](docs/apis/tags/StoreApi.md#analyses_id_delete) | **delete** /analyses/{id} | DELETE an analysis
*StoreApi* | [**analyses_id_get**](docs/apis/tags/StoreApi.md#analyses_id_get) | **get** /analyses/{id} | GET an analysis
*StoreApi* | [**analyses_id_put**](docs/apis/tags/StoreApi.md#analyses_id_put) | **put** /analyses/{id} | PUT/update an analysis
*StoreApi* | [**analyses_post**](docs/apis/tags/StoreApi.md#analyses_post) | **post** /analyses/ | POST/create an analysis
*StoreApi* | [**annotations_get**](docs/apis/tags/StoreApi.md#annotations_get) | **get** /annotations/ | Your GET endpoint
*StoreApi* | [**annotations_id_delete**](docs/apis/tags/StoreApi.md#annotations_id_delete) | **delete** /annotations/{id} | DELETE an annotation
*StoreApi* | [**annotations_id_get**](docs/apis/tags/StoreApi.md#annotations_id_get) | **get** /annotations/{id} | Your GET endpoint
*StoreApi* | [**annotations_id_put**](docs/apis/tags/StoreApi.md#annotations_id_put) | **put** /annotations/{id} | Update an annotation
*StoreApi* | [**annotations_post**](docs/apis/tags/StoreApi.md#annotations_post) | **post** /annotations/ | Post Annotation
*StoreApi* | [**conditions_get**](docs/apis/tags/StoreApi.md#conditions_get) | **get** /conditions/ | GET Conditions
*StoreApi* | [**conditions_id_delete**](docs/apis/tags/StoreApi.md#conditions_id_delete) | **delete** /conditions/{id} | DELETE a condition
*StoreApi* | [**conditions_id_get**](docs/apis/tags/StoreApi.md#conditions_id_get) | **get** /conditions/{id} | GET a condition
*StoreApi* | [**conditions_id_put**](docs/apis/tags/StoreApi.md#conditions_id_put) | **put** /conditions/{id} | PUT/update a condition
*StoreApi* | [**conditions_post**](docs/apis/tags/StoreApi.md#conditions_post) | **post** /conditions/ | POST/Create a condition
*StoreApi* | [**images_get**](docs/apis/tags/StoreApi.md#images_get) | **get** /images/ | GET a list of images
*StoreApi* | [**images_id_delete**](docs/apis/tags/StoreApi.md#images_id_delete) | **delete** /images/{id} | DELETE an image
*StoreApi* | [**images_id_get**](docs/apis/tags/StoreApi.md#images_id_get) | **get** /images/{id} | GET an image
*StoreApi* | [**images_id_put**](docs/apis/tags/StoreApi.md#images_id_put) | **put** /images/{id} | PUT/update an image
*StoreApi* | [**images_post**](docs/apis/tags/StoreApi.md#images_post) | **post** /images/ | POST/create an image
*StoreApi* | [**points_get**](docs/apis/tags/StoreApi.md#points_get) | **get** /points/ | Get Points
*StoreApi* | [**points_id_delete**](docs/apis/tags/StoreApi.md#points_id_delete) | **delete** /points/{id} | DELETE a point
*StoreApi* | [**points_id_get**](docs/apis/tags/StoreApi.md#points_id_get) | **get** /points/{id} | GET a point
*StoreApi* | [**points_id_put**](docs/apis/tags/StoreApi.md#points_id_put) | **put** /points/{id} | PUT/update a point
*StoreApi* | [**points_post**](docs/apis/tags/StoreApi.md#points_post) | **post** /points/ | POST Points
*StoreApi* | [**studies_get**](docs/apis/tags/StoreApi.md#studies_get) | **get** /studies/ | GET a list of studies
*StoreApi* | [**studies_id_delete**](docs/apis/tags/StoreApi.md#studies_id_delete) | **delete** /studies/{id} | DELETE a study
*StoreApi* | [**studies_id_get**](docs/apis/tags/StoreApi.md#studies_id_get) | **get** /studies/{id} | GET a study
*StoreApi* | [**studies_id_put**](docs/apis/tags/StoreApi.md#studies_id_put) | **put** /studies/{id} | PUT/update a study
*StoreApi* | [**studies_post**](docs/apis/tags/StoreApi.md#studies_post) | **post** /studies/ | POST/create a study
*StoreApi* | [**studysets_id_delete**](docs/apis/tags/StoreApi.md#studysets_id_delete) | **delete** /studysets/{id} | DELETE a studyset
*StoreApi* | [**studysets_id_get**](docs/apis/tags/StoreApi.md#studysets_id_get) | **get** /studysets/{id} | GET a studyset
*StoreApi* | [**studysets_id_put**](docs/apis/tags/StoreApi.md#studysets_id_put) | **put** /studysets/{id} | PUT/update a studyset
*StoreApi* | [**studysets_post**](docs/apis/tags/StoreApi.md#studysets_post) | **post** /studysets/ | POST/create a studyset
*StudiesApi* | [**studies_get**](docs/apis/tags/StudiesApi.md#studies_get) | **get** /studies/ | GET a list of studies
*StudiesApi* | [**studies_id_delete**](docs/apis/tags/StudiesApi.md#studies_id_delete) | **delete** /studies/{id} | DELETE a study
*StudiesApi* | [**studies_id_get**](docs/apis/tags/StudiesApi.md#studies_id_get) | **get** /studies/{id} | GET a study
*StudiesApi* | [**studies_id_put**](docs/apis/tags/StudiesApi.md#studies_id_put) | **put** /studies/{id} | PUT/update a study
*StudiesApi* | [**studies_post**](docs/apis/tags/StudiesApi.md#studies_post) | **post** /studies/ | POST/create a study
*StudysetsApi* | [**studysets_get**](docs/apis/tags/StudysetsApi.md#studysets_get) | **get** /studysets/ | GET a list of studysets
*StudysetsApi* | [**studysets_id_delete**](docs/apis/tags/StudysetsApi.md#studysets_id_delete) | **delete** /studysets/{id} | DELETE a studyset
*StudysetsApi* | [**studysets_id_get**](docs/apis/tags/StudysetsApi.md#studysets_id_get) | **get** /studysets/{id} | GET a studyset
*StudysetsApi* | [**studysets_id_put**](docs/apis/tags/StudysetsApi.md#studysets_id_put) | **put** /studysets/{id} | PUT/update a studyset
*StudysetsApi* | [**studysets_post**](docs/apis/tags/StudysetsApi.md#studysets_post) | **post** /studysets/ | POST/create a studyset
*UserApi* | [**users_get**](docs/apis/tags/UserApi.md#users_get) | **get** /users/ | Your GET endpoint
*UserApi* | [**users_id_get**](docs/apis/tags/UserApi.md#users_id_get) | **get** /users/{id} | Individual User Profile
*UserApi* | [**users_id_put**](docs/apis/tags/UserApi.md#users_id_put) | **put** /users/{id} | Update Individual Profile
*UserApi* | [**users_post**](docs/apis/tags/UserApi.md#users_post) | **post** /users/ | 

## Documentation For Models

 - [AnalysisBase](docs/models/AnalysisBase.md)
 - [AnalysisCommon](docs/models/AnalysisCommon.md)
 - [AnalysisList](docs/models/AnalysisList.md)
 - [AnalysisRequest](docs/models/AnalysisRequest.md)
 - [AnalysisRequestRelationships](docs/models/AnalysisRequestRelationships.md)
 - [AnalysisReturn](docs/models/AnalysisReturn.md)
 - [AnalysisReturnRelationships](docs/models/AnalysisReturnRelationships.md)
 - [AnnotationBase](docs/models/AnnotationBase.md)
 - [AnnotationCommon](docs/models/AnnotationCommon.md)
 - [AnnotationExport](docs/models/AnnotationExport.md)
 - [AnnotationList](docs/models/AnnotationList.md)
 - [AnnotationRequest](docs/models/AnnotationRequest.md)
 - [AnnotationRequestRelationships](docs/models/AnnotationRequestRelationships.md)
 - [AnnotationReturn](docs/models/AnnotationReturn.md)
 - [AnnotationReturnRelationships](docs/models/AnnotationReturnRelationships.md)
 - [Clone](docs/models/Clone.md)
 - [ConditionBase](docs/models/ConditionBase.md)
 - [ConditionList](docs/models/ConditionList.md)
 - [ConditionRequest](docs/models/ConditionRequest.md)
 - [ConditionReturn](docs/models/ConditionReturn.md)
 - [Entity](docs/models/Entity.md)
 - [ImageBase](docs/models/ImageBase.md)
 - [ImageCommon](docs/models/ImageCommon.md)
 - [ImageList](docs/models/ImageList.md)
 - [ImageRelationships](docs/models/ImageRelationships.md)
 - [ImageRequest](docs/models/ImageRequest.md)
 - [ImageReturn](docs/models/ImageReturn.md)
 - [JsonLd](docs/models/JsonLd.md)
 - [Metadata](docs/models/Metadata.md)
 - [NestedPutAttributes](docs/models/NestedPutAttributes.md)
 - [NoteCollectionBase](docs/models/NoteCollectionBase.md)
 - [NoteCollectionRequest](docs/models/NoteCollectionRequest.md)
 - [NoteCollectionReturn](docs/models/NoteCollectionReturn.md)
 - [PointBase](docs/models/PointBase.md)
 - [PointCommon](docs/models/PointCommon.md)
 - [PointList](docs/models/PointList.md)
 - [PointRelationships](docs/models/PointRelationships.md)
 - [PointRequest](docs/models/PointRequest.md)
 - [PointReturn](docs/models/PointReturn.md)
 - [PointValue](docs/models/PointValue.md)
 - [ReadableResourceAttributes](docs/models/ReadableResourceAttributes.md)
 - [ResourceAttributes](docs/models/ResourceAttributes.md)
 - [StudyBase](docs/models/StudyBase.md)
 - [StudyList](docs/models/StudyList.md)
 - [StudyRequest](docs/models/StudyRequest.md)
 - [StudyRequestRelationships](docs/models/StudyRequestRelationships.md)
 - [StudyReturn](docs/models/StudyReturn.md)
 - [StudyReturnRelationships](docs/models/StudyReturnRelationships.md)
 - [StudysetBase](docs/models/StudysetBase.md)
 - [StudysetList](docs/models/StudysetList.md)
 - [StudysetRequest](docs/models/StudysetRequest.md)
 - [StudysetRequestRelationships](docs/models/StudysetRequestRelationships.md)
 - [StudysetReturn](docs/models/StudysetReturn.md)
 - [StudysetReturnRelationships](docs/models/StudysetReturnRelationships.md)
 - [User](docs/models/User.md)
 - [UserList](docs/models/UserList.md)
 - [UserResourceAttributes](docs/models/UserResourceAttributes.md)
 - [UserlessResourceAttributes](docs/models/UserlessResourceAttributes.md)
 - [WriteableResourceAttributes](docs/models/WriteableResourceAttributes.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## JSON-Web-Token

- **Type**: Bearer authentication


## Author

jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com
jamesdkent21@gmail.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in neurostore_sdk.apis and neurostore_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from neurostore_sdk.apis.default_api import DefaultApi`
- `from neurostore_sdk.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import neurostore_sdk
from neurostore_sdk.apis import *
from neurostore_sdk.models import *
```
