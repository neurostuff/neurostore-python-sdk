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
from pydantic import BaseModel, StrictInt, StrictStr, validator

class StudysetsIdGet404Response(BaseModel):
    """
    StudysetsIdGet404Response
    """
    detail: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties = ["detail", "status", "title", "type"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (404):
            raise ValueError("must be one of enum values (404)")
        return value

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
    def from_json(cls, json_str: str) -> StudysetsIdGet404Response:
        """Create an instance of StudysetsIdGet404Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudysetsIdGet404Response:
        """Create an instance of StudysetsIdGet404Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudysetsIdGet404Response.parse_obj(obj)

        _obj = StudysetsIdGet404Response.parse_obj({
            "detail": obj.get("detail"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "type": obj.get("type")
        })
        return _obj

