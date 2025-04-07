# sampleClass.py

#Class
class SampleClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    #Print
    def display(self):
        print(f"Name: {self.name}, Value: {self.value}")

    #update the value
    def update_value(self, new_value):
        self.value = new_value
        print(f"Value updated to: {self.value}")

    #ending
if __name__ == "__main__":
    obj = SampleClass("CentiPeter", 7.42)
    obj.display()
    obj.update_value(14.84)
    obj.display()
