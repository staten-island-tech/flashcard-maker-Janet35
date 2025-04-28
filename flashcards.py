import json
try:
    with open("flashcards.json", "r") as file:
        flashcards_data = json.load(file)
except FileNotFoundError:
    flashcards_data = []

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
    flashcard("How many collabs do SZA and Kendrick Lamar have? ", "7"),
    flashcard("When was Frank Ocean's last drop? ", "2016")
    ]

new_flashcard = flashcard("What year did The Weeknd perform at a Victoria's Secret fashion show in Paris? ", '2016')
flashcards_data.append(new_flashcard.to_dict())

flashcards_data = [flashcard.to_dict() for flashcard in flashcards]
with open("flashcards.json", "w") as file:
    json.dump(flashcards_data, file, indent=4)

streak = 6

while streak <= 9:
    for flashcard.to_dict in flashcards_data:
        answer = input(flashcard.display_info())
        if answer == flashcard.answer:
            streak += 1
            print("good job!! Streak:", streak)
        else:
            streak = 0
            print("you're not quite there yet. Try again!", "your streak is now", streak)
            break

