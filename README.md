# TDD Task
- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- create a class and method to write code to pass the test
- create a test case to calculate % and code to pass the test
- create a test to check if the given values are positive
- create a method in the class to pass the test

### Steps
- create `task_test.py`
- first `pip install pytest` and `import pytest, unittest`
- import `Remainder` class from `task_code.py` (not yet written)
- define test class for all tests, first call Remainder as object within class
- define Remainder test and run to ensure syntax is correct, a return of a failed task is expected here
- write Remainder code in `task_code.py` and run to ensure syntax
- run tests in `task_test.py`, expect a pass here
- if test is passed move onto next task, if it fails trouble shoot until it passes

### Test Code
```python
import unittest
import pytest

from task_code import Tasks

class MultiTest(unittest.TestCase):

    test = Tasks()

    def test_zero(self):
        self.assertEqual(self.test.Zero(4, 2), 0)

    def test_percent(self):
        self.assertEqual(self.test.Percent(4, 2), 50)

    def test_positive(self):
        self.assertEqual(self.test.Positive(3), True)
```
### Code to Pass Tests
```python
class Tasks:

    def Zero(self, num1, num2):
        return num1 % num2

    def Percent(self, num1, num2):
        return (num2 / num1) * 100

    def Positive(self, num):
        return num > 0
```