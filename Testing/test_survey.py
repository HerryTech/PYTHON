import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""
    
    def test_store_single_respones(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses("English")
        self.assertIn("English", my_survey.responses)
        
    def test_store_more_respones(self):
        """Test that a all responses are stored properly."""
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question)
        responses = ["English", "Spanish", "French"]
        for response in responses:
            my_survey.store_responses(response)
        
        for response in responses:  
            self.assertIn(response, my_survey.responses)
        
if __name__ == "__main__":
    unittest.main()