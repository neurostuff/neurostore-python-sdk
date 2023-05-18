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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, constr
from neurostore_sdk.models.study_request_relationships_analyses import StudyRequestRelationshipsAnalyses

class StudyRequest(BaseModel):
    """
    StudyRequest
    """
    doi: Optional[StrictStr] = Field(None, description="Digital object identifier of the study.")
    name: Optional[StrictStr] = Field(None, description="Title of the study.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata associated with the study not covered by the other study attributes.")
    description: Optional[StrictStr] = Field(None, description="Long form description of the study, typically the abstract.")
    publication: Optional[StrictStr] = Field(None, description="The journal/place of publication for the study.")
    pmid: Optional[StrictStr] = Field(None, description="If the study was published on PubMed, place the PubMed ID here.")
    authors: Optional[StrictStr] = Field(None, description="The authors on the publication of this study.")
    year: Optional[conint(strict=True, le=9999, ge=0)] = Field(None, description="The year this study was published.")
    analyses: Optional[StudyRequestRelationshipsAnalyses] = None
    id: Optional[constr(strict=True, max_length=12, min_length=12)] = Field(None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(True, description="whether the resource is listed in public searches or not")
    __properties = ["doi", "name", "metadata", "description", "publication", "pmid", "authors", "year", "analyses", "id", "public"]

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
    def from_json(cls, json_str: str) -> StudyRequest:
        """Create an instance of StudyRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of analyses
        if self.analyses:
            _dict['analyses'] = self.analyses.to_dict()
        # set to None if doi (nullable) is None
        # and __fields_set__ contains the field
        if self.doi is None and "doi" in self.__fields_set__:
            _dict['doi'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if publication (nullable) is None
        # and __fields_set__ contains the field
        if self.publication is None and "publication" in self.__fields_set__:
            _dict['publication'] = None

        # set to None if pmid (nullable) is None
        # and __fields_set__ contains the field
        if self.pmid is None and "pmid" in self.__fields_set__:
            _dict['pmid'] = None

        # set to None if authors (nullable) is None
        # and __fields_set__ contains the field
        if self.authors is None and "authors" in self.__fields_set__:
            _dict['authors'] = None

        # set to None if year (nullable) is None
        # and __fields_set__ contains the field
        if self.year is None and "year" in self.__fields_set__:
            _dict['year'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudyRequest:
        """Create an instance of StudyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudyRequest.parse_obj(obj)

        _obj = StudyRequest.parse_obj({
            "doi": obj.get("doi"),
            "name": obj.get("name"),
            "metadata": obj.get("metadata"),
            "description": obj.get("description"),
            "publication": obj.get("publication"),
            "pmid": obj.get("pmid"),
            "authors": obj.get("authors"),
            "year": obj.get("year"),
            "analyses": StudyRequestRelationshipsAnalyses.from_dict(obj.get("analyses")) if obj.get("analyses") is not None else None,
            "id": obj.get("id"),
            "public": obj.get("public") if obj.get("public") is not None else True
        })
        return _obj
