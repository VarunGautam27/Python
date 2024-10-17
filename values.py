

# for i in range(3):
#     print(random.randint(10,20))

# members= ['John', 'Marry', 'Bob', 'Mosh']
# leader=random.choice(members)
# print(leader)

# import random

# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return (first, second)

# # Create an instance of the Dice class
# dice_instance = Dice()
# # Call the roll method on the instance
# print(dice_instance.roll())

from pathlib import Path

path = Path
# print(path.rmdir())
for file in path.glob('*.py'):
    print(file)