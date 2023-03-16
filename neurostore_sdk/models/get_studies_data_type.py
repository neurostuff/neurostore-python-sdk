from enum import Enum


class GetStudiesDataType(str, Enum):
    COORDINATE = "coordinate"
    IMAGE = "image"
    BOTH = "both"

    def __str__(self) -> str:
        return str(self.value)
