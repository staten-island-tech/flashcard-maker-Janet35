import json

class flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def display_info(self):
        return f"{self.question}"
    
    def to_dict(self):
        return {"answer": self.question, "answer": self.answer}

flashcards = [
    flashcard('Name three models: ', 'alex consani, naomi campbell, gigi hadid'),
    flashcard("What year did The Weeknd perform at a Victoria's Secret Fashion Show in Paris?", "2016"),
    flashcard("when did Zendaya get engaged?", '2025') 
    ]

flashcards_data = [flashcard.to_dict() for flashcard in flashcards]
with open("flashcards.json", "w") as file:
    json.dump(flashcards_data, file, indent=4)

print(flashcard.display_info())
ask = input
if input == flashcard.answer:
    streak =+ 1
    print("good job!! Streak: ", streak)