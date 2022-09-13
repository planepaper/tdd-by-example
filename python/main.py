class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self,name)
    
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = "tearDown "

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test= WasRun("testmethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

if __name__ == "__main__":
    TestCaseTest("testSetUp").run()
