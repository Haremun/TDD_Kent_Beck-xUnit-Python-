from Python.TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.log = None

    def testMethod(self):
        self.log = self.log + "testMethod "

    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "
