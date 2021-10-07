import typing

from ._business_logic import TaskService
from ._business_logic import Task
from ._implementations import FakeTaskDao


def execute() -> typing.List[Task]:
    task_dao = FakeTaskDao()
    service = TaskService(task_dao)

    return service.get_all()
