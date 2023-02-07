from typing import Callable, Generator, Iterable

"""Исправление кода"""
def create_handlers(callback: Callable) -> Generator[Callable, None, None]:
    for step in range(5):
        yield lambda: callback(step)


def plus(d):
    return d + 1


def execute_handlers(handlers: Iterable[Callable]):
    for handler in handlers:
        print(handler())


if __name__ == '__main__':
    handlers_list = create_handlers(plus)

    execute_handlers(handlers_list)
