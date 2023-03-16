from enum import Enum


class PostStudiesSource(str, Enum):
    NEUROSTORE = "neurostore"
    NEUROVAULT = "neurovault"
    PUBMED = "pubmed"
    NEUROSYNTH = "neurosynth"
    NEUROQUERY = "neuroquery"

    def __str__(self) -> str:
        return str(self.value)