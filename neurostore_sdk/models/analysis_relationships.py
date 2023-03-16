from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_return import ConditionReturn
    from ..models.image_return import ImageReturn
    from ..models.point_return import PointReturn


T = TypeVar("T", bound="AnalysisRelationships")


@attr.s(auto_attribs=True)
class AnalysisRelationships:
    """
    Attributes:
        study (Union[Unset, str]):
        images (Union[Unset, List[Union['ImageReturn', str]]]):
        points (Union[Unset, List[Union['PointReturn', str]]]):
        conditions (Union[Unset, List[Union['ConditionReturn', str]]]):
    """

    study: Union[Unset, str] = UNSET
    images: Union[Unset, List[Union["ImageReturn", str]]] = UNSET
    points: Union[Unset, List[Union["PointReturn", str]]] = UNSET
    conditions: Union[Unset, List[Union["ConditionReturn", str]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.condition_return import ConditionReturn
        from ..models.image_return import ImageReturn
        from ..models.point_return import PointReturn

        study = self.study
        images: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item: Union[Dict[str, Any], str]

                if isinstance(images_item_data, ImageReturn):
                    images_item = images_item_data.to_dict()

                else:
                    images_item = images_item_data

                images.append(images_item)

        points: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item: Union[Dict[str, Any], str]

                if isinstance(points_item_data, PointReturn):
                    points_item = points_item_data.to_dict()

                else:
                    points_item = points_item_data

                points.append(points_item)

        conditions: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item: Union[Dict[str, Any], str]

                if isinstance(conditions_item_data, ConditionReturn):
                    conditions_item = conditions_item_data.to_dict()

                else:
                    conditions_item = conditions_item_data

                conditions.append(conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if study is not UNSET:
            field_dict["study"] = study
        if images is not UNSET:
            field_dict["images"] = images
        if points is not UNSET:
            field_dict["points"] = points
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_return import ConditionReturn
        from ..models.image_return import ImageReturn
        from ..models.point_return import PointReturn

        d = src_dict.copy()
        study = d.pop("study", UNSET)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:

            def _parse_images_item(data: object) -> Union["ImageReturn", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    images_item_type_0 = ImageReturn.from_dict(data)

                    return images_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["ImageReturn", str], data)

            images_item = _parse_images_item(images_item_data)

            images.append(images_item)

        points = []
        _points = d.pop("points", UNSET)
        for points_item_data in _points or []:

            def _parse_points_item(data: object) -> Union["PointReturn", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    points_item_type_0 = PointReturn.from_dict(data)

                    return points_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["PointReturn", str], data)

            points_item = _parse_points_item(points_item_data)

            points.append(points_item)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:

            def _parse_conditions_item(data: object) -> Union["ConditionReturn", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_type_0 = ConditionReturn.from_dict(data)

                    return conditions_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["ConditionReturn", str], data)

            conditions_item = _parse_conditions_item(conditions_item_data)

            conditions.append(conditions_item)

        analysis_relationships = cls(
            study=study,
            images=images,
            points=points,
            conditions=conditions,
        )

        analysis_relationships.additional_properties = d
        return analysis_relationships

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
