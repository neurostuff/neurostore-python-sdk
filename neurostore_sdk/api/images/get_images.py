from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    search: str,
    sort: str = "created_at",
    page: int,
    desc: bool,
    page_size: int,
    filename: str,
    analysis_name: str,
    value_type: str,
    space: str,
) -> Dict[str, Any]:
    url = "{}/images/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["search"] = search

    params["sort"] = sort

    params["page"] = page

    params["desc"] = desc

    params["page_size"] = page_size

    params["filename"] = filename

    params["analysis_name"] = analysis_name

    params["value_type"] = value_type

    params["space"] = space

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
    client: Client,
    search: str,
    sort: str = "created_at",
    page: int,
    desc: bool,
    page_size: int,
    filename: str,
    analysis_name: str,
    value_type: str,
    space: str,
) -> Response[Any]:
    """GET a list of images

     Retrieve and list images.

    Args:
        search (str):  Example: imagin.
        sort (str):  Default: 'created_at'.
        page (int):
        desc (bool):
        page_size (int):
        filename (str):
        analysis_name (str):
        value_type (str):
        space (str):

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
        filename=filename,
        analysis_name=analysis_name,
        value_type=value_type,
        space=space,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    search: str,
    sort: str = "created_at",
    page: int,
    desc: bool,
    page_size: int,
    filename: str,
    analysis_name: str,
    value_type: str,
    space: str,
) -> Response[Any]:
    """GET a list of images

     Retrieve and list images.

    Args:
        search (str):  Example: imagin.
        sort (str):  Default: 'created_at'.
        page (int):
        desc (bool):
        page_size (int):
        filename (str):
        analysis_name (str):
        value_type (str):
        space (str):

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
        filename=filename,
        analysis_name=analysis_name,
        value_type=value_type,
        space=space,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)