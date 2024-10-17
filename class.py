# class Point:
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# point1.move()

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y =y

#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")


# point = Point(10,20)
# print(point.x)


# class Person:
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print(f"Hi, I am {self.name}")


# john = Person("JOhn smith")
# john.talk()

# bob = Person("Bob smith")
# bob.talk()

from pathlib import Path

path = Path("ecommerce1")
# print(path.rmdir())
for file in path.glob('*'):
    print(file)