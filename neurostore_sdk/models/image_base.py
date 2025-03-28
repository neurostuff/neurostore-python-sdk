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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ImageBase(BaseModel):
    """
    ImageBase
    """ # noqa: E501
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Metadata about image such as software and version used and other relevant data about how the image was produced.")
    url: Optional[StrictStr] = Field(default=None, description="URL to image file.")
    filename: Optional[StrictStr] = Field(default=None, description="Name of the image file.")
    space: Optional[StrictStr] = Field(default=None, description="The template space the image is in (e.g., MNI ")
    value_type: Optional[StrictStr] = Field(default=None, description="The values the image represents. For example, T-statistic or Z-statistic, or Betas.")
    add_date: Optional[datetime] = Field(default=None, description="Date the image was added.")
    __properties: ClassVar[List[str]] = ["metadata", "url", "filename", "space", "value_type", "add_date"]

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
        """Create an instance of ImageBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "add_date",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if filename (nullable) is None
        # and model_fields_set contains the field
        if self.filename is None and "filename" in self.model_fields_set:
            _dict['filename'] = None

        # set to None if space (nullable) is None
        # and model_fields_set contains the field
        if self.space is None and "space" in self.model_fields_set:
            _dict['space'] = None

        # set to None if value_type (nullable) is None
        # and model_fields_set contains the field
        if self.value_type is None and "value_type" in self.model_fields_set:
            _dict['value_type'] = None

        # set to None if add_date (nullable) is None
        # and model_fields_set contains the field
        if self.add_date is None and "add_date" in self.model_fields_set:
            _dict['add_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImageBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": obj.get("metadata"),
            "url": obj.get("url"),
            "filename": obj.get("filename"),
            "space": obj.get("space"),
            "value_type": obj.get("value_type"),
            "add_date": obj.get("add_date")
        })
        return _obj


