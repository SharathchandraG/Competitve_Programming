import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    l1 = len(my_list)
    l2 = len(alices_list)
    length = l1 + l2
    merged_list = [None] * length
    i,j = 0,0
    
    for k in range(length):
    	while i < l1 and j < l2:
    		if my_list[i] < alices_list[j]:
    			merged_list[k] = my_list[i]
    			k += 1
    			i += 1
    		else:
    			merged_list[k] = alices_list[j]
    			k += 1
    			j += 1
    	while i < l1:
    		merged_list[k] = my_list[i]
    		k += 1
    		i += 1
    	while j < l2:
    		merged_list[k] = alices_list[j]
    		k += 1
    		j += 1
    return merged_list

# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)