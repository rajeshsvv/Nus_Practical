'''

Unit Testing in Python – Unittest
What is Unit Testing?
Unit Testing is the first level of software testing where the smallest testable parts of a software are tested.
This is used to validate that each unit of the software performs as designed.
The unittest test framework is python’s xUnit style framework.

Method:
White Box Testing method is used for Unit testing.

test    fixture:
A test fixture is used as a baseline for running tests to ensure that there is a fixed environment
in which tests are run so that results are repeatable.
Examples:creating temporary databases.
         starting a server process.

test case:
A test case is a set of conditions which is used to determine whether a system under test works correctly.

test suite:
Test suite is a collection of testcases that are used to test a software program to show that
it has some specified set of behaviours by executing the aggregated tests together.

test runner:
A test runner is a component which set up the execution of tests and provides the outcome to the user.

'''


'''

import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()
    
'''

import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    # Returns True if the string contains 4 a.
    # def test_string(self):
    #     self.assertEqual('a'*4,'aaa')

    # Returns True if the string is in upper case.
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(),'FOO')


    # Returns TRUE if the string is in uppercase else returns False.
    # def test_isupper(self):
    #     self.assertTrue("FOO".isupper())
    #     self.assertTrue("foo".islower())

    # Returns true if the string is stripped and matches the given output.
    # def test_strip(self):
    #     s='geeksforgeeks'
    #     self.assertEqual(s.trip('geeksforgeeks'),'geeksforgeeks')

    # Returns true if the string splits and matches the given output.
    def test_split(self):
        s="hello world"
        self.assertEqual(s.split(","),['hello world'])
        with self.assertRaises(TypeError):
            s.split(4)

if __name__=="__main__":
    unittest.main()

