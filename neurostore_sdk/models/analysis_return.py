# coding: utf-8

"""
    neurostore api

    Create studysets for meta-analysis

    The version of the OpenAPI document: 1.0
    Contact: jamesdkent21@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from neurostore_sdk.models.analysis_return_relationships_conditions import AnalysisReturnRelationshipsConditions
from neurostore_sdk.models.analysis_return_relationships_images import AnalysisReturnRelationshipsImages
from neurostore_sdk.models.analysis_return_relationships_points import AnalysisReturnRelationshipsPoints
from neurostore_sdk.models.entity import Entity
from typing import Optional, Set
from typing_extensions import Self

class AnalysisReturn(BaseModel):
    """
    AnalysisReturn
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="A name of the contrast being performed.")
    description: Optional[StrictStr] = Field(default=None, description="A long form description of how the contrast was performed")
    weights: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="Weight applied to each condition, must be the same length as the conditions attribute.")
    created_at: Optional[datetime] = Field(default=None, description="time the resource was created on the database")
    updated_at: Optional[StrictStr] = Field(default=None, description="when the resource was last modified/updated.")
    id: Optional[Annotated[str, Field(min_length=12, strict=True, max_length=30)]] = Field(default=None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(default=True, description="whether the resource is listed in public searches or not")
    user: Optional[StrictStr] = Field(default=None, description="who owns the resource")
    username: Optional[StrictStr] = Field(default=None, description="human readable username")
    study: Optional[StrictStr] = None
    images: Optional[AnalysisReturnRelationshipsImages] = None
    points: Optional[AnalysisReturnRelationshipsPoints] = None
    conditions: Optional[AnalysisReturnRelationshipsConditions] = None
    entities: Optional[List[Entity]] = None
    order: Optional[StrictInt] = None
    metadata: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["name", "description", "weights", "created_at", "updated_at", "id", "public", "user", "username", "study", "images", "points", "conditions", "entities", "order", "metadata"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AnalysisReturn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "updated_at",
            "user",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
            for _item_entities in self.entities:
                if _item_entities:
                    _items.append(_item_entities.to_dict())
            _dict['entities'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnalysisReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
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
            "images": AnalysisReturnRelationshipsImages.from_dict(obj["images"]) if obj.get("images") is not None else None,
            "points": AnalysisReturnRelationshipsPoints.from_dict(obj["points"]) if obj.get("points") is not None else None,
            "conditions": AnalysisReturnRelationshipsConditions.from_dict(obj["conditions"]) if obj.get("conditions") is not None else None,
            "entities": [Entity.from_dict(_item) for _item in obj["entities"]] if obj.get("entities") is not None else None,
            "order": obj.get("order"),
            "metadata": obj.get("metadata")
        })
        return _obj


