from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_studies_data_type import GetStudiesDataType
from ...models.get_studies_source import GetStudiesSource
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    search: str,
    sort: str = "created_at",
    page: int,
    desc: bool,
    page_size: int,
    nested: bool,
    name: str,
    description: str,
    source_id: str,
    unique: Any,
    source: GetStudiesSource = GetStudiesSource.NEUROSTORE,
    authors: str,
    user_id: str,
    data_type: GetStudiesDataType,
    studyset_owner: str,
) -> Dict[str, Any]:
    url = "{}/studies/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["search"] = search

    params["sort"] = sort

    params["page"] = page

    params["desc"] = desc

    params["page_size"] = page_size

    params["nested"] = nested

    params["name"] = name

    params["description"] = description

    params["source_id"] = source_id

    params["unique"] = unique

    json_source = source.value

    params["source"] = json_source

    params["authors"] = authors

    params["user_id"] = user_id

    json_data_type = data_type.value

    params["data_type"] = json_data_type

    params["studyset_owner"] = studyset_owner

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    search: str,
    sort: str = "created_at",
    page: int,
    desc: bool,
    page_size: int,
    nested: bool,
    name: str,
    description: str,
    source_id: str,
    unique: Any,
    source: GetStudiesSource = GetStudiesSource.NEUROSTORE,
    authors: str,
    user_id: str,
    data_type: GetStudiesDataType,
    studyset_owner: str,
) -> Response[Any]:
    """GET a list of studies

     List studies

    Args:
        search (str):  Example: imagin.
        sort (str):  Default: 'created_at'.
        page (int):
        desc (bool):
        page_size (int):
        nested (bool):
        name (str):
        description (str):
        source_id (str):  Example: 1234567890ab.
        unique (Any):
        source (GetStudiesSource):  Default: GetStudiesSource.NEUROSTORE. Example: neurostore.
        authors (str):
        user_id (str):
        data_type (GetStudiesDataType):
        studyset_owner (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        search=search,
        sort=sort,
        page=page,
        desc=desc,
        page_size=page_size,
        nested=nested,
        name=name,
        description=description,
        source_id=source_id,
        unique=unique,
        source=source,
        authors=authors,
        user_id=user_id,
        data_type=data_type,
        studyset_owner=studyset_owner,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search: str,
    sort: str = "created_at",
    page: int,
    desc: bool,
    page_size: int,
    nested: bool,
    name: str,
    description: str,
    source_id: str,
    unique: Any,
    source: GetStudiesSource = GetStudiesSource.NEUROSTORE,
    authors: str,
    user_id: str,
    data_type: GetStudiesDataType,
    studyset_owner: str,
) -> Response[Any]:
    """GET a list of studies

     List studies

    Args:
        search (str):  Example: imagin.
        sort (str):  Default: 'created_at'.
        page (int):
        desc (bool):
        page_size (int):
        nested (bool):
        name (str):
        description (str):
        source_id (str):  Example: 1234567890ab.
        unique (Any):
        source (GetStudiesSource):  Default: GetStudiesSource.NEUROSTORE. Example: neurostore.
        authors (str):
        user_id (str):
        data_type (GetStudiesDataType):
        studyset_owner (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        search=search,
        sort=sort,
        page=page,
        desc=desc,
        page_size=page_size,
        nested=nested,
        name=name,
        description=description,
        source_id=source_id,
        unique=unique,
        source=source,
        authors=authors,
        user_id=user_id,
        data_type=data_type,
        studyset_owner=studyset_owner,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
