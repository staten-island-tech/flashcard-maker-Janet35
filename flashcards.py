import json

class flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def display_info(self):
        return f"{self.question} {self.answer}"
    
    def to_dict(self):
        return {"answer": self.question, "answer": self.answer}
    
flashcards = [
    flashcard('Who is ur goat?', 'evb is my goat'),
    flashcard('Name three models: ', 'alex consani, niamph campbell, gigi hadid') ]

flashcards_data = [flashcard.to_dict() for flashcard in flashcards]