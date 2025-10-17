from typing import Callable, cast


class WasRun:
    def __init__(self, name: str):
        self.wasRun: int | None = None
        self.name: str = name
    def run(self):
        method = cast(Callable[[], None], getattr(self, self.name))
        method()
    def testMethod(self):
        self.wasRun = 1
