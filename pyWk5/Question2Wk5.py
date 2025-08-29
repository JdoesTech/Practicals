class Animal:
    def move(self):
        print("This animal moves, not locomote.")

class Dog(Animal):
    def move(self):
        print("Runs")

class Fish(Animal):
    def move(self):
        print("Swims")

class Bird(Animal):
    def move(self):
        print("Flies")


class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driven")

class Plane(Vehicle):
    def move(self):
        print("Flown")

class Boat(Vehicle):
    def move(self):
        print("Sailed")


#Polymorphism
things = [Dog(), Fish(), Bird(), Car(), Plane(), Boat()]

for thing in things:
    thing.move()
