import unittest
from calculate_shipping_fee import calculate_shipping_fee

class TestCalculateShippingFee(unittest.TestCase):

    def test_path1_high_amount_vip(self):
        """Path 1: total_amount>=1000000 True, is_vip True -> 0."""
        self.assertEqual(calculate_shipping_fee(1500000, True), 0)

    def test_path2_high_amount_not_vip(self):
        """Path 2: total_amount>=1000000 True, is_vip False -> 20000."""
        self.assertEqual(calculate_shipping_fee(1500000, False), 20000)

    def test_path3_low_amount_vip(self):
        """Path 3: total_amount>=1000000 False, is_vip True -> 30000."""
        self.assertEqual(calculate_shipping_fee(500000, True), 30000)

    def test_path4_low_amount_not_vip(self):
        """Path 4: total_amount>=1000000 False, is_vip False -> 50000."""
        self.assertEqual(calculate_shipping_fee(500000, False), 50000)
if __name__ == "__main__":
    unittest.main()