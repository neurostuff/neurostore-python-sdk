from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.study_return import StudyReturn


T = TypeVar("T", bound="StudysetRelationships")


@attr.s(auto_attribs=True)
class StudysetRelationships:
    """
    Attributes:
        studies (Union[Unset, List[Union['StudyReturn', str]]]):
    """

    studies: Union[Unset, List[Union["StudyReturn", str]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.study_return import StudyReturn

        studies: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.studies, Unset):
            studies = []
            for studies_item_data in self.studies:
                studies_item: Union[Dict[str, Any], str]

                if isinstance(studies_item_data, StudyReturn):
                    studies_item = studies_item_data.to_dict()

                else:
                    studies_item = studies_item_data

                studies.append(studies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if studies is not UNSET:
            field_dict["studies"] = studies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.study_return import StudyReturn

        d = src_dict.copy()
        studies = []
        _studies = d.pop("studies", UNSET)
        for studies_item_data in _studies or []:

            def _parse_studies_item(data: object) -> Union["StudyReturn", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    studies_item_type_0 = StudyReturn.from_dict(data)

                    return studies_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["StudyReturn", str], data)

            studies_item = _parse_studies_item(studies_item_data)

            studies.append(studies_item)

        studyset_relationships = cls(
            studies=studies,
        )

        studyset_relationships.additional_properties = d
        return studyset_relationships

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
