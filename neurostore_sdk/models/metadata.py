from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Metadata")


@attr.s(auto_attribs=True)
class Metadata:
    """data included in every list response

    Attributes:
        total_count (Union[Unset, int]): total number of entries
        unique_count (Union[Unset, int]): count of elements for unique entries
    """

    total_count: Union[Unset, int] = UNSET
    unique_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        unique_count = self.unique_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if unique_count is not UNSET:
            field_dict["unique_count"] = unique_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count", UNSET)

        unique_count = d.pop("unique_count", UNSET)

        metadata = cls(
            total_count=total_count,
            unique_count=unique_count,
        )

        return metadata
