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
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr
from neurostore_sdk.models.analysis_return_relationships_conditions import AnalysisReturnRelationshipsConditions
from neurostore_sdk.models.analysis_return_relationships_images import AnalysisReturnRelationshipsImages
from neurostore_sdk.models.analysis_return_relationships_points import AnalysisReturnRelationshipsPoints
from neurostore_sdk.models.entity import Entity

class AnalysisReturn(BaseModel):
    """
    AnalysisReturn
    """
    name: Optional[StrictStr] = Field(None, description="A name of the contrast being performed.")
    description: Optional[StrictStr] = Field(None, description="A long form description of how the contrast was performed")
    weights: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(None, description="Weight applied to each condition, must be the same length as the conditions attribute.")
    created_at: Optional[datetime] = Field(None, description="time the resource was created on the database")
    updated_at: Optional[StrictStr] = Field(None, description="when the resource was last modified/updated.")
    id: Optional[constr(strict=True, max_length=30, min_length=12)] = Field(None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(True, description="whether the resource is listed in public searches or not")
    user: Optional[StrictStr] = Field(None, description="who owns the resource")
    username: Optional[StrictStr] = Field(None, description="human readable username")
    study: Optional[StrictStr] = None
    images: Optional[AnalysisReturnRelationshipsImages] = None
    points: Optional[AnalysisReturnRelationshipsPoints] = None
    conditions: Optional[AnalysisReturnRelationshipsConditions] = None
    entities: Optional[conlist(Entity)] = None
    order: Optional[StrictInt] = None
    metadata: Optional[Dict[str, Any]] = None
    __properties = ["name", "description", "weights", "created_at", "updated_at", "id", "public", "user", "username", "study", "images", "points", "conditions", "entities", "order", "metadata"]

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
    def from_json(cls, json_str: str) -> AnalysisReturn:
        """Create an instance of AnalysisReturn from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of images
        if self.images:
            _dict['images'] = self.images.to_dict()
        # override the default output from pydantic by calling `to_dict()` of points
        if self.points:
            _dict['points'] = self.points.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

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

        # set to None if order (nullable) is None
        # and __fields_set__ contains the field
        if self.order is None and "order" in self.__fields_set__:
            _dict['order'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnalysisReturn:
        """Create an instance of AnalysisReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AnalysisReturn.parse_obj(obj)

        _obj = AnalysisReturn.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "weights": obj.get("weights"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "id": obj.get("id"),
            "public": obj.get("public") if obj.get("public") is not None else True,
            "user": obj.get("user"),
            "username": obj.get("username"),
            "study": obj.get("study"),
            "images": AnalysisReturnRelationshipsImages.from_dict(obj.get("images")) if obj.get("images") is not None else None,
            "points": AnalysisReturnRelationshipsPoints.from_dict(obj.get("points")) if obj.get("points") is not None else None,
            "conditions": AnalysisReturnRelationshipsConditions.from_dict(obj.get("conditions")) if obj.get("conditions") is not None else None,
            "entities": [Entity.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "order": obj.get("order"),
            "metadata": obj.get("metadata")
        })
        return _obj

