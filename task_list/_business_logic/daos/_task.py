import abc
import typing

from ..domain_objects import Task
from ..domain_objects import TaskState


class TaskDao(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def find_by(self, state: TaskState=None) -> typing.List[Task]:
        pass

    @abc.abstractproperty
    def get_all(self) -> typing.List[Task]:
        pass
