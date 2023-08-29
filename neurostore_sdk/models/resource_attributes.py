# coding: utf-8

"""
    neurostore api

    Create studysets for meta-analysis  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr

class ResourceAttributes(BaseModel):
    """
    common attributes for user owned resources
    """
    created_at: Optional[datetime] = Field(None, description="time the resource was created on the database")
    updated_at: Optional[StrictStr] = Field(None, description="when was the resource last modified/updated.")
    id: Optional[constr(strict=True, max_length=12, min_length=12)] = Field(None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(True, description="whether the resource is listed in public searches or not")
    user: Optional[StrictStr] = Field(None, description="who owns the resource")
    username: Optional[StrictStr] = Field(None, description="human readable username")
    __properties = ["created_at", "updated_at", "id", "public", "user", "username"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ResourceAttributes:
        """Create an instance of ResourceAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                            "updated_at",
                            "user",
                          },
                          exclude_none=True)
        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if user (nullable) is None
        # and __fields_set__ contains the field
        if self.user is None and "user" in self.__fields_set__:
            _dict['user'] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResourceAttributes:
        """Create an instance of ResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResourceAttributes.parse_obj(obj)

        _obj = ResourceAttributes.parse_obj({
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "id": obj.get("id"),
            "public": obj.get("public") if obj.get("public") is not None else True,
            "user": obj.get("user"),
            "username": obj.get("username")
        })
        return _obj

