# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from neurostore_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from neurostore_sdk import schemas  # noqa: F401

from neurostore_sdk.model.study_list import StudyList

# Query params


class SearchSchema(
    schemas.StrSchema
):
    pass
SortSchema = schemas.StrSchema


class PageSchema(
    schemas.Int32Schema
):
    pass
DescSchema = schemas.BoolSchema


class PageSizeSchema(
    schemas.Int32Schema
):
    pass
NestedSchema = schemas.BoolSchema
NameSchema = schemas.StrSchema
DescriptionSchema = schemas.StrSchema
SourceIdSchema = schemas.StrSchema
UniqueSchema = schemas.AnyTypeSchema


class SourceSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def NEUROSTORE(cls):
        return cls("neurostore")
    
    @schemas.classproperty
    def NEUROVAULT(cls):
        return cls("neurovault")
    
    @schemas.classproperty
    def PUBMED(cls):
        return cls("pubmed")
    
    @schemas.classproperty
    def NEUROSYNTH(cls):
        return cls("neurosynth")
    
    @schemas.classproperty
    def NEUROQUERY(cls):
        return cls("neuroquery")
AuthorsSchema = schemas.StrSchema
UserIdSchema = schemas.StrSchema


class DataTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def COORDINATE(cls):
        return cls("coordinate")
    
    @schemas.classproperty
    def IMAGE(cls):
        return cls("image")
    
    @schemas.classproperty
    def BOTH(cls):
        return cls("both")
StudysetOwnerSchema = schemas.StrSchema


class LevelSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def GROUP(cls):
        return cls("group")
    
    @schemas.classproperty
    def META(cls):
        return cls("meta")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'search': typing.Union[SearchSchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'desc': typing.Union[DescSchema, bool, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'nested': typing.Union[NestedSchema, bool, ],
        'name': typing.Union[NameSchema, str, ],
        'description': typing.Union[DescriptionSchema, str, ],
        'source_id': typing.Union[SourceIdSchema, str, ],
        'unique': typing.Union[UniqueSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'source': typing.Union[SourceSchema, str, ],
        'authors': typing.Union[AuthorsSchema, str, ],
        'user_id': typing.Union[UserIdSchema, str, ],
        'data_type': typing.Union[DataTypeSchema, str, ],
        'studyset_owner': typing.Union[StudysetOwnerSchema, str, ],
        'level': typing.Union[LevelSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_desc = api_client.QueryParameter(
    name="desc",
    style=api_client.ParameterStyle.FORM,
    schema=DescSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_nested = api_client.QueryParameter(
    name="nested",
    style=api_client.ParameterStyle.FORM,
    schema=NestedSchema,
    explode=True,
)
request_query_name = api_client.QueryParameter(
    name="name",
    style=api_client.ParameterStyle.FORM,
    schema=NameSchema,
    explode=True,
)
request_query_description = api_client.QueryParameter(
    name="description",
    style=api_client.ParameterStyle.FORM,
    schema=DescriptionSchema,
    explode=True,
)
request_query_source_id = api_client.QueryParameter(
    name="source_id",
    style=api_client.ParameterStyle.FORM,
    schema=SourceIdSchema,
    explode=True,
)
request_query_unique = api_client.QueryParameter(
    name="unique",
    style=api_client.ParameterStyle.FORM,
    schema=UniqueSchema,
    explode=True,
)
request_query_source = api_client.QueryParameter(
    name="source",
    style=api_client.ParameterStyle.FORM,
    schema=SourceSchema,
    explode=True,
)
request_query_authors = api_client.QueryParameter(
    name="authors",
    style=api_client.ParameterStyle.FORM,
    schema=AuthorsSchema,
    explode=True,
)
request_query_user_id = api_client.QueryParameter(
    name="user_id",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdSchema,
    explode=True,
)
request_query_data_type = api_client.QueryParameter(
    name="data_type",
    style=api_client.ParameterStyle.FORM,
    schema=DataTypeSchema,
    explode=True,
)
request_query_studyset_owner = api_client.QueryParameter(
    name="studyset_owner",
    style=api_client.ParameterStyle.FORM,
    schema=StudysetOwnerSchema,
    explode=True,
)
request_query_level = api_client.QueryParameter(
    name="level",
    style=api_client.ParameterStyle.FORM,
    schema=LevelSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = StudyList


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _studies_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _studies_get_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _studies_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _studies_get_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        GET a list of studies
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_search,
            request_query_sort,
            request_query_page,
            request_query_desc,
            request_query_page_size,
            request_query_nested,
            request_query_name,
            request_query_description,
            request_query_source_id,
            request_query_unique,
            request_query_source,
            request_query_authors,
            request_query_user_id,
            request_query_data_type,
            request_query_studyset_owner,
            request_query_level,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class StudiesGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def studies_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def studies_get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def studies_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def studies_get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._studies_get_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._studies_get_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


