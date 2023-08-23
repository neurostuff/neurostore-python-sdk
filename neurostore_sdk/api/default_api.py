# coding: utf-8

"""
    neurostore api

    Create studysets for meta-analysis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr, conint, constr

from typing import Optional

from neurostore_sdk.models.base_study import BaseStudy
from neurostore_sdk.models.base_study_list import BaseStudyList
from neurostore_sdk.models.base_study_return import BaseStudyReturn

from neurostore_sdk.api_client import ApiClient
from neurostore_sdk.api_response import ApiResponse
from neurostore_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def base_studies_get(self, search : Annotated[Optional[constr(strict=True, min_length=1)], Field(description="search for entries that contain the substring")] = None, sort : Annotated[Optional[StrictStr], Field(description="Parameter to sort results on")] = None, page : Annotated[Optional[conint(strict=True, ge=0)], Field(description="page of results")] = None, desc : Annotated[Optional[StrictBool], Field(description="sort results by descending order (as opposed to ascending order)")] = None, page_size : Annotated[Optional[conint(strict=True, lt=30000, ge=1)], Field(description="number of results to show on a page")] = None, name : Annotated[Optional[StrictStr], Field(description="search the name field for a term")] = None, description : Annotated[Optional[StrictStr], Field(description="search description field for a term")] = None, authors : Annotated[Optional[StrictStr], Field(description="search authors")] = None, level : Annotated[Optional[StrictStr], Field(description="select between studies with group results or meta results")] = None, data_type : Annotated[Optional[StrictStr], Field(description="whether searching for studies that contain coordinates, images, or both")] = None, publication : Annotated[Optional[StrictStr], Field(description="search for papers from a particular journal")] = None, pmid : Annotated[Optional[StrictStr], Field(description="search for particular pmid")] = None, doi : Annotated[Optional[StrictStr], Field(description="search for study with specific doi")] = None, flat : Annotated[Optional[StrictBool], Field(description="do not return any embedded relationships. When set, it is incompatible with nested. ")] = None, info : Annotated[Optional[StrictBool], Field(description="show additional for endpoint-object relationships without being fully nested. Incompatible with nested")] = None, **kwargs) -> BaseStudyList:  # noqa: E501
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.base_studies_get(search, sort, page, desc, page_size, name, description, authors, level, data_type, publication, pmid, doi, flat, info, async_req=True)
        >>> result = thread.get()

        :param search: search for entries that contain the substring
        :type search: str
        :param sort: Parameter to sort results on
        :type sort: str
        :param page: page of results
        :type page: int
        :param desc: sort results by descending order (as opposed to ascending order)
        :type desc: bool
        :param page_size: number of results to show on a page
        :type page_size: int
        :param name: search the name field for a term
        :type name: str
        :param description: search description field for a term
        :type description: str
        :param authors: search authors
        :type authors: str
        :param level: select between studies with group results or meta results
        :type level: str
        :param data_type: whether searching for studies that contain coordinates, images, or both
        :type data_type: str
        :param publication: search for papers from a particular journal
        :type publication: str
        :param pmid: search for particular pmid
        :type pmid: str
        :param doi: search for study with specific doi
        :type doi: str
        :param flat: do not return any embedded relationships. When set, it is incompatible with nested. 
        :type flat: bool
        :param info: show additional for endpoint-object relationships without being fully nested. Incompatible with nested
        :type info: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BaseStudyList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the base_studies_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.base_studies_get_with_http_info(search, sort, page, desc, page_size, name, description, authors, level, data_type, publication, pmid, doi, flat, info, **kwargs)  # noqa: E501

    @validate_arguments
    def base_studies_get_with_http_info(self, search : Annotated[Optional[constr(strict=True, min_length=1)], Field(description="search for entries that contain the substring")] = None, sort : Annotated[Optional[StrictStr], Field(description="Parameter to sort results on")] = None, page : Annotated[Optional[conint(strict=True, ge=0)], Field(description="page of results")] = None, desc : Annotated[Optional[StrictBool], Field(description="sort results by descending order (as opposed to ascending order)")] = None, page_size : Annotated[Optional[conint(strict=True, lt=30000, ge=1)], Field(description="number of results to show on a page")] = None, name : Annotated[Optional[StrictStr], Field(description="search the name field for a term")] = None, description : Annotated[Optional[StrictStr], Field(description="search description field for a term")] = None, authors : Annotated[Optional[StrictStr], Field(description="search authors")] = None, level : Annotated[Optional[StrictStr], Field(description="select between studies with group results or meta results")] = None, data_type : Annotated[Optional[StrictStr], Field(description="whether searching for studies that contain coordinates, images, or both")] = None, publication : Annotated[Optional[StrictStr], Field(description="search for papers from a particular journal")] = None, pmid : Annotated[Optional[StrictStr], Field(description="search for particular pmid")] = None, doi : Annotated[Optional[StrictStr], Field(description="search for study with specific doi")] = None, flat : Annotated[Optional[StrictBool], Field(description="do not return any embedded relationships. When set, it is incompatible with nested. ")] = None, info : Annotated[Optional[StrictBool], Field(description="show additional for endpoint-object relationships without being fully nested. Incompatible with nested")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.base_studies_get_with_http_info(search, sort, page, desc, page_size, name, description, authors, level, data_type, publication, pmid, doi, flat, info, async_req=True)
        >>> result = thread.get()

        :param search: search for entries that contain the substring
        :type search: str
        :param sort: Parameter to sort results on
        :type sort: str
        :param page: page of results
        :type page: int
        :param desc: sort results by descending order (as opposed to ascending order)
        :type desc: bool
        :param page_size: number of results to show on a page
        :type page_size: int
        :param name: search the name field for a term
        :type name: str
        :param description: search description field for a term
        :type description: str
        :param authors: search authors
        :type authors: str
        :param level: select between studies with group results or meta results
        :type level: str
        :param data_type: whether searching for studies that contain coordinates, images, or both
        :type data_type: str
        :param publication: search for papers from a particular journal
        :type publication: str
        :param pmid: search for particular pmid
        :type pmid: str
        :param doi: search for study with specific doi
        :type doi: str
        :param flat: do not return any embedded relationships. When set, it is incompatible with nested. 
        :type flat: bool
        :param info: show additional for endpoint-object relationships without being fully nested. Incompatible with nested
        :type info: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BaseStudyList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'search',
            'sort',
            'page',
            'desc',
            'page_size',
            'name',
            'description',
            'authors',
            'level',
            'data_type',
            'publication',
            'pmid',
            'doi',
            'flat',
            'info'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method base_studies_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('desc') is not None:  # noqa: E501
            _query_params.append(('desc', _params['desc']))

        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('page_size', _params['page_size']))

        if _params.get('name') is not None:  # noqa: E501
            _query_params.append(('name', _params['name']))

        if _params.get('description') is not None:  # noqa: E501
            _query_params.append(('description', _params['description']))

        if _params.get('authors') is not None:  # noqa: E501
            _query_params.append(('authors', _params['authors']))

        if _params.get('level') is not None:  # noqa: E501
            _query_params.append(('level', _params['level'].value))

        if _params.get('data_type') is not None:  # noqa: E501
            _query_params.append(('data_type', _params['data_type'].value))

        if _params.get('publication') is not None:  # noqa: E501
            _query_params.append(('publication', _params['publication']))

        if _params.get('pmid') is not None:  # noqa: E501
            _query_params.append(('pmid', _params['pmid']))

        if _params.get('doi') is not None:  # noqa: E501
            _query_params.append(('doi', _params['doi']))

        if _params.get('flat') is not None:  # noqa: E501
            _query_params.append(('flat', _params['flat'].value))

        if _params.get('info') is not None:  # noqa: E501
            _query_params.append(('info', _params['info']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['JSON-Web-Token']  # noqa: E501

        _response_types_map = {
            '200': "BaseStudyList",
        }

        return self.api_client.call_api(
            '/base-studies/', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def base_studies_id_get(self, id : StrictStr, flat : Annotated[Optional[StrictBool], Field(description="do not return any embedded relationships. When set, it is incompatible with nested. ")] = None, info : Annotated[Optional[StrictBool], Field(description="show additional for endpoint-object relationships without being fully nested. Incompatible with nested")] = None, **kwargs) -> BaseStudyReturn:  # noqa: E501
        """Your GET endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.base_studies_id_get(id, flat, info, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param flat: do not return any embedded relationships. When set, it is incompatible with nested. 
        :type flat: bool
        :param info: show additional for endpoint-object relationships without being fully nested. Incompatible with nested
        :type info: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BaseStudyReturn
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the base_studies_id_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.base_studies_id_get_with_http_info(id, flat, info, **kwargs)  # noqa: E501

    @validate_arguments
    def base_studies_id_get_with_http_info(self, id : StrictStr, flat : Annotated[Optional[StrictBool], Field(description="do not return any embedded relationships. When set, it is incompatible with nested. ")] = None, info : Annotated[Optional[StrictBool], Field(description="show additional for endpoint-object relationships without being fully nested. Incompatible with nested")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Your GET endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.base_studies_id_get_with_http_info(id, flat, info, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param flat: do not return any embedded relationships. When set, it is incompatible with nested. 
        :type flat: bool
        :param info: show additional for endpoint-object relationships without being fully nested. Incompatible with nested
        :type info: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BaseStudyReturn, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'flat',
            'info'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method base_studies_id_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('flat') is not None:  # noqa: E501
            _query_params.append(('flat', _params['flat'].value))

        if _params.get('info') is not None:  # noqa: E501
            _query_params.append(('info', _params['info']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "BaseStudyReturn",
        }

        return self.api_client.call_api(
            '/base-studies/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def base_studies_id_put(self, id : StrictStr, base_study : Optional[BaseStudy] = None, **kwargs) -> BaseStudyReturn:  # noqa: E501
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.base_studies_id_put(id, base_study, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param base_study:
        :type base_study: BaseStudy
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BaseStudyReturn
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the base_studies_id_put_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.base_studies_id_put_with_http_info(id, base_study, **kwargs)  # noqa: E501

    @validate_arguments
    def base_studies_id_put_with_http_info(self, id : StrictStr, base_study : Optional[BaseStudy] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.base_studies_id_put_with_http_info(id, base_study, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param base_study:
        :type base_study: BaseStudy
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BaseStudyReturn, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'base_study'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method base_studies_id_put" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['base_study'] is not None:
            _body_params = _params['base_study']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['JSON-Web-Token']  # noqa: E501

        _response_types_map = {
            '200': "BaseStudyReturn",
        }

        return self.api_client.call_api(
            '/base-studies/{id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def base_studies_post(self, base_study : Optional[BaseStudy] = None, **kwargs) -> BaseStudyList:  # noqa: E501
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.base_studies_post(base_study, async_req=True)
        >>> result = thread.get()

        :param base_study:
        :type base_study: BaseStudy
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BaseStudyList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the base_studies_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.base_studies_post_with_http_info(base_study, **kwargs)  # noqa: E501

    @validate_arguments
    def base_studies_post_with_http_info(self, base_study : Optional[BaseStudy] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.base_studies_post_with_http_info(base_study, async_req=True)
        >>> result = thread.get()

        :param base_study:
        :type base_study: BaseStudy
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BaseStudyList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'base_study'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method base_studies_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['base_study'] is not None:
            _body_params = _params['base_study']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['JSON-Web-Token']  # noqa: E501

        _response_types_map = {
            '200': "BaseStudyList",
        }

        return self.api_client.call_api(
            '/base-studies/', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
