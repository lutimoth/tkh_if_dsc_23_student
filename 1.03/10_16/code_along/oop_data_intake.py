class Fellow:
    def __init__(self, fname, track, familiars):
        self.fname = fname
        self.track = track
        self.familiars = familiars
        
student1 = Fellow("Raysa", "DS", [])

Fellow.__init__(student1, "Raysa", "DS", [])

__init__(student1, "Raysa", "DS", []):
    student1.fname = "Raysa"
    student1.track = "DS"
    student1.familiars = []

# TODO: create "Gustavo", assign him to "DS", and give him an empty list
# for familiars
person1 = Fellow("Gustavo", "DS", [])

# TODO: print out his name using the 'person1' object
print(person1.fname)

# TODO: print out his track using the 'person1' object
print(person1.track)

# TODO: call the 'print_familiars()' method
print(person1.print_familiars())