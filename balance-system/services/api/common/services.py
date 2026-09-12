import logging
from typing import Any


class BaseService:
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)

    def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError("Please Implement this method in the service class.")
