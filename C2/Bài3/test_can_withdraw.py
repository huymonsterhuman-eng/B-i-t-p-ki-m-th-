import unittest
from can_withdraw import can_withdraw

class TestCanWithdraw(unittest.TestCase):

    def test_tc1_both_true(self):
        """TC1: C1=True, C2=True -> True."""
        self.assertTrue(can_withdraw(60000, 10000))

    def test_tc2_c1_true_c2_false(self):
        """TC2: C1=True, C2=False -> False."""
        self.assertFalse(can_withdraw(100000, 15000))

    def test_tc3_c1_false_c2_true(self):
        """TC3: C1=False, C2=True -> False."""
        self.assertFalse(can_withdraw(10000, 10000))

    def test_tc4_both_false(self):
        """TC4: C1=False, C2=False -> False."""
        self.assertFalse(can_withdraw(10000, 15000))

if __name__ == "__main__":
    unittest.main()