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
from pydantic import BaseModel, conlist
from neurostore_sdk.models.annotation_request_relationships_notes_inner import AnnotationRequestRelationshipsNotesInner

class AnnotationRequestRelationships(BaseModel):
    """
    AnnotationRequestRelationships
    """
    notes: Optional[conlist(AnnotationRequestRelationshipsNotesInner)] = None
    __properties = ["notes"]

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
    def from_json(cls, json_str: str) -> AnnotationRequestRelationships:
        """Create an instance of AnnotationRequestRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnnotationRequestRelationships:
        """Create an instance of AnnotationRequestRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AnnotationRequestRelationships.parse_obj(obj)

        _obj = AnnotationRequestRelationships.parse_obj({
            "notes": [AnnotationRequestRelationshipsNotesInner.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None
        })
        return _obj

