import unittest
from app import add_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertNotEqual(add_numbers(10, 5), 20)

if __name__ == "__main__":
    unittest.main()
