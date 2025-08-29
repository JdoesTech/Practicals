class Language:
    def __init__(self, root, continent, difficulty):
        self.root = root
        self.continent = continent
        #encapsulation
        self.__difficulty = difficulty

    def print_root(self):
        print("The original language is " + self.root)

    #getter
    def get_difficulty(self):   
        return self.__difficulty

    #setter
    def set_difficulty(self, new_difficulty):  
        self.__difficulty = new_difficulty

    #polymorphism
    def description(self):   
        return f"{self.root}-based language, common in {self.continent}, difficulty: {self.__difficulty}"


#inheritance
class Spanish(Language):   
    def __init__(self, root, continent, difficulty, speakers):
        super().__init__(root, continent, difficulty)
        self.speakers = speakers

    # overriding description (polymorphism)
    def description(self):
        return f"Spanish, a {self.root}-based language, spoken widely in {self.continent} by {self.speakers} million people."



lang = Language("Latin", "Europe", "Medium")
spanish = Spanish("Latin", "South America & Europe", "Easy", 480)

lang.print_root()
print(lang.description())
print(spanish.description())

# Encapsulation 
print("Old difficulty:", lang.get_difficulty())
lang.set_difficulty("Hard")
print("New difficulty:", lang.get_difficulty())

