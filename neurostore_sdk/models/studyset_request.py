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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator
from neurostore_sdk.models.studyset_request_relationships_studies import StudysetRequestRelationshipsStudies

class StudysetRequest(BaseModel):
    """
    StudysetRequest
    """
    name: Optional[StrictStr] = Field(None, description="Descriptive and human readable name of the studyset.")
    description: Optional[StrictStr] = Field(None, description="A longform description of the studyset.")
    publication: Optional[StrictStr] = Field(None, description="The journal/source the studyset is connected to if the studyset was published.")
    doi: Optional[StrictStr] = Field(None, description="A DOI connected to the published studyset (may change to being automatically created so each studyset connected to a successful meta-analysis gets a DOI).")
    pmid: Optional[StrictStr] = Field(None, description="If the article connected to the studyset was published on PubMed, then link the ID here.")
    studies: Optional[StudysetRequestRelationshipsStudies] = None
    id: Optional[constr(strict=True, max_length=12, min_length=12)] = Field(None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(True, description="whether the resource is listed in public searches or not")
    level: Optional[StrictStr] = None
    __properties = ["name", "description", "publication", "doi", "pmid", "studies", "id", "public", "level"]

    @validator('level')
    def level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('group', 'meta'):
            raise ValueError("must be one of enum values ('group', 'meta')")
        return value

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
    def from_json(cls, json_str: str) -> StudysetRequest:
        """Create an instance of StudysetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of studies
        if self.studies:
            _dict['studies'] = self.studies.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if publication (nullable) is None
        # and __fields_set__ contains the field
        if self.publication is None and "publication" in self.__fields_set__:
            _dict['publication'] = None

        # set to None if doi (nullable) is None
        # and __fields_set__ contains the field
        if self.doi is None and "doi" in self.__fields_set__:
            _dict['doi'] = None

        # set to None if pmid (nullable) is None
        # and __fields_set__ contains the field
        if self.pmid is None and "pmid" in self.__fields_set__:
            _dict['pmid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudysetRequest:
        """Create an instance of StudysetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudysetRequest.parse_obj(obj)

        _obj = StudysetRequest.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "publication": obj.get("publication"),
            "doi": obj.get("doi"),
            "pmid": obj.get("pmid"),
            "studies": StudysetRequestRelationshipsStudies.from_dict(obj.get("studies")) if obj.get("studies") is not None else None,
            "id": obj.get("id"),
            "public": obj.get("public") if obj.get("public") is not None else True,
            "level": obj.get("level")
        })
        return _obj

