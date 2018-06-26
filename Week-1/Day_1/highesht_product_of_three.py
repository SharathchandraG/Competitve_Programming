import unittest


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    actual_list = list_of_ints[:]

    max1 = max(list_of_ints)
    list_of_ints.remove(max(list_of_ints))
    max2 = max(list_of_ints)
    list_of_ints.remove(max(list_of_ints))    
    max3 = max(list_of_ints)
    list_of_ints.remove(max(list_of_ints))
    
    min1 = min(actual_list)
    actual_list.remove(min(actual_list))
    min2 = min(actual_list)
    actual_list.remove(min(actual_list))
    
    product1 = max1*max2*max3
    product2 = max1*min1*min2
    if product1 < product2:
        return product2
    else :
        return product1


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)