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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class StudysetRequest(BaseModel):
    """
    StudysetRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Descriptive and human readable name of the studyset.")
    description: Optional[StrictStr] = Field(default=None, description="A longform description of the studyset.")
    publication: Optional[StrictStr] = Field(default=None, description="The journal/source the studyset is connected to if the studyset was published.")
    doi: Optional[StrictStr] = Field(default=None, description="A DOI connected to the published studyset (may change to being automatically created so each studyset connected to a successful meta-analysis gets a DOI).")
    pmid: Optional[StrictStr] = Field(default=None, description="If the article connected to the studyset was published on PubMed, then link the ID here.")
    studies: Optional[List[Dict[str, Any]]] = None
    id: Optional[Annotated[str, Field(min_length=12, strict=True, max_length=30)]] = Field(default=None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(default=True, description="whether the resource is listed in public searches or not")
    level: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "description", "publication", "doi", "pmid", "studies", "id", "public", "level"]

    @field_validator('level')
    def level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['group', 'meta']):
            raise ValueError("must be one of enum values ('group', 'meta')")
        return value

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
        """Create an instance of StudysetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if publication (nullable) is None
        # and model_fields_set contains the field
        if self.publication is None and "publication" in self.model_fields_set:
            _dict['publication'] = None

        # set to None if doi (nullable) is None
        # and model_fields_set contains the field
        if self.doi is None and "doi" in self.model_fields_set:
            _dict['doi'] = None

        # set to None if pmid (nullable) is None
        # and model_fields_set contains the field
        if self.pmid is None and "pmid" in self.model_fields_set:
            _dict['pmid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StudysetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "publication": obj.get("publication"),
            "doi": obj.get("doi"),
            "pmid": obj.get("pmid"),
            "studies": obj.get("studies"),
            "id": obj.get("id"),
            "public": obj.get("public") if obj.get("public") is not None else True,
            "level": obj.get("level")
        })
        return _obj


