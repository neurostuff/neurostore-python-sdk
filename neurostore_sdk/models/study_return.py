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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, constr
from neurostore_sdk.models.study_return_all_of_studysets_inner import StudyReturnAllOfStudysetsInner
from neurostore_sdk.models.study_return_relationships_analyses import StudyReturnRelationshipsAnalyses

class StudyReturn(BaseModel):
    """
    StudyReturn
    """
    doi: Optional[StrictStr] = Field(None, description="Digital object identifier of the study.")
    name: Optional[StrictStr] = Field(None, description="Title of the study.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata associated with the study not covered by the other study attributes.")
    description: Optional[StrictStr] = Field(None, description="Long form description of the study, typically the abstract.")
    publication: Optional[StrictStr] = Field(None, description="The journal/place of publication for the study.")
    pmid: Optional[StrictStr] = Field(None, description="If the study was published on PubMed, place the PubMed ID here.")
    authors: Optional[StrictStr] = Field(None, description="The authors on the publication of this study.")
    year: Optional[conint(strict=True, le=9999, ge=0)] = Field(None, description="The year this study was published.")
    created_at: Optional[datetime] = Field(None, description="time the resource was created on the database")
    updated_at: Optional[StrictStr] = Field(None, description="when was the resource last modified/updated.")
    id: Optional[constr(strict=True, max_length=12, min_length=12)] = Field(None, description="short UUID specifying the location of this resource")
    public: Optional[StrictBool] = Field(True, description="whether the resource is listed in public searches or not")
    user: Optional[StrictStr] = Field(None, description="who owns the resource")
    username: Optional[StrictStr] = Field(None, description="human readable username")
    source: Optional[StrictStr] = None
    source_id: Optional[StrictStr] = None
    source_updated_at: Optional[StrictStr] = None
    analyses: Optional[StudyReturnRelationshipsAnalyses] = None
    studysets: Optional[conlist(StudyReturnAllOfStudysetsInner)] = None
    has_coordinates: Optional[StrictBool] = None
    has_images: Optional[StrictBool] = None
    __properties = ["doi", "name", "metadata", "description", "publication", "pmid", "authors", "year", "created_at", "updated_at", "id", "public", "user", "username", "source", "source_id", "source_updated_at", "analyses", "studysets", "has_coordinates", "has_images"]

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
    def from_json(cls, json_str: str) -> StudyReturn:
        """Create an instance of StudyReturn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                            "updated_at",
                            "user",
                            "source_updated_at",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of analyses
        if self.analyses:
            _dict['analyses'] = self.analyses.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in studysets (list)
        _items = []
        if self.studysets:
            for _item in self.studysets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['studysets'] = _items
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

        # set to None if source (nullable) is None
        # and __fields_set__ contains the field
        if self.source is None and "source" in self.__fields_set__:
            _dict['source'] = None

        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if source_updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.source_updated_at is None and "source_updated_at" in self.__fields_set__:
            _dict['source_updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StudyReturn:
        """Create an instance of StudyReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StudyReturn.parse_obj(obj)

        _obj = StudyReturn.parse_obj({
            "doi": obj.get("doi"),
            "name": obj.get("name"),
            "metadata": obj.get("metadata"),
            "description": obj.get("description"),
            "publication": obj.get("publication"),
            "pmid": obj.get("pmid"),
            "authors": obj.get("authors"),
            "year": obj.get("year"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "id": obj.get("id"),
            "public": obj.get("public") if obj.get("public") is not None else True,
            "user": obj.get("user"),
            "username": obj.get("username"),
            "source": obj.get("source"),
            "source_id": obj.get("source_id"),
            "source_updated_at": obj.get("source_updated_at"),
            "analyses": StudyReturnRelationshipsAnalyses.from_dict(obj.get("analyses")) if obj.get("analyses") is not None else None,
            "studysets": [StudyReturnAllOfStudysetsInner.from_dict(_item) for _item in obj.get("studysets")] if obj.get("studysets") is not None else None,
            "has_coordinates": obj.get("has_coordinates"),
            "has_images": obj.get("has_images")
        })
        return _obj

