import unittest

from cstats.app import wud

class TestOne(unittest.TestCase):

    def test_01(self):
        self.assertEqual(wud(),'whats up doc?')