from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_ld_context import JsonLdContext


T = TypeVar("T", bound="JsonLd")


@attr.s(auto_attribs=True)
class JsonLd:
    """JSON-LD elements for data tracking

    Attributes:
        context (Union[Unset, JsonLdContext]): Context for the shorthand names
        id (Union[Unset, str]): URI of the resource
        type (Union[Unset, str]): One of the NiMADS data types Example: Study.
    """

    context: Union[Unset, "JsonLdContext"] = UNSET
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["@context"] = context
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.json_ld_context import JsonLdContext

        d = src_dict.copy()
        _context = d.pop("@context", UNSET)
        context: Union[Unset, JsonLdContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = JsonLdContext.from_dict(_context)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        json_ld = cls(
            context=context,
            id=id,
            type=type,
        )

        json_ld.additional_properties = d
        return json_ld

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
