
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
