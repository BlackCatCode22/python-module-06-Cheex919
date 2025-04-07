# lifecycle.py
#beginning + Class
class LifeCycle:
    def __init__(self, name):
        self.name = name
        self.stage = "Egg"
        print(f"{self.name}'s life has started as an {self.stage}.")

    #life cycle
    def grow(self):
        stages = ["Egg", "Tadpole", "Tadpole with Legs", "Young Frog", "Adult Frog", "Immortal"]
        current_index = stages.index(self.stage)

        #Dead stage + Growing
        if self.stage != "Immortal":
            self.stage = stages[current_index + 1]
            print(f" your {self.name} has leveled up and grew up to an {self.stage}!")
        else:
            print(f"{self.name} is already {self.stage} and cannot grow further.")

    #Stage identifier
    def current_stage(self):
        print(f"{self.name} is currently at the {self.stage} stage.")

# ending
if __name__ == "__main__":
    frog = LifeCycle("Immortal Frog")
    frog.current_stage()
    frog.grow()
    frog.grow()
    frog.grow()
    frog.grow()
    frog.grow()
    frog.grow()  #old frog
    frog.current_stage()
