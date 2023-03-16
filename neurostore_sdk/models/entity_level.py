from enum import Enum


class EntityLevel(str, Enum):
    RUN = "run"
    SESSION = "session"
    SUBJECT = "subject"
    GROUP = "group"
    META = "meta"

    def __str__(self) -> str:
        return str(self.value)
