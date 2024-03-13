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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr
from neurostore_sdk.models.entity import Entity
from neurostore_sdk.models.point_relationships_values import PointRelationshipsValues

class PointRequest(BaseModel):
    """
    PointRequest
    """
    coordinates: Optional[conlist(Union[StrictFloat, StrictInt], max_items=3, min_items=3)] = Field(None, description="Location of the significant coordinate in three dimensional space.")
    space: Optional[StrictStr] = Field(None, description="Template space used to determine coordinate Examples include TAL or MNI.")
    kind: Optional[StrictStr] = Field(None, description="Method of how point was derived (e.g., center of mass)")
    label_id: Optional[StrictStr] = Field(None, description="If the point is associated with an image, this is the value the point takes in that image.")
    image: Optional[StrictStr] = None
    values: Optional[PointRelationshipsValues] = None
    x: Optional[Union[StrictFloat, StrictInt]] = None
    y: Optional[Union[StrictFloat, StrictInt]] = None
    z: Optional[Union[StrictFloat, StrictInt]] = None
    entities: Optional[conlist(Entity)] = None
    id: Optional[constr(strict=True, max_length=30, min_length=12)] = Field(None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(True, description="whether the resource is listed in public searches or not")
    analysis: Optional[StrictStr] = None
    cluster_size: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="size of the cluster in cubic millimeters")
    subpeak: Optional[StrictBool] = Field(None, description="whether the reported peak is the max-peak statistic or a sub-maxmimal peak.")
    order: Optional[StrictInt] = Field(None, description="determines the row to display the coordinate")
    __properties = ["coordinates", "space", "kind", "label_id", "image", "values", "x", "y", "z", "entities", "id", "public", "analysis", "cluster_size", "subpeak", "order"]

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
    def from_json(cls, json_str: str) -> PointRequest:
        """Create an instance of PointRequest from a JSON string"""
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
        # set to None if space (nullable) is None
        # and __fields_set__ contains the field
        if self.space is None and "space" in self.__fields_set__:
            _dict['space'] = None

        # set to None if kind (nullable) is None
        # and __fields_set__ contains the field
        if self.kind is None and "kind" in self.__fields_set__:
            _dict['kind'] = None

        # set to None if label_id (nullable) is None
        # and __fields_set__ contains the field
        if self.label_id is None and "label_id" in self.__fields_set__:
            _dict['label_id'] = None

        # set to None if image (nullable) is None
        # and __fields_set__ contains the field
        if self.image is None and "image" in self.__fields_set__:
            _dict['image'] = None

        # set to None if cluster_size (nullable) is None
        # and __fields_set__ contains the field
        if self.cluster_size is None and "cluster_size" in self.__fields_set__:
            _dict['cluster_size'] = None

        # set to None if subpeak (nullable) is None
        # and __fields_set__ contains the field
        if self.subpeak is None and "subpeak" in self.__fields_set__:
            _dict['subpeak'] = None

        # set to None if order (nullable) is None
        # and __fields_set__ contains the field
        if self.order is None and "order" in self.__fields_set__:
            _dict['order'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PointRequest:
        """Create an instance of PointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PointRequest.parse_obj(obj)

        _obj = PointRequest.parse_obj({
            "coordinates": obj.get("coordinates"),
            "space": obj.get("space"),
            "kind": obj.get("kind"),
            "label_id": obj.get("label_id"),
            "image": obj.get("image"),
            "values": PointRelationshipsValues.from_dict(obj.get("values")) if obj.get("values") is not None else None,
            "x": obj.get("x"),
            "y": obj.get("y"),
            "z": obj.get("z"),
            "entities": [Entity.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "id": obj.get("id"),
            "public": obj.get("public") if obj.get("public") is not None else True,
            "analysis": obj.get("analysis"),
            "cluster_size": obj.get("cluster_size"),
            "subpeak": obj.get("subpeak"),
            "order": obj.get("order")
        })
        return _obj

