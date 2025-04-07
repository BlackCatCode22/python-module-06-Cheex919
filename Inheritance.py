# inheritance.py

# class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def move(self):
        print(f"{self.name} moves around.")

# Frog Class
class Frog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.stage = "Tadpole"

    #Growing up stuff
    def metamorphose(self):
        stages = ["Tadpole", "Tadpole with Legs and arms", "Frog with tail", "Adult Frog"]
        current_index = stages.index(self.stage)
        if current_index < len(stages) - 1:
            self.stage = stages[current_index + 1]
            print(f"{self.name} grew into {self.stage}.")
        else:
            print(f"{self.name} is already an {self.stage}.")

    #final wording for adulthood
    def speak(self):
        if self.stage == "Adult Frog":
            print(f"{self.name} says: 'Ribbit!' and 'Croak!'")
        else:
            print(f"{self.name} doesn't make sounds. It's not a Frog yet!")

# Ending
if __name__ == "__main__":
    froggy = Frog("Frog the Amphibian")
    froggy.speak()
    froggy.move()
    froggy.metamorphose()
    froggy.speak()
    froggy.metamorphose()
    froggy.metamorphose()
    froggy.speak()