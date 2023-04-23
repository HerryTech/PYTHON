class AnonymousSurvey:
    """Collect anonymous answer to a surevy question"""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Show survey question"""
        print(self.question)
        
    def store_responses(self, new_response):
        """Store response to survey"""
        self. responses.append(new_response)
        
    def show_result(self):
        """Show all responses"""
        print("Survey result:")
        for response in self.responses:
            print(response)