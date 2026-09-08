import unittest
from Function import classify_age

class TestClassifyAge(unittest.TestCase):
    def test_minor(self):
        self.assertEqual(classify_age(10), "Minor")
    
    def test_adult(self):
        self.assertEqual(classify_age(20), "Adult")
    
    def test_adult_boundary(self):
        self.assertEqual(classify_age(18), "Adult")
    
    
if __name__ == "__main__":
    unittest.main()