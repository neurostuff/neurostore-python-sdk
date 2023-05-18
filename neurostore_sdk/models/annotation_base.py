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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class AnnotationBase(BaseModel):
    """
    AnnotationBase
    """
    name: Optional[StrictStr] = Field(None, description="Descriptive name for the annotation.")
    description: Optional[StrictStr] = Field(None, description="Long form description of the annotation.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="object describing metadata about the annotation, such as software used or descriptions of the keys used in the annotation.")
    note_keys: Optional[Dict[str, Any]] = Field(None, description="The keys (columns) in the annotation and the key's respective data type (such as an integer or string).")
    __properties = ["name", "description", "metadata", "note_keys"]

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
    def from_json(cls, json_str: str) -> AnnotationBase:
        """Create an instance of AnnotationBase from a JSON string"""
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

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if note_keys (nullable) is None
        # and __fields_set__ contains the field
        if self.note_keys is None and "note_keys" in self.__fields_set__:
            _dict['note_keys'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnnotationBase:
        """Create an instance of AnnotationBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AnnotationBase.parse_obj(obj)

        _obj = AnnotationBase.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "metadata": obj.get("metadata"),
            "note_keys": obj.get("note_keys")
        })
        return _obj

