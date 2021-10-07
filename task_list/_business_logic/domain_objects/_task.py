import dataclasses

from ._task_state import TaskState


@dataclasses.dataclass(frozen=True)
class Task:
    id: int
    description: str
    state: TaskState
