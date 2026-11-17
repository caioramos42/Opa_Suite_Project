
from functools import wraps
from typing import Callable, ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")


def not_implemented_error(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        raise NotImplementedError(
            f"O método {func.__name__} ainda não foi implementado."
        )

    return wrapper