from src.test_framework import WasRun

def test_test_framework():
    test = WasRun("testMehod")
    print(test.wasRun)
    test.testMethod()
    print(test.wasRun)
