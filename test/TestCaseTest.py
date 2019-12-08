from src.TestCase import TestCase
from src.TestResult import TestResult
from src.TestSuite import TestSuite
from src.WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert ("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert "1 run, 1 failed" == self.result.summary()

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert "1 run, 1 failed" == self.result.summary()

    def testSuite(self):
        suite1 = TestSuite()
        suite1.add(WasRun("testMethod"))
        suite1.add(WasRun("testBrokenMethod"))
        suite1.run(self.result)
        assert "2 run, 1 failed" == self.result.summary()


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())
