class Janet:
    def display_info(self):
        return f"Teacher: {self.trait}, Email: {self.phrase}, Subject: {self.song}"

    def __init__(trait, phrase, song):
        super().__init__(song, phrase)
        self.trait = trait
    
janet = ('amazing', 'im so fire yo', 'only girl')

print(janet.trait)