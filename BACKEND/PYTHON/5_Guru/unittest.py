'''
Unit Testing in Python is done to identify bugs early in the development stage of the application
when bugs are less recurrent and less expensive to fix.

A unit test is a scripted code level test designed in Python to verify a small "unit" of functionality.
Unit test is an object oriented framework based around test fixtures.

Python Unit Testing Techniques
Python Unit Testing mainly involves testing a particular module without accessing any dependent code.
Developers can use techniques like stubs and mocks to separate code into "units" and run unit level testing on the individual pieces.

Test-Driven Development TDD: Unit Testing should be done along with the Python, and for that developers use
Test-Driven Development method.
In TDD method, you first design Python Unit tests and only then you carry on writing the code that will implement this feature.
Stubs and Mocks: They are two main techniques that simulate fake methods that are being tested.
A Stub is used to fill in some dependency required for unit test to run correctly.
A Mock on the other hand is a fake object which runs the tests where we put assert.

The intentions of both methods are same to eliminate testing all the dependencies of a class or function.

Python Unit Testing Framework
To make the Unit Testing process easier and improve the quality of your project,
it is recommended the Python Unit Testing Framework. The Unit Testing framework includes



PyUnit: PyUnit supports fixtures, test cases, test suites and a test runner for the automated testing of the code.
In PyUnit, you can organize test cases into suites with the same fixtures.

Pyunit is a Python port of JUnit. As a part of Pyunit, in the unittest module there are five key classes.

TestCase class:     The TestCase class bears the test routines and delivers hooks for making each routine and cleaning up thereafter
TestSuite class:    It caters as a collection container, and it can possess multiple testcase objects and multiple testsuites objects
TestLoader class:   This class loads test cases and suites defined locally or from an external file.
                    It emits a testsuite objects that posseses those suites and cases
TextTestRunner class: To run the tests it caters a standard platform to execute the tests
The TestResults class: It offers a standard container for the test results.


Designing a test case for Python Testing using PyUnit.
A unit test provides a base class, test case, which may be used to create new test cases.
For designing the test case, there are three sets of methods used are

unittest.TestCase
setUp()
teardown()

skipTest(aMesg:string)
fail(aMesg:string)

id():string
shortDescription():string

In the first set are the pre and post test hooks.
The setup() method begins before each test routine, the teardown() after the routine.

The second set of method controls test execution.Both methods take a message string as input, and both cancel an ongoing test.
But the skiptest() method aborts the current test while the fail() method fails it completely.

The last or third method help determining the test.
The method id() returns a string consisting of the name of the testcase object and of the test routine.
And the method shortDescription() returns the docstr comment at the initiation of each test routine.



Advantages of using Python Unit testing:
It helps you to detect bugs early in the development cycle
It helps you to write better programs.
It syncs easily with other testing methods and tools.
It will have many fewer bugs
It is easier to modify in future with very less consequence
'''

