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


from typing import List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, conlist
from neurostore_sdk.models.entity import Entity
from neurostore_sdk.models.point_relationships_values import PointRelationshipsValues

class PointRelationships(BaseModel):
    """
    PointRelationships
    """
    image: Optional[StrictStr] = None
    values: Optional[PointRelationshipsValues] = None
    x: Optional[Union[StrictFloat, StrictInt]] = None
    y: Optional[Union[StrictFloat, StrictInt]] = None
    z: Optional[Union[StrictFloat, StrictInt]] = None
    entities: Optional[conlist(Entity)] = None
    __properties = ["image", "values", "x", "y", "z", "entities"]

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
    def from_json(cls, json_str: str) -> PointRelationships:
        """Create an instance of PointRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of values
        if self.values:
            _dict['values'] = self.values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        # set to None if image (nullable) is None
        # and __fields_set__ contains the field
        if self.image is None and "image" in self.__fields_set__:
            _dict['image'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PointRelationships:
        """Create an instance of PointRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PointRelationships.parse_obj(obj)

        _obj = PointRelationships.parse_obj({
            "image": obj.get("image"),
            "values": PointRelationshipsValues.from_dict(obj.get("values")) if obj.get("values") is not None else None,
            "x": obj.get("x"),
            "y": obj.get("y"),
            "z": obj.get("z"),
            "entities": [Entity.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None
        })
        return _obj

