import json

class flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def display_info(self):
        return f"{self.question}"
    
    def to_dict(self):
        return {"question": self.question, "answer": self.answer}

flashcards = [
    flashcard('Name three models: ', 'alex consani, naomi campbell, gigi hadid'),
    ]

flashcards_data = [flashcard.to_dict() for flashcard in flashcards]
with open("flashcards.json", "w") as file:
    json.dump(flashcards_data, file, indent=4)
new_flashcard = flashcard("What year did the Weeknd perform at a Victoria's Secret fashion show in Paris?", '2016')
flashcards_data.append(new_flashcard.to_dict())

print(flashcard(self).display_info())
streak = 0
if input == flashcard.answer:
    streak =+ 1
    print("good job!! Streak: ", streak)
else:
    print("you're not quite there yet. Try again!")