class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return TestResult()

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def testFailed(self):
        self.failureCount = self.failureCount + 1
    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failureCount)

class TestSuite:
    def __init__(self):
        self.tests=[]
    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)
        return result

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self,name)
    
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = "tearDown "

    def testBrokenMethod(self):
        raise Exception

class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test= WasRun("testmethod")
        result = self.test.run(result)
        assert("1 run, 0 failed" == result.summary())

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testFailedResultFormatting(self):
        test = WasRun("testBrokenMethod")
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())

if __name__ == "__main__":
    suite= TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testRunning"))
    suite.add(TestCaseTest("testFailedResultFormatting"))
    suite.add(TestCaseTest("testSuite"))
    result = TestResult()
    suite.run(result)
    print (result.summary())
