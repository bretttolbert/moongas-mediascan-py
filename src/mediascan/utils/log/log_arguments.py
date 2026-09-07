import functools
import inspect
from collections.abc import Callable
from typing import ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")


def log_arguments(func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        # Bind positional and keyword args to parameter names
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        print(f"\n--- [LOG] Executing {func.__name__} ---")
        for param, val in bound.arguments.items():
            print(f"  {param:<18}: {val}")
        print("---------------------------------------\n")
        
        return func(*args, **kwargs)
    return wrapper
