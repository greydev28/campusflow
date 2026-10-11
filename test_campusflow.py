import unittest
from main import CampusFlow


class TestCampusFlow(unittest.TestCase):
    def setUp(self):
        self.app = CampusFlow()

    def test_high_urgency_many_users_is_critical(self):
       result = self.app.priority_level("high", 21)
       self.assertEqual(result, "critical")

    def test_high_urgency_few_users_is_high(self):
        result = self.app.priority_level("high", 3)
        self.assertEqual(result, "high")

    def test_medium_urgency_many_users_is_high(self):
        result = self.app.priority_level("medium", 15)
        self.assertEqual(result, "high")

    def test_low_urgency_is_low(self):
        result = self.app.priority_level("low", 2)
        self.assertEqual(result, "low")

if __name__ == "__main__":
    unittest.main()
