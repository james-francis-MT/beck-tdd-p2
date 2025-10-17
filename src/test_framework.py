from typing import Callable, cast, override

class TestCase:
    def __init__(self, name: str):
        self.name: str = name
        
    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = cast(Callable[[], None], getattr(self, self.name))
        method()


class WasRun(TestCase):
    def __init__(self, name: str):
        self.wasSetUp: int | None = None
        self.wasRun: int | None = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1

    @override
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

