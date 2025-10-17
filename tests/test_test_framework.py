from src.test_framework import WasRun

def test_test_framework():
    test = WasRun("testMehod")
    assert(test.wasRun == None)
    test.testMethod()
    assert(test.wasRun == 1)
