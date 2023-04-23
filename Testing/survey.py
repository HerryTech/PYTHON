class AnonymousSurvey:
    """Collect anonymous answer to a surevy question"""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Show survey question"""