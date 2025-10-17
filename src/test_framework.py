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
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1

    @override
    def setUp(self):
        self.wasSetUp = 1

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)

print('running tests')
TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
print('tests okay')
