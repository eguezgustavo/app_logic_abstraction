import typing

from ..daos import TaskDao
from ..domain_objects import Task
from ..domain_objects import TaskState


class TaskService:
    def __init__(self, dao: TaskDao) -> None:
        self.dao = dao
    
    def get_pending_tasks(self) -> typing.List[Task]:
        return self.dao.find_by(state=TaskState.PENDING)

    def get_all(self) -> typing.List[Task]:
        return self.dao.get_all()
