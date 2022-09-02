"""
    neurostore api

    Create studysets for meta-analysis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from neurostore_sdk.endpoint import Endpoint as _Endpoint
from neurostore_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from neurostore_sdk.model.inline_response404 import InlineResponse404
from neurostore_sdk.model.inline_response422 import InlineResponse422
from neurostore_sdk.model.studyset_list import StudysetList
from neurostore_sdk.model.studyset_request import StudysetRequest
from neurostore_sdk.model.studyset_return import StudysetReturn


class StudysetsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client):
        self.api_client = api_client
        self.studysets_get_endpoint = _Endpoint(
            settings={
                'response_type': (StudysetList,),
                'auth': [
                    'JSON-Web-Token'
                ],
                'endpoint_path': '/studysets/',
                'operation_id': 'studysets_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'search',
                    'sort',
                    'page',
                    'desc',
                    'page_size',
                    'nested',
                    'name',
                    'description',
                    'source_id',
                    'unique',
                    'source',
                    'authors',
                    'user_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'source',
                ],
                'validation': [
                    'search',
                    'page',
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('search',): {

                        'min_length': 1,
                    },
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('page_size',): {

                        'exclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('source',): {

                        "NEUROSTORE": "neurostore",
                        "NEUROVAULT": "neurovault",
                        "PUBMED": "pubmed",
                        "NEUROSYNTH": "neurosynth",
                        "NEUROQUERY": "neuroquery"
                    },
                },
                'openapi_types': {
                    'search':
                        (str,),
                    'sort':
                        (str,),
                    'page':
                        (int,),
                    'desc':
                        (bool,),
                    'page_size':
                        (int,),
                    'nested':
                        (bool,),
                    'name':
                        (str,),
                    'description':
                        (str,),
                    'source_id':
                        (str,),
                    'unique':
                        (bool,),
                    'source':
                        (str,),
                    'authors':
                        (str,),
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'search': 'search',
                    'sort': 'sort',
                    'page': 'page',
                    'desc': 'desc',
                    'page_size': 'page_size',
                    'nested': 'nested',
                    'name': 'name',
                    'description': 'description',
                    'source_id': 'source_id',
                    'unique': 'unique',
                    'source': 'source',
                    'authors': 'authors',
                    'user_id': 'user_id',
                },
                'location_map': {
                    'search': 'query',
                    'sort': 'query',
                    'page': 'query',
                    'desc': 'query',
                    'page_size': 'query',
                    'nested': 'query',
                    'name': 'query',
                    'description': 'query',
                    'source_id': 'query',
                    'unique': 'query',
                    'source': 'query',
                    'authors': 'query',
                    'user_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.studysets_id_delete_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'JSON-Web-Token'
                ],
                'endpoint_path': '/studysets/{id}',
                'operation_id': 'studysets_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.studysets_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (StudysetReturn,),
                'auth': [],
                'endpoint_path': '/studysets/{id}',
                'operation_id': 'studysets_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'nested',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'nested':
                        (bool,),
                },
                'attribute_map': {
                    'id': 'id',
                    'nested': 'nested',
                },
                'location_map': {
                    'id': 'path',
                    'nested': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.studysets_id_put_endpoint = _Endpoint(
            settings={
                'response_type': (StudysetReturn,),
                'auth': [
                    'JSON-Web-Token'
                ],
                'endpoint_path': '/studysets/{id}',
                'operation_id': 'studysets_id_put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'studyset_request',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'studyset_request':
                        (StudysetRequest,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'studyset_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.studysets_post_endpoint = _Endpoint(
            settings={
                'response_type': (StudysetReturn,),
                'auth': [
                    'JSON-Web-Token'
                ],
                'endpoint_path': '/studysets/',
                'operation_id': 'studysets_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'studyset_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'studyset_request':
                        (StudysetRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'studyset_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get(
        self,
        **kwargs
    ):
        """GET a list of studysets  # noqa: E501

        Get a list of studysets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.studysets_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            search (str): search for entries that contain the substring. [optional]
            sort (str): Parameter to sort results on. [optional] if omitted the server will use the default value of "created_at"
            page (int): page of results. [optional]
            desc (bool): sort results by descending order (as opposed to ascending order). [optional]
            page_size (int): number of results to show on a page. [optional]
            nested (bool): whether to show the URI to a resource (false) or to embed the object in the response (true). [optional]
            name (str): search the name field for a term. [optional]
            description (str): search description field for a term. [optional]
            source_id (str): id of the resource you are either filtering/copying on. [optional]
            unique (bool): whether to list clones with originals. [optional]
            source (str): the source of the resource you would like to filter/copy from. [optional] if omitted the server will use the default value of "neurostore"
            authors (str): search authors. [optional]
            user_id (str): user id you want to filter by. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            StudysetList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.studysets_get_endpoint.call_with_http_info(**kwargs)

    def delete_id(
        self,
        id,
        **kwargs
    ):
        """DELETE a studyset  # noqa: E501

        delete a studyset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.studysets_id_delete(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.studysets_id_delete_endpoint.call_with_http_info(**kwargs)

    def get_id(
        self,
        id,
        **kwargs
    ):
        """GET a studyset  # noqa: E501

        Retrieve the information of a studyset with the matching studyset ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.studysets_id_get(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

        Keyword Args:
            nested (bool): whether to show the URI to a resource (false) or to embed the object in the response (true). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            StudysetReturn
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.studysets_id_get_endpoint.call_with_http_info(**kwargs)

    def put_id(
        self,
        id,
        **kwargs
    ):
        """PUT/update a studyset  # noqa: E501

        Update a studyset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.studysets_id_put(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

        Keyword Args:
            studyset_request (StudysetRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            StudysetReturn
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.studysets_id_put_endpoint.call_with_http_info(**kwargs)

    def post(
        self,
        **kwargs
    ):
        """POST/create a studyset  # noqa: E501

        Create a studyset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.studysets_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            studyset_request (StudysetRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            StudysetReturn
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.studysets_post_endpoint.call_with_http_info(**kwargs)

