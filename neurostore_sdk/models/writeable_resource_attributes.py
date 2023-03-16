from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WriteableResourceAttributes")


@attr.s(auto_attribs=True)
class WriteableResourceAttributes:
    """common resource attributes

    Attributes:
        id (Union[Unset, str]): short UUID specifying the location of this resource Example: 38jobTomPDqt.
        public (Union[Unset, bool]): whether the resource is listed in public searches or not Default: True.
    """

    id: Union[Unset, str] = UNSET
    public: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        public = self.public

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        public = d.pop("public", UNSET)

        writeable_resource_attributes = cls(
            id=id,
            public=public,
        )

        writeable_resource_attributes.additional_properties = d
        return writeable_resource_attributes

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
