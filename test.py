import unittest

from binary_search import BinarySearch

class BinarySearchTest(unittest.TestCase):

    def setUp(self):
        self.BinS = BinarySearch([11, 19, 27, 33, 42, 57, 63, 76, 81, 93, 99])                  #pass the list while creating the object

    def tearDown(self):
        pass

    def test_binary_search_found(self):                                         
        self.assertEqual(self.BinS.binary_search(27), 2)                        #random element
        self.assertEqual(self.BinS.binary_search(11), 0)                        #first element
        self.assertEqual(self.BinS.binary_search(99),10)                        #last element

    def test_binary_search_notFound(self):
        self.assertEqual(self.BinS.binary_search(53), -1)                       #test for element which is not in the set

if __name__ == '__main__':
    unittest.main()