from src.TestResult import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()
        return result

    def setUp(self):
        pass

    def tearDown(self):
        pass
