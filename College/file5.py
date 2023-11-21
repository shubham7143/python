'''polymorphism'''
class Bird:
    def intro(self):
        print("There are different types of birds")
    def flight(self):
        print("Most of the birds can fly but some cannot")
    

class Parrot(Bird):
    def flight(self):
        print("Parrots can fly")


class Pengiun(Bird):
    def flight(self):
        print("Penguins do not fly")


obj_bird = Bird()
obj_parr = Parrot()
obj_peng = Pengiun()

for bird in (obj_parr, obj_bird, obj_peng):
    bird.intro()
    bird.flight()