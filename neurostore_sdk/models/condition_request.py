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
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr

class ConditionRequest(BaseModel):
    """
    ConditionRequest
    """
    name: Optional[StrictStr] = Field(None, description="Name of the condition being applied in the contrast, either psychological, pharmacological, or group based.")
    description: Optional[StrictStr] = Field(None, description="Long form description of how the condition is operationalized and/or specific meaning.")
    id: Optional[constr(strict=True, max_length=12, min_length=12)] = Field(None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(True, description="whether the resource is listed in public searches or not")
    __properties = ["name", "description", "id", "public"]

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
    def from_json(cls, json_str: str) -> ConditionRequest:
        """Create an instance of ConditionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConditionRequest:
        """Create an instance of ConditionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConditionRequest.parse_obj(obj)

        _obj = ConditionRequest.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "public": obj.get("public") if obj.get("public") is not None else True
        })
        return _obj

