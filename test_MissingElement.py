import unittest
from MissingElement import finder 

class TestFinder(unittest.TestCase):

    def test_finder(self):
        """
        This will test for missing element between two arrays.
        """
        self.assertEqual(finder([3,7,9,2], [2,7,9]), 3)
        self.assertEqual(finder([3,7,9,2], [3,7,9]), 2)
        self.assertNotEqual(finder([3,7,9,2], [2,7,3]), 3)

if __name__ == '__main__':
    unittest.main()
