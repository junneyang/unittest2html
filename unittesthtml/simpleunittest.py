#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import unittest
#import xmlrunner
import HTMLTestRunner

class baseTestCase(unittest.TestCase):
    def handle_exception(self,e):
        print(u"出现异常:"+str(e))
        raise Exception(str(e))

class simpleunittest(baseTestCase):
    def setUp(self):
        print(u"初始化")

    def test_case001(self):
        try:
            assert(111==111)
        except Exception as e:
            self.handle_exception(e)

    def test_case002(self):
        try:
            assert(111==112)
        except Exception as e:
            self.handle_exception(e)
    def test_case003(self):
        try:
            assert(111==111)
        except Exception as e:
            self.handle_exception(e)

    def tearDown(self):
        print(u"结束")

class simpleunittest001(baseTestCase):
    def setUp(self):
        print(u"初始化")

    def test_case001(self):
        try:
            assert(111==111)
        except Exception as e:
            self.handle_exception(e)
    def test_case002(self):
        try:
            assert(111==112)
        except Exception as e:
            self.handle_exception(e)
    def test_case003(self):
        try:
            assert(111==111)
        except Exception as e:
            self.handle_exception(e)

    def tearDown(self):
        print(u"结束")

#if __name__ == "__main__":
    #unittest.main()
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/home/users/yangjun03/.jenkins/workspace/jenkinsAPI/'))

#suite = unittest.TestLoader().loadTestsFromTestCase(simpleunittest)
suite = unittest.TestSuite()
suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(simpleunittest),
            unittest.defaultTestLoader.loadTestsFromTestCase(simpleunittest001),
            ])
unittest.TextTestRunner(verbosity=2).run(suite)

#unittest.main()
#unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/home/users/yangjun03/.jenkins/workspace/jenkinsAPI/'))

suite = unittest.TestSuite()
suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(simpleunittest),
            unittest.defaultTestLoader.loadTestsFromTestCase(simpleunittest001),
            ])
outfile = open("/home/users/yangjun03/.jenkins/workspace/jenkinsAPI/html/index.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='This demonstrates the report output by Prasanna.Yelsangikar.'
                )

runner.run(suite)

