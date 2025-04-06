import unittest

def is_palindrome(my_list):
        
        r = my_list.reverse()
        return r == my_list

class MatchTest(unittest.TestCase):

    def test_all(self):
        self.assertTrue(is_palindrome(["a"]))
        self.assertFalse(is_palindrome(["a", "b"]))
        self.assertTrue(is_palindrome(["a", "b", "a"]))
        self.assertFalse(is_palindrome(["a", "b", "c"]))
        self.assertTrue(is_palindrome(["a", "b", "c", "b", "a"]))
        self.assertTrue(is_palindrome([]))
        self.assertTrue(is_palindrome([5, 3, 3, 5]))
        self.assertFalse(is_palindrome([5, 3, 3, -5]))
        self.assertTrue(is_palindrome([5, 3, 3, 5, 3, 3, 5]))
        self.assertTrue(is_palindrome([1, 5, 1]))

unittest.main(verbosity=1)