class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self,name)
    
    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasRun = None
        self.wasSetUp= 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        
    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

if __name__ == "__main__":
    TestCaseTest("testSetUp").run()
