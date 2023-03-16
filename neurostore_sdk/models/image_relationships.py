from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity


T = TypeVar("T", bound="ImageRelationships")


@attr.s(auto_attribs=True)
class ImageRelationships:
    """
    Attributes:
        analysis (Union[Unset, str]):
        entities (Union[Unset, List['Entity']]):
        analysis_name (Union[Unset, None, str]):
    """

    analysis: Union[Unset, str] = UNSET
    entities: Union[Unset, List["Entity"]] = UNSET
    analysis_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        analysis = self.analysis
        entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()

                entities.append(entities_item)

        analysis_name = self.analysis_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if analysis is not UNSET:
            field_dict["analysis"] = analysis
        if entities is not UNSET:
            field_dict["entities"] = entities
        if analysis_name is not UNSET:
            field_dict["analysis_name"] = analysis_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity import Entity

        d = src_dict.copy()
        analysis = d.pop("analysis", UNSET)

        entities = []
        _entities = d.pop("entities", UNSET)
        for entities_item_data in _entities or []:
            entities_item = Entity.from_dict(entities_item_data)

            entities.append(entities_item)

        analysis_name = d.pop("analysis_name", UNSET)

        image_relationships = cls(
            analysis=analysis,
            entities=entities,
            analysis_name=analysis_name,
        )

        image_relationships.additional_properties = d
        return image_relationships

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
