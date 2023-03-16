# coding: utf-8

"""
    neurostore api

    Create studysets for meta-analysis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by: https://openapi-generator.tech
"""

from neurostore_sdk.paths.users_.get import UsersGet
from neurostore_sdk.paths.users_id.get import UsersIdGet
from neurostore_sdk.paths.users_id.put import UsersIdPut
from neurostore_sdk.paths.users_.post import UsersPost


class UserApi(
    UsersGet,
    UsersIdGet,
    UsersIdPut,
    UsersPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass