from typing import override
from .test_framework import TestCase, WasRun

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
