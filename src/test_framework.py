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

class TestCaseTest(TestCase):
    def __init__(self, name: str):
        self.test: WasRun
        super().__init__(name)

    @override
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)

print('running tests')
TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
print('tests okay')
