# Name: Ajanae Stanback
# Assignment: Module 7.2 - Test Cases
# Date: November 26, 2026
# Description: Unit test for the city_country function.

import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Verify that a city and country are formatted correctly."""
        formatted_city = city_country("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
