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
        self.tearDown()

    def tearDown(self):
        pass

class WasRun(TestCase):
    def __init__(self, name: str):
        self.wasRun: int | None = None
        self.log: str = ""
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    @override
    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    @override
    def tearDown(self):
        self.log = self.log + "tearDown "

