import dataclasses


@dataclasses.dataclass(frozen=True)
class TaskState:
    CLOSED=1
    PENDING=2
