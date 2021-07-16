import unittest from nextPermutations import nextPermutations 
class nextTest(unittest.TestCase):
    #test the output of the correct value
    def test_next(self):
        #list to test
        myList = [1,2,3]
        #function call to be tested
        result = nextPermutations(myList)
        #assert
        self.assertEqual(result, [1, 3, 2])  
    #test for the wrong output  
    def test_next_not_equal(self):
        #list to test
        myList = [1,2,3]
        #function call to be tested
        result = nextPermutations(myList)
        #assert
        self.assertNotEqual(result, [1, 2, 3])
        
if __name__ == '__main__':
    unittest.main()
