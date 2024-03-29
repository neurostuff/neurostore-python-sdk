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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist
from neurostore_sdk.models.entity import Entity

class ImageRelationships(BaseModel):
    """
    ImageRelationships
    """
    analysis: Optional[StrictStr] = None
    entities: Optional[conlist(Entity)] = None
    analysis_name: Optional[StrictStr] = None
    __properties = ["analysis", "entities", "analysis_name"]

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
    def from_json(cls, json_str: str) -> ImageRelationships:
        """Create an instance of ImageRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        # set to None if analysis_name (nullable) is None
        # and __fields_set__ contains the field
        if self.analysis_name is None and "analysis_name" in self.__fields_set__:
            _dict['analysis_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImageRelationships:
        """Create an instance of ImageRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ImageRelationships.parse_obj(obj)

        _obj = ImageRelationships.parse_obj({
            "analysis": obj.get("analysis"),
            "entities": [Entity.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "analysis_name": obj.get("analysis_name")
        })
        return _obj

