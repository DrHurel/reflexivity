from threading import Lock
from typing import Any, Generic, Optional, TypeVar


class Singleton(type):

    _instances: dict[Any, Any] = {}
    _lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwargs: Any):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(
                    *args, **kwargs
                )
        return cls._instances[cls]

T = TypeVar("T")
class Result(Generic[T]):

    def __init__(self, value: Optional[T] =None, error: Optional[Exception]  = None) -> None:
        assert (value is not None) != (error is not None), "Either value or error must be provided, but not both."
        self.value = value
        self.error = error


    def succeeded(self) -> bool:
        return self.error is None

    def failed(self) -> bool:
        return self.error is not None

    @classmethod
    def success(cls, value: T) -> "Result[T]":
        return cls(value=value)

    @classmethod
    def failure(cls, error: Exception) -> "Result[T]":
        return cls(error=error)

    def __repr__(self) -> str:
        if self.succeeded():
            return f"Result(success: {self.value})"
        else:
            return f"Result(failure: {self.error})"


