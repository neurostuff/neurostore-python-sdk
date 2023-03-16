from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis_return import AnalysisReturn


T = TypeVar("T", bound="StudyRelationships")


@attr.s(auto_attribs=True)
class StudyRelationships:
    """
    Attributes:
        analyses (Union[Unset, List[Union['AnalysisReturn', str]]]):
    """

    analyses: Union[Unset, List[Union["AnalysisReturn", str]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.analysis_return import AnalysisReturn

        analyses: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.analyses, Unset):
            analyses = []
            for analyses_item_data in self.analyses:
                analyses_item: Union[Dict[str, Any], str]

                if isinstance(analyses_item_data, AnalysisReturn):
                    analyses_item = analyses_item_data.to_dict()

                else:
                    analyses_item = analyses_item_data

                analyses.append(analyses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if analyses is not UNSET:
            field_dict["analyses"] = analyses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.analysis_return import AnalysisReturn

        d = src_dict.copy()
        analyses = []
        _analyses = d.pop("analyses", UNSET)
        for analyses_item_data in _analyses or []:

            def _parse_analyses_item(data: object) -> Union["AnalysisReturn", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    analyses_item_type_0 = AnalysisReturn.from_dict(data)

                    return analyses_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["AnalysisReturn", str], data)

            analyses_item = _parse_analyses_item(analyses_item_data)

            analyses.append(analyses_item)

        study_relationships = cls(
            analyses=analyses,
        )

        study_relationships.additional_properties = d
        return study_relationships

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
