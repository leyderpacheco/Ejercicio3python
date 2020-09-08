import unittest
from main import palabra


class Test(unittest.TestCase):
    def test_palabra(self):
        palabrap=str(palabra())
        self.assertEqual( str("ha"), palabrap)
