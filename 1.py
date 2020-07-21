"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples(num, limit):
    ans = 0
    for i in range(num, limit):
        if i % num == 0:
            ans += i
    return ans


def solve(limit):
    # Sum of multiple of 3
    sum3 = sum_of_multiples(3, limit)
    # sum of multiple of 5
    sum5 = sum_of_multiples(5, limit)
    # sum of multiple of 15
    sum15 = sum_of_multiples(15, limit)
    
    return sum3 + sum5 - sum15


def main():
    limit = int(input())
    print(solve(limit))


if __name__ == '__main__':
    main()
