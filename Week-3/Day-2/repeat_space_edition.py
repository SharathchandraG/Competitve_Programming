import unittest


def find_repeat(the_list):

    # Find a number that appears more than once
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        
        mid = floor + ((ceiling - floor) / 2)
        lrf, lrc = floor, mid
        urf, urf = mid+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # Is it in the lower range?
            if item >= lrf and item <= lrc:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (lrc-lrf+1)
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            floor, ceiling = lrf, lrc
        else:
            floor, ceiling = urf, urf
    return floor

# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)