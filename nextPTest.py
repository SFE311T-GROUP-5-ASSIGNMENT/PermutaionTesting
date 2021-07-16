import itertools
import unittest
import types


class nextPTest(unittest.TestCase):

    # Various test cases
    mylist =  [1, 2, 3]


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


if __name__ == '__main__':
    unittest.main()
