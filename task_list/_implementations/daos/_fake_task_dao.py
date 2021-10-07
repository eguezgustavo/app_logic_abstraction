import typing

from ..._business_logic import TaskDao
from ..._business_logic import Task
from ..._business_logic import TaskState


class FakeTaskDao(TaskDao):
    def find_by(self, state: TaskState=None) -> typing.List[Task]:
        return [Task(id=2, description='Another Task', state=TaskState.PENDING)]

    def get_all(self) -> typing.List[Task]:
        return [
            Task(id=2, description='Another Task', state=TaskState.PENDING),
            Task(id=2, description='Some Task', state=TaskState.CLOSED),
        ]
