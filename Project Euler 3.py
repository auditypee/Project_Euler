"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
largestPrime = 0
num = 600851475143

while num > 1:
    for i in xrange(2, 10000):
        if num % i == 0:
            largestPrime = i
            num /= largestPrime
            break

print(largestPrime)