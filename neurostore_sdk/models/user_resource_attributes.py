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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class UserResourceAttributes(BaseModel):
    """
    common resource attributes
    """
    user: Optional[StrictStr] = Field(None, description="who owns the resource")
    __properties = ["user"]

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
    def from_json(cls, json_str: str) -> UserResourceAttributes:
        """Create an instance of UserResourceAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "user",
                          },
                          exclude_none=True)
        # set to None if user (nullable) is None
        # and __fields_set__ contains the field
        if self.user is None and "user" in self.__fields_set__:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserResourceAttributes:
        """Create an instance of UserResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserResourceAttributes.parse_obj(obj)

        _obj = UserResourceAttributes.parse_obj({
            "user": obj.get("user")
        })
        return _obj

