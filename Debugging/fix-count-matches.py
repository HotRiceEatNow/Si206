import unittest

# Return the number of items in the two lists that match.
# The lists must be sorted in ascending order.
def count_matches(list1, list2):
    if not list1 or not list2:  # Handle empty lists
        return 0

    l1 = len(list1) - 1  # Last valid index
    l2 = len(list2) - 1  # Last valid index
    count = 0

    while l1 >= 0 and l2 >= 0:  # Allow index 0
        if list1[l1] == list2[l2]:
            count += 1
            l1 -= 1
            l2 -= 1
        elif list1[l1] < list2[l2]:
            l2 -= 1
        else:
            l1 -= 1

    return count  #  returns the result

class MatchTest(unittest.TestCase):
    
    def test_none(self):
        self.assertEqual(count_matches([1, 2, 5, 7], [3, 4, 6, 8]), 0)

    def test_end(self):
        self.assertEqual(count_matches([1, 2, 3], [0, 2, 3]), 2)

    def test_front(self):
        self.assertEqual(count_matches([1, 2, 5, 8], [1, 2, 4, 7]), 2)

    def test_empty_list(self):
        self.assertEqual(count_matches([], [1, 2, 3]), 0)
        self.assertEqual(count_matches([1, 2, 3], []), 0)

    def test_identical_lists(self):
        self.assertEqual(count_matches([1, 2, 3, 4], [1, 2, 3, 4]), 4)

    def test_no_match(self):
        self.assertEqual(count_matches([1, 3, 5], [2, 4, 6]), 0)

def main():
    print("First test should print 2 and prints:")
    print(count_matches([1, 3, 7], [1, 5, 7]))

if __name__ == "__main__":
    main()
    unittest.main()
