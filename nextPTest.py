import itertools
import unittest
import types


class nextPTest(unittest.TestCase):

    # Various test cases
    mylist =  [5, 6, 7]
    single_element = [4]
    list_of_lists = [ [1.1, 1.2], [2.1, 2.2], [3.1, 3.2] ]
    multilist = [ 'a', 2, 3.3 ]


    def generic_test(self, elements):
        """Compares itertools.permutations(elements) vs permutations(elements)."""

        # Arrange
        expected = list(itertools.permutations(elements))

        # Act
        actual = list(itertools.permutations(elements))

        # Assert
        self.assertEqual(expected, actual)


    def test_is_generator(self):
        """Test that object is actually an generator."""
        # Act
        actual = itertools.permutations(self.numeric_list)

        # Assert
        self.assertTrue( isinstance(actual, types.GeneratorType))


    def test_numeric_list(self):
        """Test for a list of numbers"""
        self.generic_test(self.mylist)



    def test_single_element(self):
        """Test for a single element."""
        self.generic_test(self.single_element)


    def test_list_of_lists(self):
        """Test for a list of lists."""
        self.generic_test(self.list_of_lists)


    def test_multilist(self):
        """Test for list consisting of various elements."""
        self.generic_test(self.multilist)


if __name__ == '__main__':
    unittest.main()