from abc import ABCMeta, abstractmethod
from typing import Any, Callable


class BaseService(metaclass=ABCMeta):

    def __call__(self, *args, **kwargs) -> Any:
        self.validate()
        return self.act()

    def get_validators(self) -> list[Callable]:  # noqa
        return []

    def validate(self) -> None:
        validators = self.get_validators()
        for validator in validators:
            validator()

    @abstractmethod
    def act(self) -> Any:
        raise NotImplementedError("Please Implement this method in the service class.")
