class WasRun:
    def __init__(self, name: str):
        self.wasRun: int | None = None
    def run(self):
        self.testMethod()
    def testMethod(self):
        self.wasRun = 1
