"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt


def compute_factors(num):
    # limit = int(sqrt(num))
    limit = num // 2
    factors = []
    for d in range(2, limit):
        if num % d == 0:
            factors.append(d)
    print(len(factors))
    
    return factors


def solve_1(num):
    # Get the list of factors
    factors = compute_factors(num)
    # print(factors)

    # Get the last prime from list
    i = len(factors) - 1
    while i >= 0:
        prime = True
        for j in range(i):
            if factors[i] % factors[j] == 0:
                # print(factors[i], factors[j])
                prime = False
                break
        if prime:
            return factors[i]
        i = i - 1


def prime_factors(n):
    factors = []
    
    # Print the number of two's that divide n
    flag = False
    while n % 2 == 0:
        flag = True
        n = n / 2
    if flag:
        factors.append(2)

    for i in range(3, int(sqrt(n))+1, 2):
        flag = False
        # while i divides n , print i ad divide n
        while n % i == 0:
            flag = True
            n = n / i
        if flag:
            factors.append(i)

    if n > 2:
        factors.append(int(n))

    return factors


def solve_2(num):
    factors = prime_factors(num)
    print(factors)

    factors.sort()

    return factors[-1]


def main():
    num = int(input())
    print(solve_2(num))


if __name__ == '__main__':
    main()
