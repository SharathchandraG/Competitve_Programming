import unittest

def get_permutations_helper(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        x = lst[i]
        newlist = lst[:i] + lst[i+1:]
        for y in get_permutations_helper(newlist):
            l.append([x] + y)
    return l
def get_permutations(string):

    # Generate all permutations of the input string
    permutations = [''.join(p) for p in get_permutations_helper(list(string))]
    if len(permutations) == 0:
        permutations = [''] 
    return set(permutations)


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
