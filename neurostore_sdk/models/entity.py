import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.entity_level import EntityLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="Entity")


@attr.s(auto_attribs=True)
class Entity:
    """descriptor of level of analysis for a particular image/point (run, session, subject, group, meta)

    Attributes:
        created_at (Union[Unset, datetime.datetime]): time the resource was created on the database Example:
            2021-01-16T20:50:38.009318+00:00.
        updated_at (Union[Unset, None, str]): when was the resource last modified/updated.
        id (Union[Unset, str]): short UUID specifying the location of this resource Example: 38jobTomPDqt.
        public (Union[Unset, bool]): whether the resource is listed in public searches or not Default: True.
        label (Union[Unset, str]):
        level (Union[Unset, EntityLevel]):
        analysis (Union[Unset, str]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    public: Union[Unset, bool] = True
    label: Union[Unset, str] = UNSET
    level: Union[Unset, EntityLevel] = UNSET
    analysis: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at = self.updated_at
        id = self.id
        public = self.public
        label = self.label
        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        analysis = self.analysis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if id is not UNSET:
            field_dict["id"] = id
        if public is not UNSET:
            field_dict["public"] = public
        if label is not UNSET:
            field_dict["label"] = label
        if level is not UNSET:
            field_dict["level"] = level
        if analysis is not UNSET:
            field_dict["analysis"] = analysis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        updated_at = d.pop("updated_at", UNSET)

        id = d.pop("id", UNSET)

        public = d.pop("public", UNSET)

        label = d.pop("label", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, EntityLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = EntityLevel(_level)

        analysis = d.pop("analysis", UNSET)

        entity = cls(
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            public=public,
            label=label,
            level=level,
            analysis=analysis,
        )

        entity.additional_properties = d
        return entity

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
