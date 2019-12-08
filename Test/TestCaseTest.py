from Python.TestCase import TestCase
from Python.WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        self.test.run()
        assert ("setUp testMethod tearDown " == self.test.log)


TestCaseTest("testTemplateMethod").run()
