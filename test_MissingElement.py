import unittest
from MissingElement import finder, finder_dict 

class TestFinder(unittest.TestCase):

    def test_finder(self):
        """
        This will test the array based approach. 
        """
        self.assertEqual(finder([3,7,9,2], [2,7,9]), 3)
        self.assertEqual(finder([3,7,9,2], [3,7,9]), 2)
        self.assertNotEqual(finder([3,7,9,2], [2,7,3]), 3)
    def test_finder_dict(self):
        """
        This will test the dictionary based approach. 
        """
        self.assertEqual(finder_dict([3,7,9,2],[2,7,9]), 3)
        self.assertEqual(finder_dict([3,7,9,2],[3,7,9]), 2)
        self.assertNotEqual(finder_dict([3,7,9,2],[2,7,3]), 3)


if __name__ == '__main__':
    unittest.main()
