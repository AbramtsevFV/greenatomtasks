from typing import Callable


def create_handlers(callback: Callable) -> list:
    handlers = []
    for step in range(5):
        handlers.append(lambda: callback(step))
    print(handlers)

    return handlers


def plus(d):
    return d + 1


def execute_handlers(handlers: list):
    for row in handlers:
        print(row())


if __name__ == '__main__':
    handlers = create_handlers(plus)
    execute_handlers(handlers)
