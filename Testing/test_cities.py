import unittest
from city_function import get_formatted_city

class CityTestCase(unittest.TestCase):
    """Test for city_function"""
    
    def test_city_country(self):
        """Do city like this "Santiago, Chile work?"""
        formatted_city = get_formatted_city("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")
        
    def test_city_country_population(self):
        """Will population works?"""
        formatted_city = get_formatted_city("santiago", "chile", "population = 5_000_000")
        self.assertEqual = (formatted_city, "Santiago, Chile - population 5000000")
        
if __name__ == "__main__":
    unittest.main()