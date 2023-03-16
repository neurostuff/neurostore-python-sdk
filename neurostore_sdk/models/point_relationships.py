from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity
    from ..models.point_value import PointValue


T = TypeVar("T", bound="PointRelationships")


@attr.s(auto_attribs=True)
class PointRelationships:
    """
    Attributes:
        image (Union[Unset, None, str]):
        value (Union['PointValue', Unset, str]):
        x (Union[Unset, float]):
        y (Union[Unset, float]):
        z (Union[Unset, float]):
        entities (Union[Unset, List['Entity']]):
    """

    image: Union[Unset, None, str] = UNSET
    value: Union["PointValue", Unset, str] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    z: Union[Unset, float] = UNSET
    entities: Union[Unset, List["Entity"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.point_value import PointValue

        image = self.image
        value: Union[Dict[str, Any], Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET

        elif isinstance(self.value, PointValue):
            value = UNSET
            if not isinstance(self.value, Unset):
                value = self.value.to_dict()

        else:
            value = self.value

        x = self.x
        y = self.y
        z = self.z
        entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()

                entities.append(entities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if value is not UNSET:
            field_dict["value"] = value
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if entities is not UNSET:
            field_dict["entities"] = entities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity import Entity
        from ..models.point_value import PointValue

        d = src_dict.copy()
        image = d.pop("image", UNSET)

        def _parse_value(data: object) -> Union["PointValue", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _value_type_0 = data
                value_type_0: Union[Unset, PointValue]
                if isinstance(_value_type_0, Unset):
                    value_type_0 = UNSET
                else:
                    value_type_0 = PointValue.from_dict(_value_type_0)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PointValue", Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        entities = []
        _entities = d.pop("entities", UNSET)
        for entities_item_data in _entities or []:
            entities_item = Entity.from_dict(entities_item_data)

            entities.append(entities_item)

        point_relationships = cls(
            image=image,
            value=value,
            x=x,
            y=y,
            z=z,
            entities=entities,
        )

        point_relationships.additional_properties = d
        return point_relationships

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
