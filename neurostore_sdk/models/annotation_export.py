from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_export_metadata import AnnotationExportMetadata


T = TypeVar("T", bound="AnnotationExport")


@attr.s(auto_attribs=True)
class AnnotationExport:
    """exporting an annotation as a CSV for easier editing

    Attributes:
        annotation_csv (str): annotation object expressed as a CSV
        metadata (Union[Unset, None, AnnotationExportMetadata]):
    """

    annotation_csv: str
    metadata: Union[Unset, None, "AnnotationExportMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        annotation_csv = self.annotation_csv
        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "annotation_csv": annotation_csv,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotation_export_metadata import AnnotationExportMetadata

        d = src_dict.copy()
        annotation_csv = d.pop("annotation_csv")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, AnnotationExportMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AnnotationExportMetadata.from_dict(_metadata)

        annotation_export = cls(
            annotation_csv=annotation_csv,
            metadata=metadata,
        )

        return annotation_export
