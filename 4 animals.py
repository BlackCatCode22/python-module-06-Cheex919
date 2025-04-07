# sampleClass.py
#CLASS
class Animal:
    def __init__(self, name):
        self.name = name
        self.species = "Unknown"
        self.sound = "..."

    def speak(self):
        print(f"{self.name} the {self.species} makes the noise of: {self.sound}")

    def hunt(self):
        print(f"{self.name} the {self.species} is hunting down it's prey... This animal is a carnivore.")

    def rest(self):
        print(f"{self.name} the {self.species} is resting.")
    def habitat(self):
        print(f"{self.name} the {self.species} lives in:")

#BEAR
class Bear(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Bear"
        self.sound = "RWOOARGH"

    def hibernate(self):
        print(f"{self.name} the Bear hibernates in his cave. It waits for spring")

    def habitat(self):
        print(f"{self.name} The Bear lives in the Forest!")

#HYENA
class Hyena(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Hyena"
        self.sound = "Laughing"

    def scavenge(self):
        print(f"{self.name} the Hyena eats food and bones.")

    def habitat(self):
        print(f"{self.name} The Hyena lives in the Savanna!")

#LION
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Lion"
        self.sound = "Roar"

    def battle(self):
        print(f"{self.name} the Lion battles other male lions!")

    def habitat(self):
        print(f"{self.name} The Lion lives in the Grasslands!")

#TIGER
class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "Tiger"
        self.sound = "Meow"

    def stalk(self):
        print(f"{self.name} the Tiger stalks it's prey, waiting to strike.")

    def habitat(self):
        print(f"{self.name} The Tiger lives in the Jungle!")

#ENDING
if __name__ == "__main__":
    baloo = Bear("Baloo")
    shenzi = Hyena("Shenzi")
    simba = Lion("Simba")
    shere_khan = Tiger("Shere Khan")

    print(" Animal Sounds ")
    baloo.speak()
    shenzi.speak()
    simba.speak()
    shere_khan.speak()

    print("\n Special Behaviors ")
    baloo.hibernate()
    shenzi.scavenge()
    simba.battle()
    shere_khan.stalk()

    print("\n All Animals Hunting ")
    for animal in [baloo, shenzi, simba, shere_khan]:
        animal.hunt()

    print("\n All Animals Habitat ")
    for animal in [baloo, shenzi, simba, shere_khan]:
        animal.habitat()