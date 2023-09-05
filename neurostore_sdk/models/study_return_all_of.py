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
from pydantic import BaseModel, StrictBool, conlist
from neurostore_sdk.models.study_return_all_of_studysets_inner import StudyReturnAllOfStudysetsInner

class StudyReturnAllOf(BaseModel):
    """
    StudyReturnAllOf
    """
    studysets: Optional[conlist(StudyReturnAllOfStudysetsInner)] = None
    has_coordinates: Optional[StrictBool] = None
    has_images: Optional[StrictBool] = None
    __properties = ["studysets", "has_coordinates", "has_images"]

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
    def from_json(cls, json_str: str) -> StudyReturnAllOf:
        """Create an instance of StudyReturnAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in studysets (list)
        _items = []
        if self.studysets:
            for _item in self.studysets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['studysets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudyReturnAllOf:
        """Create an instance of StudyReturnAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudyReturnAllOf.parse_obj(obj)

        _obj = StudyReturnAllOf.parse_obj({
            "studysets": [StudyReturnAllOfStudysetsInner.from_dict(_item) for _item in obj.get("studysets")] if obj.get("studysets") is not None else None,
            "has_coordinates": obj.get("has_coordinates"),
            "has_images": obj.get("has_images")
        })
        return _obj

