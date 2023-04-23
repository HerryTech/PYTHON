import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formated_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formated_name, "Janis Joplin")
    
if __name__ == "__main__":
   unittest.main() 