from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_collection_return import NoteCollectionReturn


T = TypeVar("T", bound="AnnotationRelationships")


@attr.s(auto_attribs=True)
class AnnotationRelationships:
    """
    Attributes:
        notes (Union[Unset, List[Union['NoteCollectionReturn', str]]]):
    """

    notes: Union[Unset, List[Union["NoteCollectionReturn", str]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.note_collection_return import NoteCollectionReturn

        notes: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item: Union[Dict[str, Any], str]

                if isinstance(notes_item_data, NoteCollectionReturn):
                    notes_item = notes_item_data.to_dict()

                else:
                    notes_item = notes_item_data

                notes.append(notes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note_collection_return import NoteCollectionReturn

        d = src_dict.copy()
        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:

            def _parse_notes_item(data: object) -> Union["NoteCollectionReturn", str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    notes_item_type_0 = NoteCollectionReturn.from_dict(data)

                    return notes_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["NoteCollectionReturn", str], data)

            notes_item = _parse_notes_item(notes_item_data)

            notes.append(notes_item)

        annotation_relationships = cls(
            notes=notes,
        )

        annotation_relationships.additional_properties = d
        return annotation_relationships

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
