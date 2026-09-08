import unittest
from Function import can_login


class TestCanLogin(unittest.TestCase):

    def test_both_true(self):
        """TC1: C1=True, C2=True -> True."""
        self.assertTrue(can_login("admin", "1234"))

    def test_c1_true_c2_false(self):
        """TC2: C1=True, C2=False -> False."""
        self.assertFalse(can_login("admin", ""))

    def test_c1_false_c2_true(self):
        """TC3: C1=False, C2=True -> False."""
        self.assertFalse(can_login("", "1234"))

    def test_both_false(self):
        """TC4: C1=False, C2=False -> False."""
        self.assertFalse(can_login("", ""))


if __name__ == "__main__":
    unittest.main()