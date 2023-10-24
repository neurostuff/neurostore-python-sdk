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
from pydantic import BaseModel, Field, StrictStr

class ReadableResourceAttributes(BaseModel):
    """
    common readable resource attributes
    """
    created_at: Optional[datetime] = Field(None, description="time the resource was created on the database")
    updated_at: Optional[StrictStr] = Field(None, description="when the resource was last modified/updated.")
    __properties = ["created_at", "updated_at"]

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
    def from_json(cls, json_str: str) -> ReadableResourceAttributes:
        """Create an instance of ReadableResourceAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                            "updated_at",
                          },
                          exclude_none=True)
        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReadableResourceAttributes:
        """Create an instance of ReadableResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReadableResourceAttributes.parse_obj(obj)

        _obj = ReadableResourceAttributes.parse_obj({
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

