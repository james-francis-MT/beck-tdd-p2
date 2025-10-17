from src.test_framework import WasRun

def test_test_framework():
    test = WasRun("testMethod")
    print(type(test.run))
    assert(test.wasRun == None)
    test.run()
    assert(test.wasRun == 1)
