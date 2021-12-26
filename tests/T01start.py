import unittest

from app import wud

class TestOne(unittest.TestCase):

    def test_01(self):
        self.assertEqual(wud(),'whats up doc?')