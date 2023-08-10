import random

roll1 = random.randint(1,2000)
roll2 = random.randint(1,2000)
count = 1

while roll1 != 1 or roll2 != 1:
    # print(roll1, roll2)
    roll1 = random.randint(1,2000)
    roll2 = random.randint(1,2000)
    count += 1
# print(roll1, roll2)
print(f"It took {count} tries to get 1 on both the dice.")
