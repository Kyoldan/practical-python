# bounce.py
#
# Exercise 1.5

current_height = 100
for i in range(10):
    current_height *= 0.6
    print(i+1, round(current_height, 4))
