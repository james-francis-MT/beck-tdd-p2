from typing import Callable, cast, override

class TestCase:
    def __init__(self, name: str):
        self.name: str = name
        
    def setUp(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = cast(Callable[[], None], getattr(self, self.name))
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

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

    def testBrokenMethod(self):
        raise Exception

    @override
    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    @override
    def tearDown(self):
        self.log = self.log + "tearDown "

class TestResult:
    def __init__(self):
        self.runCount: int = 0
        self.errorCount: int = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return "%d run, %d failed"%(self.runCount, self.errorCount)

