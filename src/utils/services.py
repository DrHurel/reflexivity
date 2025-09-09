from collections.abc import Callable
from threading import Lock
from typing import Any, TypeVar, cast, get_type_hints

from meta.pattern import Singleton


T = TypeVar("T")
K = TypeVar("K")


class ServiceRegistry(metaclass=Singleton):

    def __init__(self) -> None:
        self.__lock = Lock()
        self._services: dict[int, object] = {}
    def register(self,interface: type[K], service: object) -> None:

        with self.__lock:
            assert isinstance(cast(Any,service), interface), f"{service.__class__.__name__} must implement {interface.__name__}"

            self._services[interface.__qualname__.__hash__()] = service

    def get(self, interace: type[T]) -> T:

        with self.__lock:
            return cast(T,self._services.get(interace.__qualname__.__hash__()))

__registry = ServiceRegistry()

def service(ServiceInterface: type[K]):
    def wrapper(cls: type[T]) -> type[T]:
        assert issubclass(cast(Any,cls), ServiceInterface), f"{cls.__name__} must implement {ServiceInterface.__name__}"

        __registry.register(ServiceInterface,cls())
        return cls

    return wrapper

def inject(property : Callable[[Any],T]) -> T:


    types = get_type_hints(property)
    property = __registry.get(types["return"])
    return cast(T,property)

