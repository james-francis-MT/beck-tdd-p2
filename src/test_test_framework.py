from typing import override
from .test_framework import TestCase, WasRun

class TestCaseTest(TestCase):
    def __init__(self, name: str):
        self.test: WasRun
        super().__init__(name)

    @override
    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

print('running tests')
TestCaseTest("testTemplateMethod").run()
print('tests okay')
