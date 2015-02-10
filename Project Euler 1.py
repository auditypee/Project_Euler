"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
multiplesOf3 = 0
multiplesOf5 = 0

for i in range(1, 1000):
    if i % 3 == 0:
        multiplesOf3 = multiplesOf3 + i
    elif i % 5 == 0:
        multiplesOf5 = multiplesOf5 + i

print(multiplesOf3 + multiplesOf5)