"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def num_reverse(n):
    reverse = 0
    while n:
        r = n % 10
        n = n // 10
        reverse = reverse * 10 + r
    return reverse


def is_palindrome(n):
    reverse = num_reverse(n)

    return (n == reverse)


def solve():
    large = 0
    combination = None
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            num = i * j
            if is_palindrome(num) and num > large:
                large = num
                combination = (i, j)
    
    print(combination)
    return large


def main():
    print(solve())


if __name__ == '__main__':
    main()
