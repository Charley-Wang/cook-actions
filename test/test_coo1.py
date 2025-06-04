import unittest
from app.coo1 import add

class TestCoo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))