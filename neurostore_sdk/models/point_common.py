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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class PointCommon(BaseModel):
    """
    PointCommon
    """
    analysis: Optional[StrictStr] = None
    cluster_size: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="size of the cluster in cubic millimeters")
    subpeak: Optional[StrictBool] = Field(None, description="whether the reported peak is the max-peak statistic or a sub-maxmimal peak.")
    __properties = ["analysis", "cluster_size", "subpeak"]

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
    def from_json(cls, json_str: str) -> PointCommon:
        """Create an instance of PointCommon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if cluster_size (nullable) is None
        # and __fields_set__ contains the field
        if self.cluster_size is None and "cluster_size" in self.__fields_set__:
            _dict['cluster_size'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PointCommon:
        """Create an instance of PointCommon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PointCommon.parse_obj(obj)

        _obj = PointCommon.parse_obj({
            "analysis": obj.get("analysis"),
            "cluster_size": obj.get("cluster_size"),
            "subpeak": obj.get("subpeak")
        })
        return _obj

